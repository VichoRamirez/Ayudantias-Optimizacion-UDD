# -*- coding: utf-8 -*-
"""Pre-renderiza un Recurso: LaTeX -> SVG y código -> HTML resaltado.

El resultado es un HTML **sin nada de JavaScript**: las fórmulas quedan como SVG
inline y el código con spans de Pygments. Así se ve igual en cualquier visor
(navegador sin red, preview del IDE, PDF) y el archivo pesa mucho menos que
incrustar el bundle de MathJax.

Requiere, una sola vez:
    cd _assets/mjnode && npm install

Uso desde un generador:
    sys.path.insert(0, _ASSETS)
    from prerender import postproceso
    HTML, informe = postproceso(HTML)
"""
import html as _html
import json
import os
import re
import subprocess
import sys
import tempfile

_ASSETS = os.path.dirname(os.path.abspath(__file__))
_MJNODE = os.path.join(_ASSETS, "mjnode")

# Regiones donde NO se busca matemática ni se toca nada.
_PROTEGIDO = re.compile(
    r"(<pre\b[\s\S]*?</pre>|<script\b[\s\S]*?</script>|<style\b[\s\S]*?</style>|<!--[\s\S]*?-->)",
    re.I,
)


# ---------------------------------------------------------------- matemática
def _escanear(texto, acumulador):
    """Reemplaza $...$ y $$...$$ por marcadores y acumula las expresiones TeX.

    Respeta `\\$` (signo de peso literal) y los escapes dentro del TeX.
    """
    salida = []
    i, n = 0, len(texto)
    while i < n:
        c = texto[i]
        if c == "\\" and i + 1 < n:
            if texto[i + 1] == "$":       # \$ en el HTML => signo de peso literal
                salida.append("$")
            else:
                salida.append(texto[i:i + 2])
            i += 2
            continue
        if c == "$":
            display = texto.startswith("$$", i)
            cierre = "$$" if display else "$"
            j = i + len(cierre)
            while j < n:
                if texto[j] == "\\":
                    j += 2
                    continue
                if texto.startswith(cierre, j):
                    break
                j += 1
            if j >= n:                    # $ suelto sin cierre: se deja tal cual
                salida.append(c)
                i += 1
                continue
            # El TeX viene del HTML, así que puede traer entidades (&lt; &gt; &amp;).
            # MathJax necesita los caracteres reales, igual que los recibiría del DOM.
            tex = _html.unescape(texto[i + len(cierre):j])
            idx = len(acumulador)
            acumulador.append({"id": idx, "tex": tex, "display": display})
            salida.append(f"\x00M{idx}\x00")
            i = j + len(cierre)
            continue
        salida.append(c)
        i += 1
    return "".join(salida)


def herramientas_listas():
    """¿Está disponible MathJax en Node? Devuelve (bool, motivo)."""
    if not os.path.isdir(os.path.join(_MJNODE, "node_modules")):
        return False, f'falta ejecutar:  cd "{_MJNODE}" && npm install'
    try:
        subprocess.run(["node", "--version"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception:
        return False, "no se encontró Node.js en el PATH"
    return True, ""


def _convertir(items):
    """Llama a MathJax en Node y devuelve (svgs, fontCache, css)."""
    tmp = tempfile.mkdtemp(prefix="mjx_")
    ein, eout = os.path.join(tmp, "in.json"), os.path.join(tmp, "out.json")
    with open(ein, "w", encoding="utf-8") as f:
        json.dump(items, f)
    subprocess.run(["node", os.path.join(_MJNODE, "tex2svg.js"), ein, eout],
                   check=True, cwd=_MJNODE,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open(eout, encoding="utf-8") as f:
        d = json.load(f)
    return d["items"], d["fontCache"], d["css"]


def matematica_a_svg(html_txt):
    """Convierte toda la matemática a SVG. Devuelve (html, css, fontcache, problemas)."""
    partes = _PROTEGIDO.split(html_txt)
    acum = []
    for k in range(0, len(partes), 2):
        partes[k] = _escanear(partes[k], acum)
    html_txt = "".join(partes)

    if not acum:
        return html_txt, "", "", []

    resultados, fontcache, css = _convertir(acum)
    problemas = []
    for it, orig in zip(resultados, acum):
        # MathJax pinta de rojo los comandos que no conoce (paquete noundefined)
        if it["error"] or 'fill="red"' in it["svg"]:
            problemas.append({"tex": orig["tex"], "error": it["error"] or "macro desconocida (sale en ROJO)"})
        html_txt = html_txt.replace(f"\x00M{it['id']}\x00", it["svg"])
    return html_txt, css, fontcache, problemas


# ---------------------------------------------------------------- código
_BLOQUE = re.compile(r'<pre><code(?: class="language-python")?>([\s\S]*?)</code></pre>')


def resaltar_codigo(html_txt):
    """Reemplaza los <pre><code> por HTML resaltado con Pygments. Devuelve (html, css)."""
    from pygments import highlight
    from pygments.lexers import PythonLexer, TextLexer
    from pygments.formatters import HtmlFormatter

    try:
        fmt = HtmlFormatter(nowrap=True, style="one-dark")
    except Exception:
        fmt = HtmlFormatter(nowrap=True, style="monokai")

    def _rep(m):
        es_python = 'class="language-python"' in m.group(0)
        fuente = _html.unescape(m.group(1))
        lexer = PythonLexer() if es_python else TextLexer()
        cuerpo = highlight(fuente, lexer, fmt).rstrip("\n")
        return f'<pre class="hl"><code>{cuerpo}</code></pre>'

    html_txt, n = _BLOQUE.subn(_rep, html_txt)
    css = fmt.get_style_defs(".hl") if n else ""
    return html_txt, css, n


# ---------------------------------------------------------------- todo junto
_CSS_BASE = """
mjx-container{display:inline-block;line-height:0;text-indent:0;text-align:left;
  font-style:normal;font-weight:normal;font-size:100%;font-size-adjust:none;
  letter-spacing:normal;word-spacing:normal;word-wrap:normal;white-space:nowrap;
  direction:ltr;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:middle}
mjx-container[display="true"]{display:block;text-align:center;margin:1em 0;overflow-x:auto}
mjx-container svg{max-width:none}
pre.hl{background:#282c34;color:#abb2bf;padding:1em;border-radius:10px;
  overflow-x:auto;font-size:.85rem;margin:12px 0}
pre.hl code{background:none;color:inherit;padding:0;font-size:inherit}
"""


# Red de seguridad: si no están las herramientas de build, el archivo igual se
# genera, pero con MathJax desde el CDN — o sea, NECESITA INTERNET para verse.
_CDN = """<!-- ATENCIÓN: fórmulas por CDN, este archivo necesita internet.
     Para dejarlo autocontenido:  cd _assets/mjnode && npm install  y regenerar. -->
<script>
MathJax = { tex: { inlineMath: [['$','$'],['\\\\(','\\\\)']],
                   displayMath: [['$$','$$'],['\\\\[','\\\\]']],
                   processEscapes: true } };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js" async></script>"""


def postproceso(html_txt, verbose=True):
    """Deja el HTML sin JavaScript: math en SVG y código resaltado."""
    listas, motivo = herramientas_listas()

    if not listas:
        # No se puede pre-renderizar: se genera igual, pero dependiendo del CDN.
        html_txt, css_code, n_bloques = resaltar_codigo(html_txt)
        html_txt = html_txt.replace(
            "__ASSETS__", f"<style>\n{_CSS_BASE}\n{css_code}\n</style>\n{_CDN}", 1)
        if verbose:
            print("  " + "!" * 68)
            print(f"  AVISO: no se pudo pre-renderizar la matemática ({motivo}).")
            print("  El archivo queda dependiendo del CDN: SIN INTERNET no se verán")
            print("  las fórmulas. Instala las herramientas y vuelve a generarlo.")
            print("  " + "!" * 68)
        return html_txt, {"formulas": 0, "bloques_codigo": n_bloques,
                          "scripts_restantes": html_txt.count("<script"),
                          "problemas": [], "modo": "CDN (requiere internet)"}

    html_txt, css_mjx, fontcache, problemas = matematica_a_svg(html_txt)
    html_txt, css_code, n_bloques = resaltar_codigo(html_txt)

    estilos = f"<style>\n{_CSS_BASE}\n{css_mjx}\n{css_code}\n</style>"
    html_txt = html_txt.replace("__ASSETS__", estilos, 1)

    if fontcache:
        # getCache() devuelve un <defs> suelto. Un <defs> directo dentro de <body> no
        # es HTML válido: el navegador lo descarta y TODAS las fórmulas salen en
        # blanco (los <use> no resuelven). Hay que envolverlo en un <svg> real.
        if not fontcache.lstrip().startswith("<svg"):
            fontcache = ('<svg style="display:none" xmlns="http://www.w3.org/2000/svg"'
                         ' aria-hidden="true" focusable="false">' + fontcache + "</svg>")
        html_txt = html_txt.replace("<body>", "<body>\n" + fontcache, 1)

    quedan = html_txt.count("<script")
    informe = {"formulas": html_txt.count("<mjx-container"),
               "bloques_codigo": n_bloques,
               "scripts_restantes": quedan,
               "problemas": problemas,
               "modo": "pre-renderizado (autocontenido)"}
    if verbose:
        print(f"  pre-render: {informe['formulas']} fórmulas, "
              f"{n_bloques} bloques de código, {quedan} <script> restantes")
        if problemas:
            print(f"  ATENCIÓN: {len(problemas)} expresiones con problemas:")
            for p in problemas[:20]:
                print(f"     [{p['error']}]  {p['tex'][:90]}")
    return html_txt, informe
