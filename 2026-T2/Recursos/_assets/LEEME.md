# Cómo se construyen los Recursos

Los archivos `Recurso_*.html` son **100 % autocontenidos y sin JavaScript**:

- los gráficos van como PNG en base64,
- las fórmulas van como **SVG ya renderizado** (no hay MathJax en el archivo),
- el código Python va resaltado con spans de Pygments (no hay highlight.js).

Así se ven igual con o sin internet, en el preview del IDE y al imprimir a PDF.

## ¿Quién necesita instalar algo?

| | ¿Necesita npm / Node / internet? |
|:--|:--|
| **Abrir un `Recurso_*.html`** (alumnos, tú, cualquiera) | **No.** Nada. El archivo ya trae todo adentro. |
| **Regenerar** un recurso (`build_Recurso_*.py`) | Sí: `npm install` una vez, y Python con matplotlib/scipy/gurobipy. |

Si alguien corre un generador **sin** haber hecho `npm install`, el build **no falla**:
produce el HTML igual, pero con las fórmulas por CDN y un aviso enorme en la consola.
Ese archivo **sí necesita internet** para verse. Es una red de seguridad, no el
resultado que se reparte: hay que instalar y regenerar.

## Preparación (una sola vez)

    cd _assets/mjnode
    npm install

Eso instala `mathjax-full`, que se usa **solo en tiempo de construcción** para
convertir LaTeX a SVG. La carpeta `node_modules/` está en `.gitignore` (pesa 47 MB).

## Generar un recurso

    cd 2026-T2/Recursos
    py -3.13 build_Recurso_Simplex.py

Cada generador imprime un informe al final:

    pre-render: 641 fórmulas, 3 bloques de código, 0 <script> restantes

Si alguna expresión tiene un macro que MathJax no conoce, aparece listada como
**problema**. Hay que arreglarla: si no, MathJax la pinta de **rojo** en el
archivo final en vez de fallar ruidosamente.

## Recursos antiguos, sin generador

    py -3.13 _assets/prerenderizar_html.py Recurso_XXX.html

Quita las etiquetas de CDN y pre-renderiza. Es idempotente.

## Verificar el resultado

No hace falta la extensión de Chrome; basta Chrome headless:

    CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
    "$CHROME" --headless --disable-gpu --virtual-time-budget=30000 \
              --no-pdf-header-footer --print-to-pdf=salida.pdf \
              "file:///C:/ruta/al/Recurso_XXX.html"

Y revisar el PDF. **Hay que mirarlo, no solo contar etiquetas**: en una versión
anterior las fórmulas existían en el DOM pero salían en blanco, y eso solo se
detecta viéndolo.

Chequeos rápidos sobre el HTML: `<script` debe dar 0, `"red"` debe dar 0
(sería un macro desconocido) y no debe haber ninguna URL `http`.
