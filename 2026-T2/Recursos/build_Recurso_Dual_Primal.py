# -*- coding: utf-8 -*-
"""Genera el Recurso HTML de Dualidad: Primal y Dual (IIP314W, 2026-T2)."""
import io, os, base64, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import linprog

sys.stdout.reconfigure(encoding="utf-8")

# --------------------------------------------------------------------
# Pre-render: la matemática se convierte a SVG y el código se resalta en
# tiempo de construcción. El HTML final NO lleva JavaScript, así que se ve
# igual con o sin red, en el preview del IDE y al imprimir a PDF.
# Requiere una sola vez:  cd _assets/mjnode && npm install
# --------------------------------------------------------------------
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_assets")
sys.path.insert(0, _ASSETS)
from prerender import postproceso  # noqa: E402




AZUL, AZUL2, ACC, VERDE, GRIS = "#0b3d62", "#1f5f8b", "#d6336c", "#2b8a3e", "#8898a8"
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": .25,
                     "figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False})


def b64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def img(key, cap=None):
    s = '<img class="plot" src="data:image/png;base64,' + IMG[key] + '">'
    if cap:
        s += '<p class="muted" style="text-align:center;margin-top:-6px">' + cap + '</p>'
    return s


IMG = {}


def region(ax, cons, xlim, ylim, n=600, color="#cfe3f2", alpha=.9):
    """cons: lista de (a, b, c, sentido) para a*X + b*Y <=/>= c."""
    X, Y = np.meshgrid(np.linspace(*xlim, n), np.linspace(*ylim, n))
    m = (X >= 0) & (Y >= 0)
    for a, bb, c, s in cons:
        m &= (a * X + bb * Y <= c) if s == "<" else (a * X + bb * Y >= c)
    ax.contourf(X, Y, m.astype(float), levels=[.5, 1.5], colors=[color], alpha=alpha)
    return m


# =====================================================================
# F1 — el par primal/dual, ambos en 2D
#   P: max 3x1+5x2 ; x1+x2<=4 ; x1+3x2<=6      -> x*=(3,1), z*=14
#   D: min 4y1+6y2 ; y1+y2>=3 ; y1+3y2>=5      -> y*=(2,1), w*=14
# =====================================================================
def fig_par():
    fig, axs = plt.subplots(1, 2, figsize=(12.6, 5.0))
    x = np.linspace(0, 8, 400)

    ax = axs[0]
    region(ax, [(1, 1, 4, "<"), (1, 3, 6, "<")], (0, 8), (0, 6))
    ax.plot(x, 4 - x, color=AZUL, lw=2.2, label=r"$x_1+x_2\leq 4$")
    ax.plot(x, (6 - x) / 3, color=ACC, lw=2.2, label=r"$x_1+3x_2\leq 6$")
    for z, st in [(6, ":"), (10, ":"), (14, "-")]:
        ax.plot(x, (z - 3 * x) / 5, color="#333", ls=st, lw=1.9 if z == 14 else 1.1,
                label=(r"$z=14$ (óptimo)" if z == 14 else None))
    ax.plot(3, 1, "o", color="#111", ms=10, zorder=6)
    ax.annotate(r"$x^*=(3,1)$" "\n" r"$z^*=14$", (3, 1), textcoords="offset points",
                xytext=(16, 26), fontsize=11, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.92, boxstyle="round,pad=.3"))
    ax.set_xlim(0, 6); ax.set_ylim(0, 4.2)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"PRIMAL: $\max\,3x_1+5x_2$", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")

    ax = axs[1]
    region(ax, [(1, 1, 3, ">"), (1, 3, 5, ">")], (0, 8), (0, 6), color="#f6dbe6")
    ax.plot(x, 3 - x, color=AZUL, lw=2.2, label=r"$y_1+y_2\geq 3$")
    ax.plot(x, (5 - x) / 3, color=ACC, lw=2.2, label=r"$y_1+3y_2\geq 5$")
    for w, st in [(20, ":"), (17, ":"), (14, "-")]:
        ax.plot(x, (w - 4 * x) / 6, color="#333", ls=st, lw=1.9 if w == 14 else 1.1,
                label=(r"$w=14$ (óptimo)" if w == 14 else None))
    ax.plot(2, 1, "o", color="#111", ms=10, zorder=6)
    ax.annotate(r"$y^*=(2,1)$" "\n" r"$w^*=14$", (2, 1), textcoords="offset points",
                xytext=(20, 24), fontsize=11, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.92, boxstyle="round,pad=.3"))
    ax.set_xlim(0, 6); ax.set_ylim(0, 4.2)
    ax.set_xlabel(r"$y_1$"); ax.set_ylabel(r"$y_2$")
    ax.set_title(r"DUAL: $\min\,4y_1+6y_2$", color=ACC, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")

    fig.suptitle(r"Dualidad fuerte: dos problemas distintos, el mismo número  $z^*=w^*=14$",
                 fontsize=12.5, fontweight="bold", color=AZUL, y=1.02)
    fig.tight_layout()
    return b64(fig)


IMG["par"] = fig_par()


# =====================================================================
# F2 — dualidad debil: el sandwich
# =====================================================================
def fig_sandwich():
    fig, ax = plt.subplots(figsize=(11.0, 4.2))
    ax.axvspan(-2, 14, color="#e3f2e8")
    ax.axvspan(14, 30, color="#fdeaf1")
    ax.axvline(14, color="#111", lw=2.6, zorder=5)
    ax.text(14, 1.28, r"$z^*=w^*=14$", ha="center", fontsize=12.5, fontweight="bold",
            bbox=dict(fc="white", ec="#111", boxstyle="round,pad=.35"), zorder=7)
    # (valor, etiqueta, desplazamiento vertical de la etiqueta en puntos)
    prim = [(0, r"$x=(0,0)$", 15), (11, r"$x=(2,1)$", 15), (12, r"$x=(4,0)$", 34),
            (14, r"$x^*=(3,1)$", 15)]
    dual = [(14, r"$y^*=(2,1)$", -24), (15, r"$y=(1{,}5;\,1{,}5)$", -43),
            (18, r"$y=(3,1)$", -24), (20, r"$y=(5,0)$", -43)]
    for v, lab, dy in prim:
        ax.plot(v, .18, "o", color=VERDE, ms=9, zorder=6)
        ax.annotate(lab, (v, .18), textcoords="offset points", xytext=(0, dy),
                    ha="center", fontsize=8.8, color=VERDE, fontweight="bold")
    for v, lab, dy in dual:
        ax.plot(v, -.18, "s", color=ACC, ms=9, zorder=6)
        ax.annotate(lab, (v, -.18), textcoords="offset points", xytext=(0, dy),
                    ha="center", fontsize=8.8, color=ACC, fontweight="bold")
    ax.annotate("", xy=(13.5, .95), xytext=(0.5, .95),
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=2.2))
    ax.text(7, 1.03, r"todo $x$ factible del primal da $c^\top x\leq 14$",
            ha="center", fontsize=10.5, color=VERDE, fontweight="bold")
    ax.annotate("", xy=(14.5, -1.05), xytext=(28, -1.05),
                arrowprops=dict(arrowstyle="->", color=ACC, lw=2.2))
    ax.text(21.5, -1.32, r"todo $y$ factible del dual da $b^\top y\geq 14$",
            ha="center", fontsize=10.5, color=ACC, fontweight="bold")
    ax.set_xlim(-2, 30); ax.set_ylim(-1.6, 1.6)
    ax.set_yticks([]); ax.grid(False)
    ax.set_xlabel("valor de la función objetivo")
    ax.set_title("Dualidad débil: el dual acota al primal por arriba, y el óptimo es donde se tocan",
                 color=AZUL, fontweight="bold", fontsize=11.5)
    return b64(fig)


IMG["sandwich"] = fig_sandwich()


# =====================================================================
# F3 — Molino Del Sur:  max 4x1+3x2 ; 2x1+x2<=10 ; x1+x2<=7 ; x1<=4
# =====================================================================
def fig_molino():
    fig, ax = plt.subplots(figsize=(7.4, 5.4))
    x = np.linspace(0, 12, 400)
    region(ax, [(2, 1, 10, "<"), (1, 1, 7, "<"), (1, 0, 4, "<")], (0, 12), (0, 12))
    ax.plot(x, 10 - 2 * x, color=AZUL, lw=2.2, label=r"trigo: $2x_1+x_2\leq10$")
    ax.plot(x, 7 - x, color=ACC, lw=2.2, label=r"molienda: $x_1+x_2\leq7$")
    ax.axvline(4, color=VERDE, lw=2.2, label=r"cuota: $x_1\leq4$")
    for z, st in [(12, ":"), (18, ":"), (24, "-")]:
        ax.plot(x, (z - 4 * x) / 3, color="#333", ls=st, lw=1.9 if z == 24 else 1.1,
                label=(r"$z=24$ (óptimo)" if z == 24 else None))
    ax.plot(3, 4, "o", color="#111", ms=10, zorder=6)
    ax.annotate(r"$x^*=(3,4)$,  $z^*=24$", (3, 4), textcoords="offset points",
                xytext=(-142, -30), fontsize=10.5, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.95, boxstyle="round,pad=.3"),
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.annotate("la cuota sobra:\n$s_3=1$", xy=(3.5, 2.4), xytext=(4.6, 3.4), fontsize=9.5,
                color=VERDE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=1.4))
    ax.plot([3, 4], [2.4, 2.4], color=VERDE, lw=2.4)
    ax.set_xlim(0, 8); ax.set_ylim(0, 9)
    ax.set_xlabel(r"$x_1$ — harina integral (quintales)")
    ax.set_ylabel(r"$x_2$ — harina blanca (quintales)")
    ax.set_title("Molino Del Sur", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")
    return b64(fig)


IMG["molino"] = fig_molino()


# =====================================================================
# F4 — AquaNutri: restriccion >= y precio sombra negativo
# =====================================================================
def fig_aqua():
    fig, axs = plt.subplots(1, 2, figsize=(12.6, 4.9))
    ax = axs[0]
    x = np.linspace(0, 1400, 500)
    region(ax, [(1, 1, 1100, "<"), (0, .5, 150, "<"), (.8, .5, 900, "<"), (1, 0, 900, ">")],
           (0, 1400), (0, 500))
    ax.plot(x, 1100 - x, color=AZUL, lw=2.2, label=r"extrusora: $x_1+x_2\leq1100$")
    ax.axhline(300, color=ACC, lw=2.2, label=r"harina: $0{,}5x_2\leq150$")
    ax.plot(x, (900 - .8 * x) / .5, color=GRIS, lw=2.2, label=r"soya: $0{,}8x_1+0{,}5x_2\leq900$")
    ax.axvline(900, color=VERDE, lw=2.6, label=r"contrato: $x_1\geq900$")
    ax.plot(900, 200, "o", color="#111", ms=10, zorder=6)
    ax.annotate(r"$x^*=(900,\,200)$", (900, 200), textcoords="offset points",
                xytext=(48, 46), fontsize=10.5, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.95, boxstyle="round,pad=.3"),
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.plot(800, 300, "^", color=VERDE, ms=10, zorder=6)
    ax.annotate("sin contrato el óptimo\nsería $(800,300)$",
                (800, 300), textcoords="offset points", xytext=(-40, -84), fontsize=9,
                color=VERDE, fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="->", color=VERDE))
    ax.set_xlim(600, 1250); ax.set_ylim(0, 420)
    ax.set_xlabel(r"$x_1$ — Engorda (t)"); ax.set_ylabel(r"$x_2$ — Smolt (t)")
    ax.set_title("(a) El contrato empuja el óptimo hacia abajo", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.4, loc="upper right")

    ax = axs[1]
    bb = np.linspace(600, 1100, 600)
    zz = np.array([
        -linprog(c=[-530, -550], A_ub=[[1, 1], [0, .5], [.8, .5], [-1, 0]],
                 b_ub=[1100, 150, 900, -b], bounds=[(0, None)] * 2, method="highs").fun
        for b in bb])
    ax.plot(bb, zz / 1000, color=AZUL, lw=2.6)
    ax.plot(900, 587, "o", color="#111", ms=9, zorder=5)
    ax.plot(bb, (605000 - 20 * bb) / 1000, color=ACC, ls="--", lw=1.5,
            label=r"recta de pendiente $\pi_C=-20$")
    ax.axvline(800, color=GRIS, ls=":", lw=1.4)
    ax.text(660, 588.3, r"$\pi_C=0$", color=GRIS, fontsize=10, fontweight="bold")
    ax.text(1000, 586.6, r"$\pi_C=-20$", color=ACC, fontsize=10.5, fontweight="bold")
    ax.annotate("el contrato no muerde:\nvale 0", xy=(760, 589), xytext=(640, 584.4),
                fontsize=8.8, color=GRIS,
                arrowprops=dict(arrowstyle="->", color=GRIS))
    ax.annotate(r"hoy: $b_C=900$", (900, 587), textcoords="offset points", xytext=(-110, -30),
                fontsize=9.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.set_xlabel(r"$b_C$ — toneladas comprometidas por contrato")
    ax.set_ylabel(r"$z^*$  (\$ millones)")
    ax.set_title(r"(b) Subir el piso $\Rightarrow$ el óptimo BAJA", color=ACC, fontweight="bold")
    ax.legend(fontsize=9, loc="lower left")
    fig.tight_layout()
    return b64(fig)


IMG["aqua"] = fig_aqua()


# =====================================================================
# F5 — patologias
# =====================================================================
def fig_patol():
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.7))
    ax = axs[0]
    x = np.linspace(0, 12, 400)
    region(ax, [(-1, 1, 1, "<"), (1, -1, 1, "<")], (0, 12), (0, 12))
    ax.plot(x, x + 1, color=AZUL, lw=2.2, label=r"$-x_1+x_2\leq1$")
    ax.plot(x, x - 1, color=ACC, lw=2.2, label=r"$x_1-x_2\leq1$")
    for z in [4, 8, 14, 20]:
        ax.plot(x, z - x, color="#333", ls=":", lw=1.1)
    ax.annotate("", xy=(9.2, 9.2), xytext=(2.2, 2.2),
                arrowprops=dict(arrowstyle="->", color="#111", lw=2.4))
    ax.text(4.4, 7.4, r"$z=x_1+x_2\to+\infty$", fontsize=11.5, fontweight="bold", color="#111",
            rotation=45, rotation_mode="anchor")
    ax.set_xlim(0, 11); ax.set_ylim(0, 11)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(a) PRIMAL no acotado: $\max\,x_1+x_2$", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")

    ax = axs[1]
    y = np.linspace(0, 11, 400)
    Y1, Y2 = np.meshgrid(np.linspace(0, 11, 500), np.linspace(0, 11, 500))
    ax.contourf(Y1, Y2, (Y2 >= Y1 + 1).astype(float), levels=[.5, 1.5], colors=["#cfe3f2"], alpha=.75)
    ax.contourf(Y1, Y2, (Y1 >= Y2 + 1).astype(float), levels=[.5, 1.5], colors=["#f6dbe6"], alpha=.75)
    ax.plot(y, y + 1, color=AZUL, lw=2.2, label=r"$-y_1+y_2\geq1$")
    ax.plot(y, y - 1, color=ACC, lw=2.2, label=r"$y_1-y_2\geq1$")
    ax.text(1.6, 8.0, r"$y_2\geq y_1+1$", color=AZUL, fontsize=11, fontweight="bold", rotation=45)
    ax.text(6.2, 2.2, r"$y_1\geq y_2+1$", color=ACC, fontsize=11, fontweight="bold", rotation=45)
    ax.text(5.5, 5.6, "las dos zonas\nNO se cruzan", fontsize=11.5, fontweight="bold",
            color="#111", ha="center",
            bbox=dict(fc="white", ec="#111", boxstyle="round,pad=.35", alpha=.95))
    ax.set_xlim(0, 11); ax.set_ylim(0, 11)
    ax.set_xlabel(r"$y_1$"); ax.set_ylabel(r"$y_2$")
    ax.set_title(r"(b) DUAL infactible: $\min\,y_1+y_2$", color=ACC, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout()
    return b64(fig)


IMG["patol"] = fig_patol()

print("figuras listas:", {k: len(v) // 1024 for k, v in IMG.items()}, "KB")

# =====================================================================
#                               HTML
# =====================================================================
HEAD = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Recurso de estudio — Primal y Dual | IIP314W UDD</title>
__ASSETS__
<style>
:root{--azul:#0b3d62;--azul2:#1f5f8b;--acc:#d6336c;--verde:#2b8a3e;--bg:#f6f8fb;--card:#fff;--mut:#5b6b7b;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#1a2733;background:var(--bg);line-height:1.6}
header.top{background:linear-gradient(135deg,var(--azul),var(--azul2));color:#fff;padding:34px 22px}
header.top h1{margin:0 0 6px;font-size:1.5rem}
header.top .sub{font-size:1.05rem;opacity:.95}
header.top .meta{margin-top:14px;font-size:.9rem;opacity:.9}
.wrap{max-width:1000px;margin:0 auto;padding:0 18px}
nav.toc{background:var(--card);border:1px solid #e2e8f0;border-radius:12px;padding:16px 22px;margin:22px auto;max-width:1000px}
nav.toc h2{margin:0 0 8px;font-size:1rem;color:var(--azul)}
nav.toc ol{margin:0;padding-left:20px;columns:2;column-gap:30px}
nav.toc a{color:var(--azul2);text-decoration:none}
nav.toc a:hover{text-decoration:underline}
section{background:var(--card);border:1px solid #e7edf3;border-radius:12px;padding:22px 26px;margin:18px auto;max-width:1000px;box-shadow:0 1px 2px rgba(0,0,0,.03)}
h2.part{color:#fff;background:var(--azul);border-radius:10px;padding:12px 18px;margin:26px auto;max-width:1000px;font-size:1.2rem}
h3{color:var(--azul);border-bottom:2px solid #e7edf3;padding-bottom:6px;margin-top:26px}
h4{color:var(--azul2);margin:18px 0 6px}
.badge{display:inline-block;background:#e7f0f7;color:var(--azul2);border-radius:6px;padding:2px 9px;font-size:.78rem;font-weight:600;margin-bottom:6px}
.app{border-left:4px solid var(--verde);background:#f1f8f3;padding:10px 14px;border-radius:0 8px 8px 0;margin:14px 0}
.app b{color:var(--verde)}
.tip{border-left:4px solid var(--acc);background:#fdf2f6;padding:10px 14px;border-radius:0 8px 8px 0;margin:14px 0}
.tip b{color:var(--acc)}
.key{border-left:4px solid var(--azul2);background:#eef5fb;padding:10px 14px;border-radius:0 8px 8px 0;margin:14px 0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.93rem}
th,td{border:1px solid #d8e2ec;padding:7px 10px;text-align:center}
th{background:var(--azul);color:#fff}
tr:nth-child(even) td{background:#f4f8fb}
td.l,th.l{text-align:left}
td.no{background:#fdeaf1 !important;color:#a01746;font-weight:600}
td.si{background:#e8f5ec !important;color:#1c6b2c;font-weight:600}
pre{border-radius:10px;overflow:auto;font-size:.85rem;margin:12px 0}
code{font-family:"SFMono-Regular",Consolas,Menlo,monospace}
p code,li code,td code{background:#eef2f6;color:#b5266b;padding:1px 5px;border-radius:4px;font-size:.9em}
img.plot{display:block;max-width:100%;height:auto;margin:14px auto;border:1px solid #e7edf3;border-radius:8px}
.muted{color:var(--mut);font-size:.9rem}
details{margin:8px 0;background:#f4f8fb;border:1px solid #dde7f0;border-radius:8px;padding:6px 12px}
summary{cursor:pointer;font-weight:600;color:var(--azul2)}
footer{text-align:center;color:var(--mut);font-size:.85rem;padding:30px 18px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:680px){nav.toc ol{columns:1}.grid2{grid-template-columns:1fr}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="badge" style="background:rgba(255,255,255,.2);color:#fff">IIP314W-2 · 2026-T2</div>
    <h1>Recurso de estudio — Primal y Dual</h1>
    <div class="sub">Cómo se construye el dual, qué garantizan los teoremas de dualidad y qué significa cada número en términos de negocio</div>
    <div class="meta">
      <b>Optimización Aplicada a Negocios</b> · Universidad del Desarrollo<br>
      Profesor: Rodrigo Trigo Vilches · Ayudante: Vicente Ramírez
    </div>
  </div>
</header>

<nav class="toc">
  <h2>Contenido</h2>
  <ol>
    <li><a href="#intro">Cómo usar este recurso</a></li>
    <li><a href="#d1">1. ¿De dónde sale el dual?</a></li>
    <li><a href="#d2">2. El par canónico</a></li>
    <li><a href="#d3">3. Reglas generales de construcción</a></li>
    <li><a href="#d4">4. El dual del dual</a></li>
    <li><a href="#t1">5. Dualidad débil</a></li>
    <li><a href="#t2">6. Dualidad fuerte y casos posibles</a></li>
    <li><a href="#t3">7. Holguras complementarias</a></li>
    <li><a href="#i1">8. El dual como el problema del comprador</a></li>
    <li><a href="#i2">9. Signos y duales negativos</a></li>
    <li><a href="#x1">Ej. 1 — El par en 2D</a></li>
    <li><a href="#x2">Ej. 2 — Molino Del Sur (completo)</a></li>
    <li><a href="#x3">Ej. 3 — Dual de un problema mixto</a></li>
    <li><a href="#x4">Ej. 4 — Dieta: primal de mínimo</a></li>
    <li><a href="#x5">Ej. 5 — AquaNutrí: dual negativo</a></li>
    <li><a href="#x6">Ej. 6 — Patologías</a></li>
    <li><a href="#gur">10. Todo esto en Gurobi</a></li>
    <li><a href="#trampas">11. Diez trampas clásicas</a></li>
    <li><a href="#cheat">Resumen / cheat-sheet</a></li>
    <li><a href="#prac">Ejercicios propuestos</a></li>
  </ol>
</nav>

<section id="intro">
  <h3>Cómo usar este recurso</h3>
  <p>A todo programa lineal —el <b>primal</b>— le corresponde otro programa lineal, el <b>dual</b>, que contiene <i>la misma información vista desde el otro lado</i>: si el primal decide <b>cuánto producir</b>, el dual decide <b>cuánto vale cada recurso</b>. Este documento cubre las tres cosas que hay que saber hacer con ese par: <b>construirlo</b> (secciones 1–4), <b>usar los teoremas</b> que lo relacionan (5–7) e <b>interpretarlo</b> económicamente (8–9). Después vienen <b>seis ejemplos resueltos</b> y el bloque de Gurobi, trampas y práctica.</p>
  <div class="key"><b>Notación.</b> Primal en forma canónica de maximización, $\max\{c^\top x:\;Ax\le b,\;x\ge0\}$, con $n$ variables y $m$ restricciones. Dual: $\min\{b^\top y:\;A^\top y\ge c,\;y\ge0\}$, con $m$ variables y $n$ restricciones. Escribimos $z=c^\top x$ para el objetivo primal y $w=b^\top y$ para el dual. Todos los números fueron verificados con <code>gurobipy</code>.</div>
  <div class="tip"><b>Relación con el otro recurso.</b> Aquí se construye y se demuestra; en el <b>Recurso de precios sombra y análisis de sensibilidad</b> se <i>usa</i> el dual para responder preguntas de negocio (rangos de validez, cuánto pagar por un recurso). La holgura complementaria aparece en ambos: acá con su demostración, allá como receta de cálculo.</div>
</section>
"""

# ---------------------------------------------------------------- Bloque I
B1 = r"""
<h2 class="part" id="p1">Bloque I — Cómo se construye el dual</h2>

<section id="d1">
  <h3>1. ¿De dónde sale el dual? La idea de <i>acotar</i></h3>
  <p>El dual no es una definición arbitraria que hay que memorizar: <b>aparece solo</b> cuando uno intenta responder una pregunta natural. Tomemos un primal chico:</p>
  $$\max\; z=3x_1+5x_2\qquad\text{s.a.}\quad \underbrace{x_1+x_2\le4}_{\text{R1}},\quad \underbrace{x_1+3x_2\le6}_{\text{R2}},\quad x_1,x_2\ge0$$
  <p>Antes de resolverlo, pregunta: <b>¿puedo demostrar que $z$ nunca pasa de cierto número?</b> Sí, combinando restricciones. Multiplico R1 por $2$ y R2 por $1$ (ambos multiplicadores <b>no negativos</b>, para no dar vuelta las desigualdades) y sumo:</p>
  $$2(x_1+x_2)+1(x_1+3x_2)\;\le\;2(4)+1(6)\qquad\Longrightarrow\qquad 3x_1+5x_2\;\le\;14.$$
  <p>El lado izquierdo quedó <b>exactamente</b> igual a la función objetivo, así que acabamos de probar que $z\le14$ para <b>todo</b> punto factible, <b>sin resolver nada</b>.</p>
  <div class="key"><b>Generalicemos.</b> Buscamos multiplicadores $y_1,y_2\ge0$ tales que la combinación $y_1\text{R1}+y_2\text{R2}$ tenga un lado izquierdo que <b>domine</b> a la objetivo, coeficiente por coeficiente:
  $$\underbrace{y_1+y_2\;\ge\;3}_{\text{coeficiente de }x_1},\qquad \underbrace{y_1+3y_2\;\ge\;5}_{\text{coeficiente de }x_2}$$
  Con eso, para todo $x\ge0$ factible: $\;3x_1+5x_2\le (y_1+y_2)x_1+(y_1+3y_2)x_2 \le 4y_1+6y_2$. La cota es $\;4y_1+6y_2$. Y como queremos <b>la mejor cota posible</b>, la minimizamos.</div>
  $$\boxed{\;\min\; w=4y_1+6y_2\qquad\text{s.a.}\quad y_1+y_2\ge3,\quad y_1+3y_2\ge5,\quad y_1,y_2\ge0\;}$$
  <p><b>Eso es el dual.</b> No salió de ninguna receta: salió de preguntarse cuál es la mejor cota superior demostrable por combinación de restricciones. Las restricciones duales dicen "la combinación tiene que dominar a la objetivo"; la objetivo dual es "el valor de la cota"; y $y\ge0$ está para no invertir las desigualdades.</p>
  <div class="app"><b>Y la respuesta es exacta.</b> El teorema de dualidad fuerte (sección 6) dice que la mejor cota demostrable <b>coincide</b> con el óptimo verdadero: no hay brecha. En este ejemplo, $z^*=w^*=14$, y los multiplicadores óptimos son justamente los $2$ y $1$ con que empezamos.</div>
</section>

<section id="d2">
  <h3>2. El par canónico</h3>
  <p>Repitiendo el argumento con letras se obtiene el par que hay que tener memorizado:</p>
  <div class="grid2">
    <div class="key" style="border-color:var(--azul2)">
      <b>PRIMAL</b>
      $$\max\; z=c^\top x$$
      $$\text{s.a.}\quad Ax\le b$$
      $$x\ge0$$
      <p class="muted">$n$ variables, $m$ restricciones</p>
    </div>
    <div class="tip" style="border-color:var(--acc)">
      <b>DUAL</b>
      $$\min\; w=b^\top y$$
      $$\text{s.a.}\quad A^\top y\ge c$$
      $$y\ge0$$
      <p class="muted">$m$ variables, $n$ restricciones</p>
    </div>
  </div>
  <table>
    <tr><th class="l">En el primal...</th><th class="l">...le corresponde en el dual</th></tr>
    <tr><td class="l">la restricción $i$ (recurso $i$)</td><td class="l">la variable $y_i$ (precio del recurso $i$)</td></tr>
    <tr><td class="l">la variable $x_j$ (producto $j$)</td><td class="l">la restricción $j$ (rentabilidad del producto $j$)</td></tr>
    <tr><td class="l">el lado derecho $b_i$ (disponibilidad)</td><td class="l">el coeficiente objetivo de $y_i$</td></tr>
    <tr><td class="l">el coeficiente objetivo $c_j$ (margen)</td><td class="l">el lado derecho de la restricción $j$</td></tr>
    <tr><td class="l">la matriz $A$</td><td class="l">la matriz <b>transpuesta</b> $A^\top$</td></tr>
    <tr><td class="l">maximizar</td><td class="l">minimizar</td></tr>
  </table>
  <div class="tip"><b>Chequeo de dimensiones (vale oro en el certamen).</b> Si el primal tiene 3 variables y 5 restricciones, el dual tiene <b>5 variables y 3 restricciones</b>. Si le salieron otras dimensiones, se equivocó antes de empezar a pensar.</div>
</section>

<section id="d3">
  <h3>3. Reglas generales: primales con $\le$, $\ge$, $=$ y variables libres</h3>
  <p>En la práctica los modelos de negocio mezclan tipos de restricción. La tabla completa para un <b>primal de maximización</b> es:</p>
  <table>
    <tr><th class="l">Primal ($\max\,c^\top x$)</th><th class="l">Dual ($\min\,b^\top y$)</th></tr>
    <tr><td class="l">restricción $i$ de tipo $\le b_i$</td><td class="l">variable $y_i\;\ge0$</td></tr>
    <tr><td class="l">restricción $i$ de tipo $\ge b_i$</td><td class="l">variable $y_i\;\le0$</td></tr>
    <tr><td class="l">restricción $i$ de tipo $= b_i$</td><td class="l">variable $y_i$ <b>libre</b></td></tr>
    <tr><td class="l">variable $x_j\ge0$</td><td class="l">restricción $j$ de tipo $\ge c_j$</td></tr>
    <tr><td class="l">variable $x_j\le0$</td><td class="l">restricción $j$ de tipo $\le c_j$</td></tr>
    <tr><td class="l">variable $x_j$ <b>libre</b></td><td class="l">restricción $j$ de tipo $= c_j$</td></tr>
  </table>
  <p>Y si el <b>primal es de minimización</b>, todo se invierte:</p>
  <table>
    <tr><th class="l">Primal ($\min\,c^\top x$)</th><th class="l">Dual ($\max\,b^\top y$)</th></tr>
    <tr><td class="l">restricción $\ge b_i$</td><td class="l">$y_i\ge0$</td></tr>
    <tr><td class="l">restricción $\le b_i$</td><td class="l">$y_i\le0$</td></tr>
    <tr><td class="l">restricción $= b_i$</td><td class="l">$y_i$ libre</td></tr>
    <tr><td class="l">variable $x_j\ge0$</td><td class="l">restricción $\le c_j$</td></tr>
    <tr><td class="l">variable $x_j$ libre</td><td class="l">restricción $= c_j$</td></tr>
  </table>
  <div class="key"><b>La regla que resume las dos tablas.</b> Una restricción se llama <b>"del mismo sentido"</b> que su objetivo cuando es $\le$ en un máximo o $\ge$ en un mínimo. Entonces:
  <ul style="margin:6px 0">
    <li>restricción <b>del mismo sentido</b> ⟹ variable dual $\ge0$;</li>
    <li>restricción <b>del sentido contrario</b> ⟹ variable dual $\le0$;</li>
    <li>restricción de <b>igualdad</b> ⟹ variable dual <b>libre</b>;</li>
    <li>y simétricamente: variable $\ge0$ ⟹ restricción dual del mismo sentido que <i>su</i> objetivo; variable libre ⟹ restricción dual de <b>igualdad</b>.</li>
  </ul></div>
  <div class="tip"><b>No hace falta memorizar la segunda tabla.</b> Toda restricción $\ge$ se convierte en $\le$ multiplicando por $-1$: $\;a_i^\top x\ge b_i \iff -a_i^\top x\le -b_i$. Toda igualdad se parte en dos desigualdades. Toda variable libre se escribe $x_j=x_j^+-x_j^-$ con ambas $\ge0$. Y todo mínimo es un máximo del negativo. Es decir: <b>siempre</b> se puede llevar al par canónico. El precio de hacerlo es que el dual queda escrito en otras variables; la tabla general evita esa traducción.</div>
  <h4>Receta paso a paso</h4>
  <ol>
    <li>Verifique el <b>sentido de la objetivo</b> primal y elija la tabla.</li>
    <li>Cuente: $m$ restricciones ⟹ $m$ variables duales. Bautícelas $y_1,\dots,y_m$ <b>en orden</b>.</li>
    <li>Escriba la <b>objetivo dual</b> $b^\top y$ con el sentido opuesto.</li>
    <li>Por cada <b>variable primal</b> $x_j$, escriba una restricción dual: su lado izquierdo es la <b>columna $j$</b> de $A$ multiplicada por $y$, y su lado derecho es $c_j$. El tipo lo da la tabla.</li>
    <li>Escriba el <b>signo</b> de cada $y_i$ según el tipo de la restricción primal $i$.</li>
    <li><b>Chequee dimensiones</b> y verifique con un punto: evalúe $c^\top x$ en un $x$ factible y $b^\top y$ en un $y$ factible; la desigualdad de dualidad débil debe cumplirse.</li>
  </ol>
</section>

<section id="d4">
  <h3>4. El dual del dual es el primal</h3>
  <p>La relación es <b>simétrica</b>: no hay un problema "principal" y otro "secundario". Tomemos el dual canónico y dualicémoslo. Primero lo llevamos a forma de máximo con $\le$:</p>
  $$\min\; b^\top y,\;\; A^\top y\ge c,\;\;y\ge0 \qquad\Longleftrightarrow\qquad \max\; (-b)^\top y,\;\; (-A^\top)y\le -c,\;\;y\ge0$$
  <p>Aplicando la regla canónica con "$c$"$=-b$, "$A$"$=-A^\top$ y "$b$"$=-c$, el dual de esto es</p>
  $$\min\; (-c)^\top x,\;\; (-A^\top)^\top x\ge -b,\;\;x\ge0 \qquad\Longleftrightarrow\qquad \max\; c^\top x,\;\;Ax\le b,\;\;x\ge0.$$
  <p>que es el primal original. $\blacksquare$</p>
  <div class="app"><b>Consecuencia práctica.</b> Si un problema tiene <b>muchas restricciones y pocas variables</b>, su dual tiene pocas restricciones y muchas variables — y el Simplex es mucho más rápido cuando hay pocas restricciones. Resolver el dual y recuperar el primal por holgura complementaria es una técnica estándar, no un truco de examen.</div>
  <div class="key"><b>Lo mismo pasa con los precios sombra.</b> Si resuelve el dual, <b>los precios sombra del dual son la solución óptima del primal</b>. Lo verá literalmente en el Ejemplo 1: Gurobi entrega <code>Pi</code> del dual $=(3,1)=x^*$.</div>
</section>
"""

# ---------------------------------------------------------------- Bloque II
B2 = r"""
<h2 class="part" id="p2">Bloque II — Los tres teoremas</h2>

<section id="t1">
  <h3>5. Dualidad débil</h3>
  <div class="key"><b>Teorema.</b> Si $x$ es factible para el primal ($\max$) e $y$ es factible para el dual ($\min$), entonces
  $$\boxed{\;c^\top x\;\le\;b^\top y\;}$$
  Es decir, <b>todo</b> valor dual factible es una cota superior de <b>todo</b> valor primal factible.</div>
  <h4>Demostración (tres líneas)</h4>
  $$c^\top x \;\underset{(1)}{\le}\; (A^\top y)^\top x \;=\; y^\top A x \;\underset{(2)}{\le}\; y^\top b \;=\; b^\top y$$
  <p>En $(1)$ se usa $A^\top y\ge c$ junto con $x\ge0$ (multiplicar una desigualdad por algo no negativo la conserva). En $(2)$ se usa $Ax\le b$ junto con $y\ge0$. <b>Los signos de no negatividad no son decoración: son lo que hace funcionar la demostración.</b> $\blacksquare$</p>
  """ + img("sandwich", "Con los datos del Ejemplo 1: todo punto primal factible cae a la izquierda del 14 y todo punto dual factible a la derecha. El óptimo es exactamente donde se tocan.") + r"""
  <h4>Tres corolarios que se usan todo el tiempo</h4>
  <table>
    <tr><th>#</th><th class="l">Corolario</th><th class="l">Para qué sirve</th></tr>
    <tr><td>C1</td><td class="l">Si encuentra $x$ e $y$ factibles con $c^\top x = b^\top y$, <b>ambos son óptimos</b>.</td><td class="l">Es un <b>certificado</b>: demuestra optimalidad sin ejecutar el Simplex</td></tr>
    <tr><td>C2</td><td class="l">Si el primal es <b>no acotado</b>, el dual es <b>infactible</b>.</td><td class="l">Si $z\to\infty$ ninguna cota finita puede existir</td></tr>
    <tr><td>C3</td><td class="l">Si el dual es <b>no acotado</b> ($w\to-\infty$), el primal es <b>infactible</b>.</td><td class="l">Simétrico al anterior</td></tr>
  </table>
  <div class="app"><b>Uso típico en la práctica.</b> Un modelo grande corre 40 minutos y usted necesita saber si vale la pena esperar. Un punto dual factible cualquiera le da de inmediato una <b>garantía</b>: "el óptimo no puede superar los \$14 millones". Eso es exactamente lo que hace el <i>gap</i> que reporta Gurobi mientras resuelve.</div>
</section>

<section id="t2">
  <h3>6. Dualidad fuerte y qué combinaciones son posibles</h3>
  <div class="key"><b>Teorema (dualidad fuerte).</b> Si el primal tiene una solución óptima finita $x^*$, entonces el dual también tiene óptimo finito $y^*$ y
  $$\boxed{\;c^\top x^* = b^\top y^*\;}$$
  <b>No hay brecha de dualidad</b> en programación lineal. (En programación entera <b>sí la hay</b>: ese hueco es el <i>gap</i> de la relajación lineal.)</div>
  <p>La demostración estándar sale del propio Simplex: al terminar, la base óptima $B$ define $y^{*\top}=c_B^\top B^{-1}$, y la condición de parada del algoritmo (todos los costos reducidos con el signo correcto) <b>es exactamente</b> la factibilidad dual $A^\top y^*\ge c$. Con eso, $b^\top y^* = c_B^\top B^{-1}b = c_B^\top x_B = c^\top x^*$.</p>
  <div class="tip"><b>El Simplex resuelve los dos problemas al mismo tiempo.</b> Mientras itera mantiene siempre la <b>factibilidad primal</b> y va buscando la factibilidad dual; cuando la consigue, para. Por eso el tableau óptimo contiene la solución de ambos: las variables básicas en la columna RHS, y los duales en la fila de costos reducidos bajo las holguras.</div>
  <h4>Las nueve combinaciones (y las cinco imposibles)</h4>
  <table>
    <tr><th></th><th>Dual con óptimo finito</th><th>Dual no acotado</th><th>Dual infactible</th></tr>
    <tr><th class="l">Primal con óptimo finito</th><td class="si">POSIBLE<br><span class="muted">el caso normal, $z^*=w^*$</span></td><td class="no">imposible</td><td class="no">imposible</td></tr>
    <tr><th class="l">Primal no acotado</th><td class="no">imposible</td><td class="no">imposible</td><td class="si">POSIBLE<br><span class="muted">Ejemplo 6(a)</span></td></tr>
    <tr><th class="l">Primal infactible</th><td class="no">imposible</td><td class="si">POSIBLE</td><td class="si">POSIBLE<br><span class="muted">Ejemplo 6(b)</span></td></tr>
  </table>
  <div class="key"><b>Cómo se lee esta tabla.</b> Solo hay <b>cuatro</b> escenarios posibles. Si el primal tiene óptimo finito, el dual también (dualidad fuerte). Si uno es no acotado, el otro es <b>necesariamente infactible</b> (corolarios C2 y C3). Y "los dos infactibles" es posible, aunque raro. <b>Lo que nunca puede pasar</b> es que ambos sean no acotados, o que uno sea no acotado y el otro tenga óptimo finito.</div>
  <div class="tip"><b>Pregunta de certamen.</b> "Un modelo resulta infactible. ¿Qué puede decir de su dual?" Respuesta correcta: <b>o es no acotado, o es infactible</b> — las dos cosas son posibles, y no se puede decidir cuál sin mirar el problema. Contestar "es no acotado" sin más es un error.</div>
</section>

<section id="t3">
  <h3>7. Holguras complementarias</h3>
  <p>La dualidad fuerte dice que los óptimos <b>coinciden</b>. Las holguras complementarias dicen <b>exactamente dónde se pierde el juego</b> en la cadena de desigualdades de la demostración: para que $c^\top x^*=b^\top y^*$, las dos desigualdades $(1)$ y $(2)$ tienen que ser <b>igualdades</b>. Eso obliga, término a término:</p>
  <div class="key">
  $$\boxed{\;y_i^*\,\underbrace{\big(b_i-a_i^\top x^*\big)}_{\text{holgura de la restricción }i}=0\quad\forall i\;}\qquad\qquad
    \boxed{\;x_j^*\,\underbrace{\big(a_j^\top y^*-c_j\big)}_{\text{holgura de la restricción dual }j}=0\quad\forall j\;}$$
  </div>
  <p>Como cada factor es $\ge0$, el producto solo puede anularse si <b>al menos uno</b> es cero. De ahí las cuatro lecturas:</p>
  <table>
    <tr><th class="l">Si en el óptimo...</th><th class="l">entonces...</th><th class="l">Traducción</th></tr>
    <tr><td class="l">la restricción $i$ tiene <b>holgura</b></td><td class="l">$y_i^*=0$</td><td class="l">un recurso que sobra no vale nada</td></tr>
    <tr><td class="l">$y_i^*&gt;0$</td><td class="l">la restricción $i$ es <b>activa</b></td><td class="l">solo los cuellos de botella tienen precio</td></tr>
    <tr><td class="l">$x_j^*&gt;0$ (se produce $j$)</td><td class="l">la restricción dual $j$ es <b>igualdad</b></td><td class="l">lo que se fabrica paga exacto lo que consume</td></tr>
    <tr><td class="l">la restricción dual $j$ es <b>estricta</b></td><td class="l">$x_j^*=0$</td><td class="l">lo que consume más de lo que aporta, no se fabrica</td></tr>
  </table>
  <div class="app"><b>Receta para recuperar un óptimo teniendo el otro.</b>
  <ol style="margin:6px 0">
    <li>Marque qué restricciones del problema conocido están <b>activas</b> y cuáles tienen holgura.</li>
    <li>Las holgadas anulan su variable complementaria.</li>
    <li>Las variables positivas convierten su restricción complementaria en <b>igualdad</b>.</li>
    <li>Con las igualdades del paso 3 arme un <b>sistema chico</b> (casi siempre $2\times2$ o $3\times3$) y resuélvalo.</li>
    <li><b>Verifique</b>: factibilidad, signos correctos, y $c^\top x^*=b^\top y^*$. Si el último chequeo falla, hay un error en los pasos anteriores.</li>
  </ol></div>
  <div class="tip"><b>El caso degenerado.</b> Puede ocurrir que una restricción esté activa <b>y</b> su dual sea $0$ (o que $x_j=0$ <b>y</b> su restricción dual sea igualdad). La holgura complementaria dice "el producto es cero", <b>no</b> "exactamente uno de los dos es cero". Por eso el paso 4 a veces deja un sistema indeterminado: es la señal de <b>degeneración</b> o de <b>óptimos alternativos</b>.</div>
</section>
"""

# ---------------------------------------------------------------- Bloque III
B3 = r"""
<h2 class="part" id="p3">Bloque III — Qué significa el dual</h2>

<section id="i1">
  <h3>8. El dual como el problema del comprador de recursos</h3>
  <p>Esta es la historia que le da sentido a todo. Volvamos al primal de producción:</p>
  <div class="grid2">
    <div>
      <b>Usted (el primal): el fabricante</b>
      <p>Tiene $b_i$ unidades de cada recurso y márgenes $c_j$ por producto. Decide <b>cuánto producir</b> de cada cosa para maximizar la utilidad.</p>
      $$\max\;c^\top x,\quad Ax\le b,\quad x\ge0$$
    </div>
    <div>
      <b>Él (el dual): el comprador</b>
      <p>Quiere <b>comprarle la fábrica entera</b>, recurso por recurso. Le ofrece un precio $y_i$ por unidad del recurso $i$ y quiere <b>gastar lo menos posible</b>.</p>
      $$\min\;b^\top y,\quad A^\top y\ge c,\quad y\ge0$$
    </div>
  </div>
  <div class="key"><b>¿Por qué la restricción $A^\top y\ge c$?</b> Porque usted no le vende si la oferta no es razonable. Para cualquier producto $j$, la canasta de recursos que ese producto consume ($a_{1j},\dots,a_{mj}$) tiene que valer, a los precios ofrecidos, <b>al menos</b> lo que usted ganaría fabricándolo:
  $$\sum_i a_{ij}\,y_i\;\ge\;c_j.$$
  Si algún producto violara esta condición, a usted le convendría <b>no vender</b> ese recurso y fabricar el producto. La oferta tiene que ser <i>a prueba de eso</i> para todos los productos a la vez.</div>
  <p>Y el teorema de dualidad fuerte dice algo notable: <b>el mínimo que él tiene que pagar es exactamente lo que usted ganaría produciendo</b>. El mercado no deja plata en la mesa por ninguno de los dos lados.</p>
  <div class="app"><b>Por eso los $y_i$ se llaman <i>precios sombra</i>.</b> No son precios de mercado, son los <b>precios internos</b> que la propia estructura del negocio le asigna a cada recurso. Un recurso que sobra vale $0$ en esta valorización, aunque haya costado caro comprarlo — porque una unidad más no le permite ganar ni un peso más.</div>
  <div class="tip"><b>Otros nombres de lo mismo.</b> Según el contexto: <i>precio sombra</i>, <i>valor marginal</i>, <i>variable dual</i>, <i>multiplicador de Lagrange/KKT</i>, <i>precio de escasez</i>. Todos son $y_i^*=\partial z^*/\partial b_i$.</div>
</section>

<section id="i2">
  <h3>9. Signos: cuándo un dual es negativo y qué significa</h3>
  <p>La tabla de la sección 3 no es una convención: <b>tiene contenido económico</b>.</p>
  <table>
    <tr><th class="l">Tipo de restricción en un <b>máximo</b></th><th>Signo</th><th class="l">Sentido</th></tr>
    <tr><td class="l"><b>$\le$ (un techo):</b> capacidad, disponibilidad, presupuesto</td><td>$y_i\ge0$</td><td class="l">Subir un techo <b>nunca empeora</b>. Es un <b>recurso</b>: $y_i$ mide cuánto <b>vale</b>.</td></tr>
    <tr><td class="l"><b>$\ge$ (un piso):</b> contrato mínimo, requerimiento de calidad, cuota obligatoria</td><td>$y_i\le0$</td><td class="l">Subir un piso <b>nunca mejora</b>. Es una <b>obligación</b>: $|y_i|$ mide cuánto <b>cuesta</b>.</td></tr>
    <tr><td class="l"><b>$=$ (un balance):</b> conservación de masa, inventario</td><td>libre</td><td class="l">Puede ser de cualquier signo: depende de si el balance aprieta hacia arriba o hacia abajo.</td></tr>
  </table>
  <div class="key"><b>Cuidado con reportar el signo.</b> Toda restricción $\ge$ se puede reescribir como $\le$ multiplicando por $-1$, y en esa forma su multiplicador es $\mu_i\ge0$, con $y_i=-\mu_i$. <b>Es el mismo número con distinto signo</b>, y hay que decir cuál se está reportando. Gurobi siempre entrega $\partial z^*/\partial b_i$ <b>sobre la restricción tal como usted la escribió</b>: si la escribió $\ge$ en un máximo, verá un <code>Pi</code> negativo.</div>
  <div class="app"><b>El dual negativo en lenguaje de negocio.</b> Si el precio sombra del contrato es $-20$, la frase correcta <b>no</b> es "el contrato vale $-20$". Es: <b>"cada tonelada adicional que me obliguen a entregar me cuesta 20 mil pesos de utilidad"</b>, y por lo tanto <b>"estoy dispuesto a pagar hasta 20 mil por tonelada para que me liberen del compromiso"</b>. Lo vemos con números en el Ejemplo 5.</div>
</section>
"""

# ---------------------------------------------------------------- Ejemplos
X1 = r"""
<h2 class="part" id="p4">Bloque IV — Ejemplos resueltos</h2>

<section id="x1">
  <span class="badge">Ejemplo 1 · el par completo, ambos en 2D</span>
  <h3>Ver el primal y el dual al mismo tiempo</h3>
  <p>Es el único caso en que se pueden <b>dibujar los dos</b>: un primal con 2 variables y 2 restricciones tiene un dual con 2 variables y 2 restricciones.</p>
  <div class="grid2">
    <div><b>PRIMAL</b>
    $$\max\;3x_1+5x_2$$
    $$x_1+x_2\le4$$
    $$x_1+3x_2\le6$$
    $$x_1,x_2\ge0$$</div>
    <div><b>DUAL</b>
    $$\min\;4y_1+6y_2$$
    $$y_1+y_2\ge3$$
    $$y_1+3y_2\ge5$$
    $$y_1,y_2\ge0$$</div>
  </div>
  """ + img("par") + r"""
  <h4>Los dos óptimos</h4>
  <p><b>Primal:</b> las dos restricciones se cruzan en $x_1+x_2=4$, $x_1+3x_2=6$ ⟹ $x^*=(3,1)$, $z^*=9+5=14$.<br>
  <b>Dual:</b> las dos restricciones se cruzan en $y_1+y_2=3$, $y_1+3y_2=5$ ⟹ $y^*=(2,1)$, $w^*=8+6=14$.</p>
  $$\boxed{\;z^*=w^*=14\;}$$
  <h4>Todo lo que este ejemplo muestra de una vez</h4>
  <table>
    <tr><th class="l">Propiedad</th><th class="l">Cómo se ve acá</th></tr>
    <tr><td class="l"><b>Dualidad fuerte</b></td><td class="l">$z^*=w^*=14$, aunque las regiones factibles no se parecen en nada (una es acotada, la otra no)</td></tr>
    <tr><td class="l"><b>Los duales del primal son la solución del dual</b></td><td class="l">Gurobi entrega $\pi=(2,1)$ en el primal, que es exactamente $y^*$</td></tr>
    <tr><td class="l"><b>Los duales del dual son la solución del primal</b></td><td class="l">Gurobi entrega $\pi=(3,1)$ en el dual, que es exactamente $x^*$</td></tr>
    <tr><td class="l"><b>Holgura complementaria</b></td><td class="l">$x_1,x_2&gt;0$ ⟹ las dos restricciones duales son igualdad ✓; $y_1,y_2&gt;0$ ⟹ las dos primales son activas ✓</td></tr>
    <tr><td class="l"><b>Dualidad débil</b></td><td class="l">$x=(2,1)$ da $z=11\le14$; $y=(3,1)$ da $w=18\ge14$ — la figura del sándwich de la sección 5</td></tr>
  </table>
  <div class="key"><b>Fíjese en las formas.</b> La región primal es un <b>polígono acotado</b> (hay techos por todos lados); la dual es una región <b>no acotada hacia arriba</b> (los pisos $\ge$ solo cortan por abajo, y siempre se puede pagar de más). Aun así ambos tienen óptimo finito: el dual porque minimiza y su región tiene un vértice "más barato".</div>
</section>
"""

X2 = r"""
<section id="x2">
  <span class="badge">Ejemplo 2 · el flujo completo · Ayudantía 6</span>
  <h3>Molino "Del Sur": construir, resolver y verificar</h3>
  <div class="app"><b>Enunciado.</b> El molino produce <b>harina integral</b> ($x_1$) y <b>harina blanca</b> ($x_2$), en quintales por semana, con márgenes de <b>4</b> y <b>3</b> millones de \$ por quintal. Dispone de 10 toneladas de trigo (la integral usa 2 t/quintal y la blanca 1), de 7 horas de molienda (1 h/quintal cada una), y tiene una <b>cuota comercial</b> que le impide vender más de 4 quintales de integral.</div>
  $$\max\; z=4x_1+3x_2 \qquad \text{s.a.}\quad
  \begin{cases}
  2x_1+x_2\le 10 & \text{(trigo)}\\
  x_1+x_2\le 7 & \text{(molienda)}\\
  x_1\le 4 & \text{(cuota integral)}\\
  x_1,x_2\ge 0
  \end{cases}$$

  <h4>Paso 1 — Resolver el primal</h4>
  """ + img("molino") + r"""
  <p>El óptimo está en el cruce de <b>trigo</b> y <b>molienda</b>: $2x_1+x_2=10$ y $x_1+x_2=7$ ⟹ $x_1=3$, $x_2=4$, y</p>
  $$\boxed{x^*=(3,\,4),\qquad z^*=12+12=24}$$
  <p>La cuota queda con <b>holgura</b>: $x_1=3&lt;4$, luego $s_3=1$.</p>

  <h4>Paso 2 — Construir el dual</h4>
  <p>Tres restricciones $\le$ en un máximo ⟹ tres variables $y_1,y_2,y_3\ge0$. Dos variables primales ⟹ dos restricciones duales de tipo $\ge$. Las columnas de $A$ son $a_{x_1}=(2,1,1)^\top$ y $a_{x_2}=(1,1,0)^\top$:</p>
  $$\min\; w=10y_1+7y_2+4y_3\qquad\text{s.a.}\quad
  \begin{cases}
  2y_1+y_2+y_3\ \ge\ 4 & (x_1)\\
  y_1+y_2\qquad\quad\ \ \ge\ 3 & (x_2)\\
  y_1,y_2,y_3\ge0
  \end{cases}$$
  <div class="tip"><b>Chequeo de dimensiones.</b> Primal $2$ variables / $3$ restricciones ⟹ dual $3$ variables / $2$ restricciones ✓. Y note que $y_3$ <b>no aparece</b> en la segunda restricción dual: correcto, porque la cuota no involucra a $x_2$ (su coeficiente es $0$).</div>

  <h4>Paso 3 — Resolver el dual con holgura complementaria (sin Simplex)</h4>
  <table>
    <tr><th class="l">Observación en el primal</th><th class="l">Consecuencia en el dual</th></tr>
    <tr><td class="l">la cuota tiene holgura ($s_3=1&gt;0$)</td><td class="l">$y_3=0$</td></tr>
    <tr><td class="l">$x_1=3&gt;0$</td><td class="l">$2y_1+y_2+y_3=4$ (igualdad)</td></tr>
    <tr><td class="l">$x_2=4&gt;0$</td><td class="l">$y_1+y_2=3$ (igualdad)</td></tr>
  </table>
  <p>Con $y_3=0$ queda el sistema $2y_1+y_2=4$, $y_1+y_2=3$. Restando: $y_1=1$, y entonces $y_2=2$.</p>
  $$\boxed{y^*=(1,\,2,\,0)}$$

  <h4>Paso 4 — Los cuatro chequeos</h4>
  <table>
    <tr><th class="l">Chequeo</th><th class="l">Cuenta</th><th>OK</th></tr>
    <tr><td class="l"><b>Dualidad fuerte</b></td><td class="l">$w^*=10(1)+7(2)+4(0)=10+14=24=z^*$</td><td>✓</td></tr>
    <tr><td class="l"><b>Factibilidad dual</b></td><td class="l">$2(1)+2+0=4\ge4$ ✓ ; $1+2=3\ge3$ ✓ ; $y\ge0$ ✓</td><td>✓</td></tr>
    <tr><td class="l"><b>H. compl. por restricción</b></td><td class="l">$y_1 s_1 = 1\cdot0$ ; $y_2 s_2 = 2\cdot0$ ; $y_3 s_3 = 0\cdot1$ — los tres nulos</td><td>✓</td></tr>
    <tr><td class="l"><b>H. compl. por variable</b></td><td class="l">las dos restricciones duales son igualdad, y $x_1,x_2&gt;0$</td><td>✓</td></tr>
  </table>

  <h4>Paso 5 — Interpretación</h4>
  <div class="app">
  <ul style="margin:6px 0">
    <li><b>$y_1=1$:</b> una tonelada más de trigo agrega 1 millón. Es lo máximo que conviene pagar por trigo adicional <i>por sobre</i> su costo actual.</li>
    <li><b>$y_2=2$:</b> una hora más de molienda agrega 2 millones — <b>el cuello de botella caro</b>. Si un turno extra de una hora cuesta menos de 2 millones, conviene.</li>
    <li><b>$y_3=0$:</b> la cuota comercial <b>no está apretando</b>. Negociar con el distribuidor para ampliarla no sirve de nada <i>hoy</i>; hay que revisarlo si cambian el trigo o la molienda.</li>
  </ul></div>
  <div class="key"><b>Verificación cruzada con Gurobi.</b> Al resolver el <b>dual</b> como problema independiente, sus precios sombra resultan $\pi=(3,\,4)$, que es exactamente $x^*$. Y el <b>costo reducido</b> de $y_3$ resulta $1$, que es exactamente la holgura $s_3$ de la cuota en el primal. La simetría es total: <b>las holguras de uno son los costos reducidos del otro</b>.</div>
</section>
"""

X3 = r"""
<section id="x3">
  <span class="badge">Ejemplo 3 · el drill mecánico</span>
  <h3>Dual de un problema con $\le$, $\ge$, $=$ y una variable libre</h3>
  <p>Este es el ejercicio que hay que poder hacer <b>sin pensar</b> en el certamen.</p>
  $$\max\; z=5x_1+4x_2-2x_3\qquad\text{s.a.}\quad
  \begin{cases}
  2x_1+x_2+x_3 \le 18 & \text{(R1)}\\
  x_1-x_2+2x_3 \ge 6 & \text{(R2)}\\
  x_1+x_2+x_3 = 12 & \text{(R3)}\\
  x_1\ge0,\;x_2\ge0,\;x_3\ \textbf{libre}
  \end{cases}$$

  <h4>Paso 1 — Las variables duales y sus signos</h4>
  <table>
    <tr><th class="l">Restricción primal</th><th>Tipo</th><th class="l">Variable dual</th><th>Signo</th></tr>
    <tr><td class="l">R1</td><td>$\le$</td><td class="l">$y_1$</td><td>$y_1\ge0$</td></tr>
    <tr><td class="l">R2</td><td>$\ge$</td><td class="l">$y_2$</td><td>$y_2\le0$</td></tr>
    <tr><td class="l">R3</td><td>$=$</td><td class="l">$y_3$</td><td><b>libre</b></td></tr>
  </table>

  <h4>Paso 2 — La objetivo dual</h4>
  $$\min\; w=18y_1+6y_2+12y_3$$

  <h4>Paso 3 — Una restricción dual por cada variable primal</h4>
  <p>El lado izquierdo de la restricción dual $j$ es la <b>columna $j$</b> de $A$ multiplicada por $y$:</p>
  <table>
    <tr><th class="l">Variable primal</th><th class="l">Su columna en $A$</th><th class="l">Restricción dual</th><th class="l">Tipo (por el signo de $x_j$)</th></tr>
    <tr><td class="l">$x_1\ge0$</td><td class="l">$(2,\,1,\,1)^\top$</td><td class="l">$2y_1+y_2+y_3$</td><td class="l">$\ge 5$</td></tr>
    <tr><td class="l">$x_2\ge0$</td><td class="l">$(1,\,-1,\,1)^\top$</td><td class="l">$y_1-y_2+y_3$</td><td class="l">$\ge 4$</td></tr>
    <tr><td class="l">$x_3$ <b>libre</b></td><td class="l">$(1,\,2,\,1)^\top$</td><td class="l">$y_1+2y_2+y_3$</td><td class="l"><b>$=-2$</b></td></tr>
  </table>

  <h4>El dual completo</h4>
  $$\boxed{\;\min\; w=18y_1+6y_2+12y_3\quad\text{s.a.}\quad
  \begin{cases}
  2y_1+y_2+y_3 \ge 5\\
  y_1-y_2+y_3 \ge 4\\
  y_1+2y_2+y_3 = -2\\
  y_1\ge0,\quad y_2\le0,\quad y_3 \text{ libre}
  \end{cases}\;}$$

  <h4>Verificación numérica</h4>
  <p>Resolviendo ambos por separado:</p>
  <table>
    <tr><th class="l">Primal</th><th class="l">Dual</th></tr>
    <tr><td class="l">$x^*=(6,\,4,\,2)$, &nbsp;$z^*=30+16-4=\mathbf{42}$</td><td class="l">$y^*=(5,\,-2,\,-3)$, &nbsp;$w^*=90-12-36=\mathbf{42}$</td></tr>
  </table>
  <p>Los signos salieron como la tabla predecía: $y_1=5\ge0$ ✓, $y_2=-2\le0$ ✓, $y_3=-3$ libre ✓. Y como las tres variables primales son distintas de cero, <b>las tres restricciones duales están activas</b>:</p>
  $$2(5)+(-2)+(-3)=5\;✓\qquad 5-(-2)+(-3)=4\;✓\qquad 5+2(-2)+(-3)=-2\;✓$$
  <div class="tip"><b>Los dos errores más frecuentes en este ejercicio.</b> (1) Escribir las <b>filas</b> de $A$ en las restricciones duales en vez de las <b>columnas</b> — por eso aparece la transpuesta. (2) Olvidar que la variable <b>libre</b> genera una restricción dual de <b>igualdad</b>, y que la restricción de <b>igualdad</b> genera una variable dual <b>libre</b>. Son dos reglas distintas que se confunden entre sí.</div>
</section>
"""

X4 = r"""
<section id="x4">
  <span class="badge">Ejemplo 4 · primal de mínimo · Clase 22</span>
  <h3>Problema de dieta: cuando el primal es el que minimiza</h3>
  <p>Es el <b>Ejercicio 18</b> que el profesor resolvió en clase por Simplex matricial y luego por el dual.</p>
  $$\min\;25x_1+20x_2\qquad\text{s.a.}\quad 4x_1+3x_2\ge250,\quad 3x_1+4x_2\ge270,\quad 2x_1+5x_2\ge300,\quad x\ge0$$

  <h4>El dual</h4>
  <p>Primal de <b>mínimo</b> con restricciones $\ge$ (del mismo sentido) ⟹ variables duales $\ge0$; variables primales $\ge0$ ⟹ restricciones duales $\le$:</p>
  $$\max\;250y_1+270y_2+300y_3\qquad\text{s.a.}\quad
  \begin{cases}
  4y_1+3y_2+2y_3\le25 & (x_1)\\
  3y_1+4y_2+5y_3\le20 & (x_2)\\
  y_1,y_2,y_3\ge0
  \end{cases}$$
  <div class="key">Note que el dual quedó con <b>3 variables y 2 restricciones</b>: es más fácil de resolver por Simplex que el primal (menos filas en el tableau), y además <b>ya viene con base factible inicial</b> ($y=0$ es factible porque todas las restricciones son $\le$ con lado derecho positivo). Por eso el profesor lo resolvió por ese lado en la Clase 22: <b>evita las variables artificiales</b>.</div>

  <h4>Las soluciones</h4>
  $$x^*=(25,\,50),\quad z^*=625+1000=1625 \qquad\qquad y^*=\left(\tfrac{85}{14},\;0,\;\tfrac{5}{14}\right),\quad w^*=1625$$
  <p>Chequeo de dualidad fuerte: $250\cdot\tfrac{85}{14}+300\cdot\tfrac{5}{14}=\tfrac{21250+1500}{14}=\tfrac{22750}{14}=1625$ ✓.</p>
  <p>Y de holgura complementaria: la segunda restricción primal da $3(25)+4(50)=275&gt;270$, tiene <b>excedente de 5</b>, y en efecto $y_2=0$ ✓. Las otras dos son activas ($4(25)+3(50)=250$, $2(25)+5(50)=300$) y sus duales son positivos ✓.</p>

  <h4>Interpretación en un problema de mínimo</h4>
  <div class="app">Aquí $y_i\ge0$ significa <b>costo</b>, no valor: subir el requerimiento nutricional 1 en una unidad <b>encarece</b> la dieta en $85/14\approx6{,}07$. Simétricamente, si se consigue <b>relajar</b> ese requerimiento, se <b>ahorran</b> 6,07 por unidad. El requerimiento 2 se cumple "de yapa": relajarlo no ahorra <b>nada</b>.</div>

  <h4>La observación matricial de la Clase 22</h4>
  <p>Al resolver ambos problemas por tableau y comparar las submatrices de las variables <b>fuera de la base</b>, el profesor mostró que</p>
  $$A_p=-A_d^\top,$$
  <p>es decir, <b>los dos tableaus óptimos son el mismo objeto transpuesto y con el signo cambiado</b>. Es la versión "en el tableau" de la simetría de la sección 4: no son dos cálculos, es uno solo mirado desde dos ángulos. En la práctica esto significa que <b>al terminar el Simplex de cualquiera de los dos, ya tiene la solución de ambos</b> — en la fila de costos reducidos y en la columna RHS.</p>
</section>
"""

X5 = r"""
<section id="x5">
  <span class="badge">Ejemplo 5 · restricción $\ge$ · dual negativo · Ayudantía 8</span>
  <h3>AquaNutrí Chiloé: cuánto cuesta un contrato</h3>
  <div class="app"><b>Enunciado.</b> Una planta de alimento para salmones produce dos formulaciones, <b>Engorda</b> ($x_1$) y <b>Smolt</b> ($x_2$), en toneladas al mes, con márgenes de <b>530</b> y <b>550</b> mil \$/t. La extrusora procesa hasta 1.100 t/mes; hay 150 t de harina de pescado (el Smolt usa 0,5 t/t) y 900 t de soya (Engorda 0,8, Smolt 0,5). Este mes la salmonera firmó un <b>contrato</b>: hay que entregar <b>al menos 900 t de Engorda</b>.</div>
  $$\max\; z=530x_1+550x_2\qquad\text{s.a.}\quad
  \begin{cases}
  x_1+x_2\le 1.100 & \text{(E) extrusora}\\
  0{,}5x_2\le 150 & \text{(H) harina}\\
  0{,}8x_1+0{,}5x_2\le 900 & \text{(S) soya}\\
  x_1\ \ge\ 900 & \text{(C) contrato}\\
  x_1,x_2\ge0
  \end{cases}$$

  <h4>Paso 1 — El primal, razonado</h4>
  <p>El contrato obliga $x_1\ge900$ y la extrusora impone $x_1+x_2\le1.100$, luego $x_2\le200$. Como ambos márgenes son positivos la extrusora se satura, $x_1=1.100-x_2$, y</p>
  $$z=530(1.100-x_2)+550x_2=583.000+\underbrace{20}_{550-530}\,x_2,$$
  <p>creciente en $x_2$: se lleva $x_2$ al máximo, $x_2=200$, y $x_1=900$.</p>
  $$\boxed{x^*=(900,\;200),\qquad z^*=\$587.000\text{ mil}}$$
  """ + img("aqua") + r"""
  <p>Activas: <b>extrusora</b> y <b>contrato</b>. Con holgura: harina ($x_2=200&lt;300$, sobran 50 t de capacidad de uso) y soya ($720+100=820\le900$, sobran 80 t).</p>

  <h4>Paso 2 — El dual, con los signos correctos</h4>
  <p>Tres restricciones $\le$ ⟹ $y_E,y_H,y_S\ge0$. Una restricción $\ge$ en un máximo ⟹ $\boxed{y_C\le0}$:</p>
  $$\min\;1.100\,y_E+150\,y_H+900\,y_S+900\,y_C\qquad\text{s.a.}\quad
  \begin{cases}
  y_E+0{,}8\,y_S+y_C\ \ge\ 530 & (x_1)\\
  y_E+0{,}5\,y_H+0{,}5\,y_S\ \ge\ 550 & (x_2)\\
  y_E,y_H,y_S\ge0,\quad y_C\le0
  \end{cases}$$

  <h4>Paso 3 — Resolver por holgura complementaria</h4>
  <p>Harina y soya tienen holgura ⟹ $y_H=y_S=0$. Ambas variables primales son positivas ⟹ las dos restricciones duales son igualdades:</p>
  $$\begin{cases} y_E+y_C=530\\ y_E=550\end{cases}\;\Longrightarrow\;\boxed{y_E=550,\qquad y_C=-20}$$
  <p>Chequeo: $1.100(550)+900(-20)=605.000-18.000=587.000=z^*$ ✓. Y el signo $y_C=-20\le0$ es el que la tabla predecía ✓.</p>

  <h4>Paso 4 — Interpretación</h4>
  <table>
    <tr><th class="l">Dual</th><th>Valor</th><th class="l">Lectura de negocio</th></tr>
    <tr><td class="l">$y_E$ extrusora</td><td><b>550</b></td><td class="l">una tonelada más de extrusora agrega 550 mil — el <b>cuello de botella</b></td></tr>
    <tr><td class="l">$y_H$ harina</td><td>0</td><td class="l">sobra: comprar más harina de pescado no sirve</td></tr>
    <tr><td class="l">$y_S$ soya</td><td>0</td><td class="l">sobra: idem</td></tr>
    <tr><td class="l">$y_C$ contrato</td><td><b>−20</b></td><td class="l">cada tonelada comprometida <b>cuesta</b> 20 mil de utilidad</td></tr>
  </table>
  <div class="tip"><b>¿Por qué exactamente $-20$?</b> Porque cada tonelada extra de contrato obliga a producir una tonelada más de Engorda, y como la extrusora está saturada, esa tonelada <b>desplaza</b> una de Smolt. La diferencia de márgenes es $530-550=-20$. El precio sombra no es un número mágico: es <b>el costo de oportunidad</b> del desplazamiento.</div>
  <div class="app"><b>La pregunta de negocio.</b> "La salmonera ofrece subir el contrato a 950 t a cambio de un pago único de \$800 mil. ¿Conviene?" Son 50 t adicionales, y el gráfico (b) muestra que el rango de validez aguanta hasta 1.100. Pérdida: $50\times20=\$1.000$ mil. Pago ofrecido: $\$800$ mil. <b>No conviene</b>: se pierden \$200 mil netos. El precio sombra responde la pregunta directamente <i>porque el cambio cae dentro del rango</i>.</div>
</section>
"""

X6 = r"""
<section id="x6">
  <span class="badge">Ejemplo 6 · las patologías</span>
  <h3>Cuando no hay óptimo: no acotado e infactible</h3>
  <p>La tabla de la sección 6 dice qué combinaciones son posibles. Acá están las dos que hay que saber reconocer.</p>

  <h4>(a) Primal no acotado ⟹ dual infactible</h4>
  $$\text{P: }\max\;x_1+x_2\quad\text{s.a.}\quad -x_1+x_2\le1,\;\;x_1-x_2\le1,\;\;x\ge0$$
  <p>La región factible es una <b>franja diagonal infinita</b>: cualquier punto de la forma $(t,t)$ es factible para todo $t\ge0$, y ahí $z=2t\to+\infty$. El primal es <b>no acotado</b>.</p>
  <p>Su dual es</p>
  $$\text{D: }\min\;y_1+y_2\quad\text{s.a.}\quad -y_1+y_2\ge1,\;\;y_1-y_2\ge1,\;\;y\ge0$$
  <p>La primera pide $y_2-y_1\ge1$ y la segunda $y_1-y_2\ge1$. Sumándolas: $0\ge2$, <b>absurdo</b>. El dual es <b>infactible</b>, tal como anticipaba el corolario C2.</p>
  """ + img("patol", "(a) La franja diagonal no está acotada en la dirección de crecimiento del objetivo. (b) Las dos condiciones duales piden zonas del plano que no se tocan.") + r"""
  <div class="key"><b>La suma de las dos restricciones duales <i>es</i> el certificado.</b> Que $0\ge2$ sea absurdo no es coincidencia: es la traducción algebraica de que el primal se escapa al infinito por la dirección $(1,1)$, que satisface ambas restricciones primales con lado izquierdo $\le0$ y mejora el objetivo. Esa dirección se llama <b>rayo de no acotamiento</b>, y es lo que Gurobi devuelve en <code>UnbdRay</code>.</div>

  <h4>(b) Los dos infactibles</h4>
  <p>Es el caso raro, pero existe y aparece en preguntas conceptuales:</p>
  $$\text{P: }\max\;2x_1-x_2\quad\text{s.a.}\quad x_1-x_2\le1,\;\;-x_1+x_2\le-2,\;\;x\ge0$$
  <p>La segunda restricción dice $x_1-x_2\ge2$ y la primera $x_1-x_2\le1$: <b>infactible</b>. Su dual es</p>
  $$\text{D: }\min\;y_1-2y_2\quad\text{s.a.}\quad y_1-y_2\ge2,\;\;-y_1+y_2\ge-1,\;\;y\ge0$$
  <p>La segunda dice $y_1-y_2\le1$ y la primera $y_1-y_2\ge2$: también <b>infactible</b>. Verificado con Gurobi: ambos devuelven <code>INFEASIBLE</code>.</p>
  <div class="tip"><b>Qué contestar.</b> "El primal es infactible, ¿y el dual?" — <b>no se puede saber sin mirar</b>: puede ser no acotado o infactible. Lo que <b>sí</b> se puede afirmar es que <b>no</b> tiene óptimo finito, porque eso obligaría al primal a tenerlo (dualidad fuerte).</div>
  <div class="app"><b>En la práctica.</b> Si Gurobi dice <code>INFEASIBLE</code> o <code>UNBOUNDED</code> en un modelo de negocio, casi siempre es un <b>error de modelamiento</b>, no una propiedad del negocio: un $\le$ escrito como $\ge$, una restricción de capacidad que faltó, un Big-M mal puesto o unidades mezcladas. Un modelo que representa una fábrica real <b>tiene</b> óptimo finito: la producción está acotada y no producir nada suele ser factible.</div>
</section>
"""

GUR = r"""
<h2 class="part" id="p5">Bloque V — Gurobi, trampas y práctica</h2>

<section id="gur">
  <h3>10. Todo esto en <code>gurobipy</code></h3>
  <p>El código útil no es "resolver el primal": es <b>armar los dos y verificar los teoremas</b>. Ese es exactamente el chequeo que hay que hacer en una tarea antes de entregar.</p>
<pre><code class="language-python">import gurobipy as gp
from gurobipy import GRB

# ---------- PRIMAL:  max 4x1+3x2 ;  2x1+x2<=10 ; x1+x2<=7 ; x1<=4 ----------
P = gp.Model("primal"); P.Params.OutputFlag = 0
x1 = P.addVar(name="integral"); x2 = P.addVar(name="blanca")
P.setObjective(4*x1 + 3*x2, GRB.MAXIMIZE)
P.addConstr(2*x1 + x2 &lt;= 10, name="trigo")
P.addConstr(  x1 + x2 &lt;=  7, name="molienda")
P.addConstr(  x1      &lt;=  4, name="cuota")
P.optimize()

# ---------- DUAL:  min 10y1+7y2+4y3 ; 2y1+y2+y3>=4 ; y1+y2>=3 ----------
D = gp.Model("dual"); D.Params.OutputFlag = 0
y = D.addVars(3, name=["y_trigo", "y_molienda", "y_cuota"])
D.setObjective(10*y[0] + 7*y[1] + 4*y[2], GRB.MINIMIZE)
D.addConstr(2*y[0] + y[1] + y[2] &gt;= 4, name="dual_x1")   # columna de x1 en A
D.addConstr(  y[0] + y[1]        &gt;= 3, name="dual_x2")   # columna de x2 en A
D.optimize()

print(f"z* (primal) = {P.ObjVal:.4f}")
print(f"w* (dual)   = {D.ObjVal:.4f}")
print(f"dualidad fuerte: {abs(P.ObjVal - D.ObjVal) &lt; 1e-9}\n")

print("los duales del PRIMAL deben ser la solucion del DUAL:")
print("   pi(P) =", [round(c.Pi, 4) for c in P.getConstrs()])
print("   y*    =", [round(v.X, 4) for v in D.getVars()])

print("\nlos duales del DUAL deben ser la solucion del PRIMAL:")
print("   pi(D) =", [round(c.Pi, 4) for c in D.getConstrs()])
print("   x*    =", [round(v.X, 4) for v in P.getVars()])

print("\nholgura complementaria (cada producto debe dar 0):")
for c, v in zip(P.getConstrs(), D.getVars()):
    print(f"   {c.ConstrName:&lt;10} holgura={c.Slack:7.4f} * dual={v.X:6.4f} = {c.Slack*v.X:.2e}")
</code></pre>
  <p>Salida:</p>
<pre><code>z* (primal) = 24.0000
w* (dual)   = 24.0000
dualidad fuerte: True

los duales del PRIMAL deben ser la solucion del DUAL:
   pi(P) = [1.0, 2.0, 0.0]
   y*    = [1.0, 2.0, 0.0]

los duales del DUAL deben ser la solucion del PRIMAL:
   pi(D) = [3.0, 4.0]
   x*    = [3.0, 4.0]

holgura complementaria (cada producto debe dar 0):
   trigo      holgura= 0.0000 * dual=1.0000 = 0.00e+00
   molienda   holgura= 0.0000 * dual=2.0000 = 0.00e+00
   cuota      holgura= 1.0000 * dual=0.0000 = 0.00e+00
</code></pre>

  <h4>Atributos relevantes</h4>
  <table>
    <tr><th class="l">Atributo</th><th class="l">Se pide a</th><th class="l">Qué entrega</th></tr>
    <tr><td class="l"><code>.Pi</code></td><td class="l">restricción</td><td class="l">la variable dual $y_i$ de esa restricción</td></tr>
    <tr><td class="l"><code>.Slack</code></td><td class="l">restricción</td><td class="l">holgura (en las $\ge$ sale <b>negativa</b>: es excedente)</td></tr>
    <tr><td class="l"><code>.RC</code></td><td class="l">variable</td><td class="l">costo reducido = holgura de <b>su</b> restricción dual</td></tr>
    <tr><td class="l"><code>.Status</code></td><td class="l">modelo</td><td class="l">2 = OPTIMAL, 3 = INFEASIBLE, 5 = UNBOUNDED</td></tr>
    <tr><td class="l"><code>lb=-GRB.INFINITY</code></td><td class="l">variable</td><td class="l">así se declara una variable <b>libre</b> (para los duales de igualdades)</td></tr>
    <tr><td class="l"><code>ub=0</code></td><td class="l">variable</td><td class="l">así se declara una variable $\le0$ (dual de una $\ge$ en un máximo)</td></tr>
  </table>
  <div class="tip"><b>Al armar el dual a mano en código, el error clásico es el mismo del papel:</b> escribir las <b>filas</b> de $A$ en vez de las <b>columnas</b>. Un chequeo barato: la restricción dual asociada a $x_j$ debe tener tantos términos como restricciones primales <b>en las que $x_j$ aparece con coeficiente no nulo</b>.</div>
</section>

<section id="trampas">
  <h3>11. Diez trampas clásicas</h3>
  <table>
    <tr><th>#</th><th class="l">Trampa</th><th class="l">Lo correcto</th></tr>
    <tr><td>1</td><td class="l">Usar las <b>filas</b> de $A$ en las restricciones duales</td><td class="l">Van las <b>columnas</b>: el dual usa $A^\top$</td></tr>
    <tr><td>2</td><td class="l">Poner todas las variables duales $\ge0$</td><td class="l">El signo lo da el <b>tipo</b> de la restricción primal (sección 3)</td></tr>
    <tr><td>3</td><td class="l">Confundir "variable libre" con "restricción de igualdad"</td><td class="l">Variable libre ⟹ restricción dual $=$. Restricción $=$ ⟹ variable dual libre. Son reglas distintas</td></tr>
    <tr><td>4</td><td class="l">Decir "el precio sombra del contrato es $-20$, o sea que no vale nada"</td><td class="l">Vale $20$ <b>en contra</b>: es una obligación que cuesta</td></tr>
    <tr><td>5</td><td class="l">Concluir de la holgura complementaria que "uno de los dos es exactamente cero"</td><td class="l">Dice que el <b>producto</b> es cero; ambos pueden serlo (degeneración)</td></tr>
    <tr><td>6</td><td class="l">"El primal es infactible ⟹ el dual es no acotado"</td><td class="l">Puede ser no acotado <b>o</b> infactible; no se decide sin mirar</td></tr>
    <tr><td>7</td><td class="l">Olvidar verificar $z^*=w^*$</td><td class="l">Es el chequeo más barato y el que atrapa casi todos los errores</td></tr>
    <tr><td>8</td><td class="l">Esperar $z^*=w^*$ en un modelo con <b>enteras</b></td><td class="l">En un MIP <b>sí hay brecha</b>. Hay que fijar las enteras para hablar de dualidad</td></tr>
    <tr><td>9</td><td class="l">Reportar los duales sin unidad</td><td class="l">Siempre \$/hora, \$/tonelada, \$/m³...</td></tr>
    <tr><td>10</td><td class="l">Dualizar sin chequear dimensiones</td><td class="l">$m$ restricciones ⟹ $m$ variables duales; $n$ variables ⟹ $n$ restricciones duales</td></tr>
  </table>
</section>

<section id="cheat">
  <h3>Cheat-sheet</h3>
  <div class="grid2">
    <div>
      <h4>El par canónico</h4>
      $$\max\{c^\top x:\;Ax\le b,\;x\ge0\}$$
      $$\min\{b^\top y:\;A^\top y\ge c,\;y\ge0\}$$
      <h4>Teoremas</h4>
      $$\text{débil: }\;c^\top x\le b^\top y\;\;\forall\text{ par factible}$$
      $$\text{fuerte: }\;c^\top x^*=b^\top y^*$$
      $$\text{h. compl.: }\;y_i^*s_i=0,\qquad x_j^*\,rc_j=0$$
      <h4>Simetría</h4>
      $$(\text{dual})^{\text{dual}}=\text{primal}$$
      $$\pi(\text{primal})=y^*,\qquad \pi(\text{dual})=x^*$$
      $$y^{*\top}=c_B^\top B^{-1}$$
    </div>
    <div>
      <h4>Signos (primal de máximo)</h4>
      <table style="font-size:.88rem">
        <tr><th>Restricción</th><th>Variable dual</th></tr>
        <tr><td>$\le$</td><td>$y_i\ge0$</td></tr>
        <tr><td>$\ge$</td><td>$y_i\le0$</td></tr>
        <tr><td>$=$</td><td>libre</td></tr>
        <tr><th>Variable</th><th>Restricción dual</th></tr>
        <tr><td>$x_j\ge0$</td><td>$\ge c_j$</td></tr>
        <tr><td>$x_j$ libre</td><td>$= c_j$</td></tr>
      </table>
      <h4>Casos posibles</h4>
      <table style="font-size:.86rem">
        <tr><th class="l">Primal</th><th class="l">Dual</th></tr>
        <tr><td class="l">óptimo finito</td><td class="l">óptimo finito, $z^*=w^*$</td></tr>
        <tr><td class="l">no acotado</td><td class="l">infactible</td></tr>
        <tr><td class="l">infactible</td><td class="l">no acotado <b>o</b> infactible</td></tr>
      </table>
    </div>
  </div>
  <h4>Los cinco chequeos antes de entregar</h4>
  <ol>
    <li><b>Dimensiones:</b> $m$ restricciones ⟹ $m$ variables duales, y viceversa.</li>
    <li><b>Signos:</b> cada $y_i$ con el signo que le corresponde por el tipo de su restricción.</li>
    <li><b>Dualidad fuerte:</b> $c^\top x^*=b^\top y^*$.</li>
    <li><b>Holgura complementaria:</b> todos los productos $y_i s_i$ y $x_j\,rc_j$ nulos.</li>
    <li><b>Factibilidad de ambos:</b> $x^*$ cumple el primal, $y^*$ cumple el dual (¡incluidos los signos!).</li>
  </ol>
</section>

<section id="prac">
  <h3>Ejercicios propuestos</h3>

  <h4>P1 — Construir el dual de un mixto (primal de mínimo)</h4>
  $$\min\;3x_1+2x_2+4x_3\qquad\text{s.a.}\quad
  \begin{cases}
  x_1+x_2\ \ge\ 4\\
  2x_1+x_3\ =\ 6\\
  x_2-x_3\ \le\ 2\\
  x_1\ge0,\;x_2\ \textbf{libre},\;x_3\ge0
  \end{cases}$$
  <p><b>a)</b> Escriba el dual con los signos correctos. <b>b)</b> Sabiendo que $x^*=(3,\,1,\,0)$ con $z^*=11$, encuentre $y^*$ por holgura complementaria. <b>c)</b> Verifique dualidad fuerte.</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Primal de <b>mínimo</b>: $\ge$ ⟹ $y_1\ge0$; $=$ ⟹ $y_2$ libre; $\le$ ⟹ $y_3\le0$. Variables: $x_1\ge0$ ⟹ restricción $\le3$; $x_2$ libre ⟹ restricción $=2$; $x_3\ge0$ ⟹ restricción $\le4$. Columnas de $A$: $x_1\to(1,2,0)$, $x_2\to(1,0,1)$, $x_3\to(0,1,-1)$.</p>
  $$\max\;4y_1+6y_2+2y_3\quad\text{s.a.}\quad
  \begin{cases}
  y_1+2y_2\ \le\ 3\\
  y_1\qquad\ +y_3\ =\ 2\\
  y_2-y_3\ \le\ 4\\
  y_1\ge0,\;y_2\text{ libre},\;y_3\le0
  \end{cases}$$
  <p><b>b)</b> R1: $3+1=4$, <b>activa</b>. R2: $6+0=6$, igualdad (siempre activa). R3: $1-0=1&lt;2$, <b>holgura de 1</b> ⟹ $y_3=0$. Variables: $x_1=3&gt;0$ ⟹ primera restricción dual activa: $y_1+2y_2=3$. $x_2=1\ne0$ ⟹ segunda activa (ya lo era por ser igualdad): $y_1+y_3=2$ ⟹ con $y_3=0$, $\boxed{y_1=2}$ y entonces $2+2y_2=3$ ⟹ $\boxed{y_2=0{,}5}$. Resultado: $y^*=(2;\;0{,}5;\;0)$.</p>
  <p><b>c)</b> $w^*=4(2)+6(0{,}5)+2(0)=8+3=11=z^*$ ✓. Y $x_3=0$ es consistente con que su restricción dual quede estricta: $0{,}5-0=0{,}5&lt;4$ ✓.</p>
  </details>

  <h4>P2 — Otto Kraus: dual y holgura complementaria</h4>
  $$\max\;3x_1+2x_2+5x_3\qquad\text{s.a.}\quad x_1+2x_2+x_3\le430,\;\;3x_1+2x_3\le460,\;\;x_1+4x_2\le420$$
  <p>El óptimo primal es $x^*=(0,\,100,\,230)$ con $z^*=1350$. <b>a)</b> Plantee el dual. <b>b)</b> Resuélvalo por holgura complementaria. <b>c)</b> ¿Qué dice el hecho de que $x_1^*=0$ sobre la primera restricción dual?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> $$\min\;430y_1+460y_2+420y_3\quad\text{s.a.}\quad y_1+3y_2+y_3\ge3,\;\;2y_1+4y_3\ge2,\;\;y_1+2y_2\ge5,\;\;y\ge0$$</p>
  <p><b>b)</b> Máquina 3: $0+400=400&lt;420$, <b>holgura 20</b> ⟹ $y_3=0$. $x_2&gt;0$ ⟹ $2y_1+4y_3=2$ ⟹ $y_1=1$. $x_3&gt;0$ ⟹ $y_1+2y_2=5$ ⟹ $y_2=2$. Luego $\boxed{y^*=(1,\,2,\,0)}$ y $w^*=430+920+0=1350=z^*$ ✓.</p>
  <p><b>c)</b> Que <b>puede</b> estar estricta, y lo está: $1+3(2)+0=7&gt;3$. La holgura es $7-3=4$, que es el <b>costo reducido</b> del tren (con signo): el tren consume 7 en recursos valorizados y solo aporta 3. Por eso no se fabrica.</p>
  </details>

  <h4>P3 — Certificado por dualidad débil</h4>
  <p>Para el primal $\max\,3x_1+5x_2$ con $x_1+x_2\le4$, $x_1+3x_2\le6$, $x\ge0$, un compañero afirma haber encontrado la solución $x=(1;\,1{,}5)$ con $z=10{,}5$, y sostiene que es óptima.</p>
  <p><b>a)</b> Verifique que $y=(2{,}5;\,0{,}5)$ es factible para el dual y calcule $w$. <b>b)</b> ¿Qué puede concluir sobre la afirmación? <b>c)</b> ¿Qué tendría que pasar para que un par $(x,y)$ demuestre optimalidad?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Dual: $\min\,4y_1+6y_2$ s.a. $y_1+y_2\ge3$, $y_1+3y_2\ge5$. Con $y=(2{,}5;\,0{,}5)$: $2{,}5+0{,}5=3\ge3$ ✓ y $2{,}5+1{,}5=4&lt;5$ ✗. <b>No es factible</b>, así que no sirve como cota. Con $y=(2,1)$ sí: $3\ge3$ ✓, $5\ge5$ ✓, y $w=8+6=14$.</p>
  <p><b>b)</b> $x=(1;\,1{,}5)$ es factible ($2{,}5\le4$, $5{,}5\le6$) y da $z=10{,}5$. Por dualidad débil $z^*\le14$, pero eso <b>no</b> confirma que $10{,}5$ sea óptimo: solo dice que el óptimo está entre $10{,}5$ y $14$. De hecho $z^*=14$, así que la afirmación es <b>falsa</b>.</p>
  <p><b>c)</b> Que <b>coincidan</b>: si $x$ es primal-factible, $y$ es dual-factible y $c^\top x=b^\top y$, entonces <b>ambos son óptimos</b> (corolario C1). Ese par es un certificado que no requiere ejecutar el Simplex.</p>
  </details>

  <h4>P4 — El dual del dual</h4>
  <p>Tome el dual del Ejemplo 2 (Molino) como si fuera un primal: $\min\,10y_1+7y_2+4y_3$ s.a. $2y_1+y_2+y_3\ge4$, $y_1+y_2\ge3$, $y\ge0$.</p>
  <p><b>a)</b> Constrúyale <i>su</i> dual. <b>b)</b> ¿Qué obtuvo? <b>c)</b> ¿Cuál de los dos conviene resolver por Simplex y por qué?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Primal de mínimo con $\ge$ ⟹ variables duales $\ge0$; hay 2 restricciones ⟹ 2 variables, llamémoslas $x_1,x_2$. Las 3 variables $y_i\ge0$ ⟹ 3 restricciones $\le$. Las columnas son $y_1\to(2,1)$, $y_2\to(1,1)$, $y_3\to(1,0)$:</p>
  $$\max\;4x_1+3x_2\quad\text{s.a.}\quad 2x_1+x_2\le10,\;\;x_1+x_2\le7,\;\;x_1\le4,\;\;x\ge0$$
  <p><b>b)</b> Exactamente el <b>primal original</b> del Molino. El dual del dual es el primal.</p>
  <p><b>c)</b> El primal tiene 3 restricciones y 2 variables; el dual, 2 restricciones y 3 variables. El esfuerzo del Simplex crece sobre todo con el <b>número de restricciones</b> (el tamaño de la base y de $B^{-1}$), así que conviene resolver el <b>dual</b>: tableau de 2 filas en vez de 3. Con la solución dual se recupera la primal por holgura complementaria.</p>
  </details>

  <h4>P5 — Diagnóstico</h4>
  <p>Para cada situación, diga qué se puede afirmar del otro problema, y justifique con el teorema correspondiente.</p>
  <p><b>a)</b> El primal tiene óptimo $z^*=500$. <b>b)</b> El dual resulta no acotado. <b>c)</b> El primal es infactible. <b>d)</b> Alguien reporta que el primal tiene óptimo $z^*=500$ y el dual óptimo $w^*=480$.</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> El dual tiene óptimo finito y $w^*=500$ (dualidad fuerte).</p>
  <p><b>b)</b> El primal es <b>infactible</b> (corolario C3): si existiera un $x$ factible, su valor $c^\top x$ sería una cota inferior finita para el dual y este no podría irse a $-\infty$.</p>
  <p><b>c)</b> El dual es <b>no acotado o infactible</b>. No se puede decidir sin mirar el problema. Lo que sí se afirma: el dual <b>no</b> tiene óptimo finito.</p>
  <p><b>d)</b> <b>Imposible</b> en programación lineal: la dualidad fuerte prohíbe la brecha. Además $w^*=480&lt;500=z^*$ viola incluso la dualidad <b>débil</b>, que exige $z\le w$. Hay un error de cálculo, o el modelo tiene variables <b>enteras</b> —y entonces "el dual" es el de la relajación lineal, no el del MIP.</p>
  </details>
</section>

<footer>
  <b>IIP314W-2 · Optimización Aplicada a Negocios · 2026-T2</b><br>
  Universidad del Desarrollo · Profesor Rodrigo Trigo Vilches · Ayudante Vicente Ramírez<br>
  Recurso de estudio — Primal y Dual
</footer>
</body>
</html>
"""

HTML = HEAD + B1 + B2 + B3 + X1 + X2 + X3 + X4 + X5 + X6 + GUR

OUT = r"C:\Users\raalv\__Ayudantía Opti Inf\2026-T2\Recursos\Recurso_Dual_Primal.html"
HTML, _informe = postproceso(HTML)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("escrito:", OUT, len(HTML) // 1024, "KB")
