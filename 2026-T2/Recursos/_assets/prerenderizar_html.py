# -*- coding: utf-8 -*-
"""Pre-renderiza un Recurso HTML ya escrito (sin generador disponible).

Quita las etiquetas que dependen del CDN, convierte la matemática a SVG y
resalta el código. El resultado no lleva JavaScript.

Uso:  py -3.13 _assets/prerenderizar_html.py Recurso_XXX.html [otro.html ...]
"""
import io, os, re, sys

_ASSETS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ASSETS)
sys.stdout.reconfigure(encoding="utf-8")
from prerender import postproceso  # noqa: E402

# etiquetas que dependen de la red
PATRONES = [
    r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com[^"]*">\s*',
    r'<script src="https://cdnjs\.cloudflare\.com[^"]*"></script>\s*',
    r"<script>window\.addEventListener\('load',\(\)=>hljs\.highlightAll\(\)\);</script>\s*",
    r"<script>\s*MathJax\s*=\s*\{[\s\S]*?\};?\s*</script>\s*",
    r'<script src="https://cdn\.jsdelivr\.net[^"]*"[^>]*></script>\s*',
]

for ruta in sys.argv[1:]:
    if not os.path.isabs(ruta):
        ruta = os.path.join(os.path.dirname(_ASSETS), ruta)
    nom = os.path.basename(ruta)
    s = io.open(ruta, encoding="utf-8").read()

    if "<mjx-container" in s:
        print(f"{nom}: ya está pre-renderizado, sin cambios")
        continue

    quitados = 0
    for pat in PATRONES:
        s, n = re.subn(pat, "", s, count=1)
        quitados += n
    # dejar el marcador donde irán los estilos
    s = s.replace("<style>", "__ASSETS__\n<style>", 1)

    print(f"{nom}: {quitados} etiquetas CDN quitadas")
    s, informe = postproceso(s)
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(s)
    print(f"  -> {len(s)//1024} KB, {informe['formulas']} fórmulas, "
          f"{informe['scripts_restantes']} scripts")
