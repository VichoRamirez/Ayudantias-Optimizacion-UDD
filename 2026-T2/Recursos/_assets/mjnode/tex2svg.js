// Convierte una lista de expresiones TeX a SVG usando MathJax 3 en Node.
// Entrada  (stdin) : JSON  [{id, tex, display}, ...]
// Salida  (stdout) : JSON  {items:[{id, svg, error}], fontCache:"<svg>...</svg>"}
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({packages: AllPackages, processEscapes: true});
const svg = new SVG({fontCache: 'global'});
const doc = mathjax.document('', {InputJax: tex, OutputJax: svg});

// Uso: node tex2svg.js entrada.json salida.json
const fs = require('fs');
(function () {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const salida = [];
  for (const it of items) {
    let html = '', error = null;
    try {
      const nodo = doc.convert(it.tex, {display: !!it.display, em: 16, ex: 8, containerWidth: 1000});
      html = adaptor.outerHTML(nodo);
      // MathJax marca los errores de TeX con data-mjx-error
      const m = html.match(/data-mjx-error="([^"]*)"/);
      if (m) error = m[1];
    } catch (e) {
      error = String(e.message || e);
    }
    salida.push({id: it.id, svg: html, error});
  }
  const cache = adaptor.outerHTML(svg.fontCache.getCache());
  const css = adaptor.textContent(svg.styleSheet(doc));
  fs.writeFileSync(process.argv[3], JSON.stringify({items: salida, fontCache: cache, css}), 'utf8');
})();
