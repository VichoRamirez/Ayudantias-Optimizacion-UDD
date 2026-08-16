# -*- coding: utf-8 -*-
"""Genera el Recurso HTML de Precios Sombra y Analisis de Sensibilidad (IIP314W, 2026-T2)."""
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

# =====================================================================
# Instancia CONSERVAS:  max 30x1+40x2 ; x1+2x2<=b1 ; 5x1+3x2<=180 ; x1+x2<=45
# =====================================================================
def conservas(b1=80.0, c1=30.0, c2=40.0, b2=180.0, b3=45.0):
    r = linprog(c=[-c1, -c2], A_ub=[[1, 2], [5, 3], [1, 1]], b_ub=[b1, b2, b3],
                bounds=[(0, None), (0, None)], method="highs")
    return (-r.fun, r.x) if r.success else (np.nan, None)


# ---------- Figura 1: region factible ----------
def fig_region():
    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    x = np.linspace(0, 60, 400)
    r1 = (80 - x) / 2
    r2 = (180 - 5 * x) / 3
    r3 = 45 - x
    y = np.linspace(0, 60, 400)
    X, Y = np.meshgrid(np.linspace(0, 60, 500), np.linspace(0, 60, 500))
    feas = (X + 2 * Y <= 80) & (5 * X + 3 * Y <= 180) & (X + Y <= 45) & (X >= 0) & (Y >= 0)
    ax.contourf(X, Y, feas.astype(float), levels=[.5, 1.5], colors=["#cfe3f2"], alpha=.85)
    ax.plot(x, r1, color=AZUL, lw=2, label=r"R1 clasificación: $x_1+2x_2\leq 80$")
    ax.plot(x, r2, color=ACC, lw=2, label=r"R2 despalillado: $5x_1+3x_2\leq 180$")
    ax.plot(x, r3, color=VERDE, lw=2, label=r"R3 bodega: $x_1+x_2\leq 45$")
    for z, st in [(900, ":"), (1300, ":"), (1700, "-")]:
        ax.plot(x, (z - 30 * x) / 40, color="#555", ls=st, lw=1.6 if z == 1700 else 1,
                label=(r"isobeneficio $z=1700$" if z == 1700 else None))
    ax.plot(10, 35, "o", color="#111", ms=9, zorder=5)
    ax.annotate(r"$x^*=(10,\,35)$" "\n" r"$z^*=1700$", (10, 35), textcoords="offset points",
                xytext=(18, 14), fontsize=11, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.9, boxstyle="round,pad=.3"))
    ax.annotate("R2 no toca el óptimo:\nle sobran 25 h", xy=(21.5, 24.2), xytext=(11, 11),
                fontsize=9.5, color=ACC, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ACC, lw=1.4))
    ax.set_xlim(0, 50); ax.set_ylim(0, 50)
    ax.set_xlabel(r"$x_1$ — toneladas de durazno"); ax.set_ylabel(r"$x_2$ — toneladas de cereza")
    ax.set_title("Conservas: región factible y óptimo", color=AZUL, fontweight="bold")
    ax.legend(loc="upper right", fontsize=9)
    return b64(fig)


IMG["region"] = fig_region()

# ---------- Figura 2: sensibilidad de b1 ----------
def fig_b1():
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.9))
    ax = axs[0]
    x = np.linspace(0, 60, 400)
    X, Y = np.meshgrid(np.linspace(0, 60, 500), np.linspace(0, 60, 500))
    feas = (X + 2 * Y <= 90) & (5 * X + 3 * Y <= 180) & (X + Y <= 45)
    ax.contourf(X, Y, feas.astype(float), levels=[.5, 1.5], colors=["#e7f0f7"])
    feas0 = (X + 2 * Y <= 80) & (5 * X + 3 * Y <= 180) & (X + Y <= 45)
    ax.contourf(X, Y, feas0.astype(float), levels=[.5, 1.5], colors=["#cfe3f2"])
    for b1v, st, lab in [(67.5, "--", r"$b_1=67{,}5$ (mín)"), (80, "-", r"$b_1=80$ (actual)"),
                         (90, "--", r"$b_1=90$ (máx)")]:
        ax.plot(x, (b1v - x) / 2, color=AZUL, ls=st, lw=2 if b1v == 80 else 1.4, label=lab)
    ax.plot(x, (180 - 5 * x) / 3, color=ACC, lw=1.8, label="R2 despalillado")
    ax.plot(x, 45 - x, color=VERDE, lw=1.8, label="R3 bodega")
    bs = np.linspace(67.5, 90, 60)
    ax.plot(90 - bs, bs - 45, color="#111", lw=3, alpha=.8)
    for bv, mk in [(67.5, "s"), (80, "o"), (90, "^")]:
        ax.plot(90 - bv, bv - 45, mk, color="#111", ms=8, zorder=5)
    ax.annotate("el óptimo se desliza\nsobre la bodega (R3)", (14, 26), fontsize=9.5,
                color="#111", fontweight="bold")
    ax.set_xlim(0, 40); ax.set_ylim(0, 50)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(a) Al mover $b_1$ el vértice se desliza", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.5, loc="upper right")

    ax = axs[1]
    bb = np.linspace(20, 110, 900)
    zz = np.array([conservas(b1=b)[0] for b in bb])
    ax.plot(bb, zz, color=AZUL, lw=2.4)
    ax.axvspan(67.5, 90, color="#cfe3f2", alpha=.75, label="rango de validez [67,5 ; 90]")
    ax.plot(bb, 900 + 10 * bb, color=ACC, ls="--", lw=1.5,
            label=r"recta de pendiente $\pi_1=10$")
    ax.plot(80, 1700, "o", color="#111", ms=8, zorder=5)
    ax.annotate(r"$b_1=80,\ z^*=1700$", (80, 1700), textcoords="offset points", xytext=(-120, 20),
                fontsize=10, fontweight="bold")
    for bv, txt in [(36, r"$\pi_1=110/7$"), (67.5, r"$\pi_1=10$"), (90, r"$\pi_1=0$")]:
        ax.axvline(bv, color=GRIS, ls=":", lw=1)
    ax.text(48, 1180, r"$\pi_1=\frac{110}{7}\approx15{,}7$", color=GRIS, fontsize=9.5)
    ax.text(72, 1420, r"$\pi_1=10$", color=ACC, fontsize=10, fontweight="bold")
    ax.text(95, 1740, r"$\pi_1=0$", color=GRIS, fontsize=9.5)
    ax.set_ylim(600, 2000)
    ax.set_xlabel(r"$b_1$ — horas de clasificación"); ax.set_ylabel(r"$z^*(b_1)$")
    ax.set_title(r"(b) $z^*(b_1)$ es cóncava y lineal a trozos", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")
    fig.tight_layout()
    return b64(fig)


IMG["b1"] = fig_b1()

# ---------- Figura 3: sensibilidad de c1 ----------
def fig_c1():
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.9))
    ax = axs[0]
    x = np.linspace(0, 60, 400)
    X, Y = np.meshgrid(np.linspace(0, 60, 500), np.linspace(0, 60, 500))
    feas = (X + 2 * Y <= 80) & (5 * X + 3 * Y <= 180) & (X + Y <= 45)
    ax.contourf(X, Y, feas.astype(float), levels=[.5, 1.5], colors=["#cfe3f2"], alpha=.9)
    ax.plot(x, (80 - x) / 2, color=AZUL, lw=2.4, label="R1 clasificación")
    ax.plot(x, (180 - 5 * x) / 3, color=ACC, lw=2.4, label="R2 despalillado")
    ax.plot(x, 45 - x, color=VERDE, lw=2.4, label="R3 bodega")
    etiq = {20: r"isobeneficio $c_1=20$  ($\parallel$ R1: empate)",
            30: r"isobeneficio $c_1=30$  (actual)",
            40: r"isobeneficio $c_1=40$  ($\parallel$ R3: empate)"}
    for cv, st in [(20, (0, (1, 2))), (30, "-"), (40, (0, (1, 2)))]:
        z = cv * 10 + 40 * 35
        ax.plot(x, (z - cv * x) / 40, color="#000", ls=st, lw=2.2 if cv == 30 else 1.8,
                label=etiq[cv], zorder=6)
    ax.plot(10, 35, "o", color="#111", ms=9, zorder=7)
    ax.annotate("el vértice (10, 35)\nno se mueve", (10, 35), textcoords="offset points",
                xytext=(-14, -52), fontsize=9.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.set_xlim(0, 45); ax.set_ylim(0, 50)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(a) Al mover $c_1$ la isobeneficio rota", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.2, loc="upper right", framealpha=.95)

    ax = axs[1]
    cc = np.linspace(5, 70, 800)
    zz = np.array([conservas(c1=c)[0] for c in cc])
    ax.plot(cc, zz, color=AZUL, lw=2.4)
    ax.axvspan(20, 40, color="#cfe3f2", alpha=.75, label="rango de validez [20 ; 40]")
    ax.plot(cc, 10 * cc + 1400, color=ACC, ls="--", lw=1.5,
            label=r"recta de pendiente $x_1^*=10$")
    ax.plot(30, 1700, "o", color="#111", ms=8, zorder=5)
    ax.set_ylim(1300, 2700)
    ax.set_xlabel(r"$c_1$ — beneficio por tonelada de durazno"); ax.set_ylabel(r"$z^*(c_1)$")
    ax.set_title(r"(b) $z^*(c_1)$ es convexa y lineal a trozos", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    return b64(fig)


IMG["c1"] = fig_c1()

# ---------- Figura 4: degeneracion ----------
def fig_degen():
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.6))
    ax = axs[0]
    X, Y = np.meshgrid(np.linspace(0, 10, 500), np.linspace(0, 10, 500))
    feas = (X <= 4) & (Y <= 4) & (X + Y <= 8)
    ax.contourf(X, Y, feas.astype(float), levels=[.5, 1.5], colors=["#cfe3f2"])
    ax.axvline(4, color=AZUL, lw=2, label=r"$x_1\leq 4$")
    ax.axhline(4, color=ACC, lw=2, label=r"$x_2\leq 4$")
    xx = np.linspace(0, 10, 100)
    ax.plot(xx, 8 - xx, color=VERDE, lw=2, label=r"$x_1+x_2\leq 8$")
    ax.plot(4, 4, "o", color="#111", ms=10, zorder=5)
    ax.annotate("3 restricciones activas\nen un vértice de 2 variables\n→ vértice DEGENERADO",
                (4, 4), textcoords="offset points", xytext=(-140, -70), fontsize=9.5,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.set_xlim(0, 8); ax.set_ylim(0, 8)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(a) $\max\,x_1+x_2$ con un vértice degenerado", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")

    ax = axs[1]
    bb = np.linspace(0, 8, 400)
    zz = np.minimum(np.minimum(bb + 4, 8), bb + 4)
    zz = np.array([min(b + 4, 8) for b in bb])
    ax.plot(bb, zz, color=AZUL, lw=2.6)
    ax.plot(4, 8, "o", color="#111", ms=9, zorder=5)
    ax.plot([2, 4], [6, 8], color=ACC, lw=2.4, ls="--")
    ax.plot([4, 6], [8, 8], color=VERDE, lw=2.4, ls="--")
    ax.text(1.1, 6.6, r"por la izquierda: $\pi_1=1$", color=ACC, fontsize=10, fontweight="bold")
    ax.text(4.4, 8.25, r"por la derecha: $\pi_1=0$", color=VERDE, fontsize=10, fontweight="bold")
    ax.set_xlim(0, 8); ax.set_ylim(3, 9)
    ax.set_xlabel(r"$b_1$ (lado derecho de $x_1\leq b_1$)"); ax.set_ylabel(r"$z^*(b_1)$")
    ax.set_title(r"(b) El precio sombra no está definido: hay dos", color=AZUL, fontweight="bold")
    fig.tight_layout()
    return b64(fig)


IMG["degen"] = fig_degen()

# ---------- Figura 5: MIP ----------
def fig_mip():
    """max 8x1+6x2-20y ; x1+x2 <= 10+15y ; 2x1+x2 <= b ; y in {0,1}."""
    def z_fija(b, y):
        r = linprog(c=[-8, -6], A_ub=[[1, 1], [2, 1]], b_ub=[10 + 15 * y, b],
                    bounds=[(0, None), (0, None)], method="highs")
        return -r.fun - 20 * y if r.success else -np.inf

    bb = np.linspace(0, 55, 1200)
    z0 = np.array([z_fija(b, 0) for b in bb])
    z1 = np.array([z_fija(b, 1) for b in bb])
    zm = np.maximum(z0, z1)
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    ax.plot(bb, zm, color=AZUL, lw=5, alpha=.35, solid_capstyle="round",
            label=r"MIP: $z^*(b)=\max$ de las dos")
    ax.plot(bb, z0, color=GRIS, ls="--", lw=2, label=r"LP con $y=0$ (cóncava)")
    ax.plot(bb, z1, color=VERDE, ls="-.", lw=2, label=r"LP con $y=1$ (cóncava)")
    # punto de trabajo b=12 (ahi y*=0) y su extrapolacion con el precio sombra del LP y=0
    ax.plot(12, 64, "o", color="#111", ms=9, zorder=6)
    ax.annotate(r"hoy: $b=12$, $y^*=0$, $z^*=64$", (12, 64), textcoords="offset points",
                xytext=(-78, -48), fontsize=9.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#111"))
    bx = np.linspace(12, 26, 50)
    ax.plot(bx, 64 + 2 * (bx - 12), color=ACC, ls=":", lw=2,
            label=r"extrapolación con $\pi=2$ del LP $y=0$")
    ax.plot([20, 20], [80, 100], color=ACC, lw=2.4)
    ax.plot(20, 100, "^", color=ACC, ms=9, zorder=6)
    ax.annotate("en $b=15$ el MIP cambia a $y^*=1$:\nla pendiente SUBE de 2 a 6\n"
                "y la extrapolación queda CORTA",
                xy=(15, 70), xytext=(26.5, 18), fontsize=9.5, color=ACC, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ACC, lw=1.6))
    ax.annotate("en $b=20$:\nreal 100, predicho 80", xy=(20, 90), xytext=(28, 92),
                fontsize=9.2, color=ACC, arrowprops=dict(arrowstyle="->", color=ACC))
    ax.set_ylim(-30, 185)
    ax.set_xlabel(r"$b$ — lado derecho del recurso escaso"); ax.set_ylabel(r"$z^*(b)$")
    ax.set_title(r"En un MIP $z^*(b)$ es un máximo de cóncavas: NO es cóncava",
                 color=AZUL, fontweight="bold", fontsize=11.5)
    ax.legend(fontsize=9, loc="upper left")
    return b64(fig)


IMG["mip"] = fig_mip()

print("figuras listas:", {k: len(v) // 1024 for k, v in IMG.items()}, "KB")

# =====================================================================
#                               HTML
# =====================================================================
HEAD = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Recurso de estudio — Precios sombra y análisis de sensibilidad | IIP314W UDD</title>
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
    <h1>Recurso de estudio — Precios sombra y análisis de sensibilidad</h1>
    <div class="sub">Dualidad aplicada: valor marginal de un recurso, costos reducidos, rangos de validez y qué hacer cuando hay enteras</div>
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
    <li><a href="#f1">1. Qué es un precio sombra</a></li>
    <li><a href="#f2">2. El dual y las reglas de signo</a></li>
    <li><a href="#f3">3. Holgura complementaria</a></li>
    <li><a href="#f4">4. Costo reducido</a></li>
    <li><a href="#f5">5. Leerlos en el tableau</a></li>
    <li><a href="#r1">6. Rango de validez de $b_i$</a></li>
    <li><a href="#r2">7. Rango de validez de $c_j$</a></li>
    <li><a href="#r3">8. Regla del 100 %</a></li>
    <li><a href="#e1">Ej. 1 — Conservas (completo)</a></li>
    <li><a href="#e2">Ej. 2 — Gas envasado</a></li>
    <li><a href="#e3">Ej. 3 — Juguetes: costo reducido</a></li>
    <li><a href="#e4">Ej. 4 — Taller: precio sombra negativo</a></li>
    <li><a href="#e5">Ej. 5 — Dieta: leer el tableau</a></li>
    <li><a href="#e6">Ej. 6 — MIP: fijar la binaria</a></li>
    <li><a href="#gur">9. Todo esto en Gurobi</a></li>
    <li><a href="#trampas">10. Diez trampas clásicas</a></li>
    <li><a href="#cheat">Resumen / cheat-sheet</a></li>
    <li><a href="#prac">Ejercicios propuestos</a></li>
  </ol>
</nav>

<section id="intro">
  <h3>Cómo usar este recurso</h3>
  <p>Este documento cubre la última unidad del curso: <b>dualidad aplicada</b>. Después de resolver un modelo, la pregunta de negocio casi nunca es "¿cuánto produzco?" sino <b>"¿qué me conviene cambiar?"</b>: comprar más horas-máquina, arrendar otra bodega, subir un precio, aceptar un contrato. El <b>análisis de sensibilidad</b> responde esas preguntas <i>sin volver a resolver el modelo</i>, y el <b>precio sombra</b> es la pieza central.</p>
  <p>Está organizado en cuatro bloques: <b>fundamentos</b> (secciones 1–5), <b>rangos de validez</b> (6–8), <b>seis ejemplos resueltos</b> con desarrollo a mano y gráfico, y <b>Gurobi + trampas</b> (9–10). Cierra con un cheat-sheet y ejercicios propuestos con solución plegable.</p>
  <div class="key"><b>Convención de todo el documento.</b> Trabajamos con el primal en forma canónica de maximización, $\max\{c^\top x : Ax\le b,\ x\ge0\}$, y su dual $\min\{b^\top y : A^\top y\ge c,\ y\ge0\}$. Escribimos $\pi_i$ (o $y_i^*$) para el precio sombra de la restricción $i$ y $s_i$ para su holgura. Todos los números del documento fueron verificados con <code>gurobipy</code>.</div>
  <div class="tip"><b>Prerrequisito.</b> Conviene tener fresco el <b>Simplex en tableau</b> y la construcción del dual (Ayudantía 6 y Clases 22–24). Todo lo que sigue vive en el <i>tableau óptimo</i>: el precio sombra ya está ahí, solo hay que saber dónde mirar.</div>
</section>
"""

# ---------------------------------------------------------------- Parte 1
P1 = r"""
<h2 class="part" id="p1">Bloque I — Fundamentos</h2>

<section id="f1">
  <h3>1. Qué es un precio sombra</h3>
  <p>Sea $z^*(b)$ el valor óptimo del problema como <b>función del vector de recursos</b> $b$. El <b>precio sombra</b> (o <i>valor marginal</i>, o <i>dual</i>) de la restricción $i$ es</p>
  $$\boxed{\;\pi_i \;=\; \frac{\partial z^*}{\partial b_i}\;}$$
  <p>es decir, <b>en cuánto mejora el óptimo si se dispone de una unidad más del recurso $i$</b>, manteniendo todo lo demás igual.</p>
  <div class="app"><b>Lectura de negocio.</b> $\pi_i$ es el <b>máximo que conviene pagar por una unidad adicional</b> del recurso $i$, <i>por sobre</i> el costo que ya está incorporado en el modelo. Si una hora extra de máquina vale $\pi=10$ mil y el turno extra cuesta $7$ mil, conviene: gano $3$ mil netos. Si cuesta $12$ mil, no.</div>
  <h4>Tres propiedades que hay que tener claras</h4>
  <ul>
    <li><b>Es marginal, no total.</b> $\pi_i$ mide el efecto de <i>la siguiente</i> unidad, no de las 100 siguientes. Por eso existe el <b>rango de validez</b> (sección 6).</li>
    <li><b>Tiene unidades.</b> Si $z$ está en \$ mil y $b_i$ en horas, $\pi_i$ está en <b>\$ mil por hora</b>. Contestar "el precio sombra es 10" sin unidad es media respuesta.</li>
    <li><b>Es un precio de <i>escasez</i>, no de mercado.</b> Un recurso que sobra vale $0$ aunque haya costado caro comprarlo. Un recurso barato puede tener precio sombra altísimo si es el cuello de botella.</li>
  </ul>
  <div class="key"><b>Interpretación geométrica.</b> Aumentar $b_i$ es <b>empujar hacia afuera</b> la recta de la restricción $i$. Si la restricción está <b>activa</b> (toca el óptimo), el vértice óptimo se mueve y $z^*$ mejora: $\pi_i>0$. Si está <b>inactiva</b> (le sobra holgura), empujarla no cambia nada: $\pi_i=0$.</div>
</section>

<section id="f2">
  <h3>2. El dual y las reglas de signo</h3>
  <p>El teorema de <b>dualidad fuerte</b> dice que si el primal tiene óptimo finito, el dual también, y</p>
  $$z^*_{\text{primal}} = w^*_{\text{dual}}\qquad\text{y}\qquad \pi_i = y_i^*.$$
  <p><b>Los precios sombra <i>son</i> la solución óptima del dual.</b> Por eso las preguntas de sensibilidad se contestan resolviendo el dual (que suele ser más chico) o leyendo el tableau óptimo del primal.</p>
  <h4>Correspondencia primal ↔ dual</h4>
  <table>
    <tr><th class="l">Primal (máx)</th><th class="l">Dual (mín)</th></tr>
    <tr><td class="l">$m$ restricciones</td><td class="l">$m$ variables $y_i$</td></tr>
    <tr><td class="l">$n$ variables $x_j$</td><td class="l">$n$ restricciones</td></tr>
    <tr><td class="l">coeficientes objetivo $c_j$</td><td class="l">lados derechos $c_j$</td></tr>
    <tr><td class="l">lados derechos $b_i$</td><td class="l">coeficientes objetivo $b_i$</td></tr>
    <tr><td class="l">matriz $A$</td><td class="l">matriz $A^\top$</td></tr>
  </table>
  <h4>Signo del dual según el tipo de restricción</h4>
  <p>Esta tabla evita la mitad de los errores en certamen:</p>
  <table>
    <tr><th>Primal</th><th>Restricción</th><th>Signo de $\pi_i$</th><th class="l">Por qué</th></tr>
    <tr><td rowspan="3"><b>máx</b></td><td>$\le$</td><td>$\pi_i \ge 0$</td><td class="l">más recurso nunca empeora un máximo</td></tr>
    <tr><td>$\ge$</td><td>$\pi_i \le 0$</td><td class="l">exigir más de un mínimo obligatorio <b>cuesta</b></td></tr>
    <tr><td>$=$</td><td>libre</td><td class="l">puede ser de cualquier signo</td></tr>
    <tr><td rowspan="3"><b>mín</b></td><td>$\ge$</td><td>$\pi_i \ge 0$</td><td class="l">exigir más requisito sube el costo</td></tr>
    <tr><td>$\le$</td><td>$\pi_i \le 0$</td><td class="l">más holgura de capacidad abarata</td></tr>
    <tr><td>$=$</td><td>libre</td><td class="l">—</td></tr>
  </table>
  <div class="tip"><b>Cuidado con el signo que reporta el software.</b> Gurobi entrega <code>constr.Pi</code> siempre como $\partial z^*/\partial b_i$ <b>con el sentido original del modelo</b>. En un máximo, una restricción $\ge$ activa da un <code>Pi</code> <b>negativo</b>, y eso <i>no</i> es un error: significa que esa exigencia le está costando plata a la empresa (lo vemos en el Ejemplo 4).</div>
</section>

<section id="f3">
  <h3>3. Holgura complementaria</h3>
  <p>Es el puente entre primal y dual, y la herramienta que permite <b>obtener la solución de uno teniendo la del otro</b> sin resolver nada.</p>
  $$\boxed{\;\pi_i\cdot s_i = 0\quad\forall i\;}\qquad\qquad \boxed{\;x_j\cdot rc_j = 0\quad\forall j\;}$$
  <p>donde $s_i = b_i - (Ax^*)_i$ es la holgura de la restricción $i$ y $rc_j$ el costo reducido de la variable $j$. En palabras, y en las dos direcciones:</p>
  <table>
    <tr><th class="l">Si...</th><th class="l">entonces...</th><th class="l">Negocio</th></tr>
    <tr><td class="l">la restricción <b>sobra</b> ($s_i>0$)</td><td class="l">$\pi_i = 0$</td><td class="l">un recurso que no se agota no vale nada al margen</td></tr>
    <tr><td class="l">$\pi_i > 0$</td><td class="l">la restricción es <b>activa</b> ($s_i=0$)</td><td class="l">solo los cuellos de botella tienen valor</td></tr>
    <tr><td class="l">la variable se <b>usa</b> ($x_j>0$)</td><td class="l">$rc_j=0$: su restricción dual es <b>igualdad</b></td><td class="l">lo que se produce paga exactamente lo que consume</td></tr>
    <tr><td class="l">$rc_j \ne 0$</td><td class="l">$x_j = 0$</td><td class="l">un producto que no rinde no se fabrica</td></tr>
  </table>
  <div class="key"><b>Es la condición KKT de siempre.</b> La holgura complementaria del LP es exactamente $\mu_i\,g_i(x^*)=0$ de las condiciones KKT, aplicada al caso lineal. El multiplicador de KKT y el precio sombra <b>son el mismo objeto</b>.</div>
  <div class="app"><b>Receta de certamen.</b> Te dan $y^*$ y te piden $x^*$ (o al revés):
  <ol style="margin:6px 0">
    <li>Con $y_i^*>0$ → la restricción primal $i$ es <b>igualdad</b>.</li>
    <li>Con $y_i^*=0$ y restricción primal <b>no activa</b> → sin información, pero...</li>
    <li>Evalúa las restricciones <b>duales</b> en $y^*$: las que quedan <b>estrictas</b> ($&gt;c_j$) fuerzan $x_j=0$.</li>
    <li>Con las $x_j$ sobrevivientes y las igualdades del paso 1, arma un sistema chico y resuélvelo.</li>
    <li>Verifica $c^\top x^* = b^\top y^*$. Si no coinciden, algo se rompió.</li>
  </ol></div>
</section>

<section id="f4">
  <h3>4. Costo reducido</h3>
  <p>El <b>costo reducido</b> de la variable $x_j$ es</p>
  $$\boxed{\;rc_j \;=\; c_j - y^{*\top}\!A_j \;=\; \underbrace{c_j}_{\text{lo que aporta}} \;-\; \underbrace{\sum_i \pi_i\,a_{ij}}_{\text{lo que cuesta en recursos escasos}}\;}$$
  <p>Es el <b>margen neto verdadero</b> del producto $j$, una vez que se le cobran los recursos a su precio de escasez.</p>
  <ul>
    <li>$rc_j = 0$ → la variable es <b>básica</b> (se produce). Paga exacto lo que consume.</li>
    <li>$rc_j &lt; 0$ (en máx) → <b>no conviene</b>: consume más valor del que aporta. Por eso $x_j^*=0$.</li>
    <li>$|rc_j|$ es <b>cuánto tendría que subir $c_j$</b> para que el producto empiece a ser rentable.</li>
  </ul>
  <div class="app"><b>Pregunta típica.</b> "¿A cuánto tendría que subir el precio del producto 1 para que convenga fabricarlo?" Respuesta: a $c_1 - rc_1$. Si $c_1=3$ y $rc_1=-4$, hay que llegar a $\mathbf{7}$. Ni un peso menos (a exactamente $7$ hay <b>empate</b>: óptimos alternativos).</div>
</section>

<section id="f5">
  <h3>5. Dónde están en el tableau óptimo</h3>
  <p>No hay que calcular nada aparte: el Simplex ya los dejó escritos.</p>
  <table>
    <tr><th class="l">En el tableau óptimo...</th><th class="l">...está</th></tr>
    <tr><td class="l">fila $z$, columna de la <b>holgura</b> $s_i$</td><td class="l">el <b>precio sombra</b> $\pi_i$ de la restricción $i$</td></tr>
    <tr><td class="l">fila $z$, columna de una variable <b>no básica</b> $x_j$</td><td class="l">el <b>costo reducido</b> $rc_j$</td></tr>
    <tr><td class="l">columna LD, fila $z$</td><td class="l">el valor óptimo $z^*$</td></tr>
    <tr><td class="l">columna LD, fila de una básica</td><td class="l">el valor de esa variable</td></tr>
  </table>
  <p>Y en forma matricial, si $B$ es la base óptima:</p>
  $$y^{*\top} = c_B^\top B^{-1}, \qquad rc^\top = c^\top - c_B^\top B^{-1}A, \qquad x_B = B^{-1}b, \qquad z^* = c_B^\top B^{-1} b.$$
  <div class="tip"><b>El signo depende de tu convención de tableau.</b> Según se escriba la fila $z$ como $z - c^\top x = 0$ o como $-z + c^\top x=0$, los duales aparecen con signo cambiado. La forma de no equivocarse nunca: <b>verifica con dualidad fuerte</b>, $\sum_i \pi_i b_i$ debe dar $z^*$. Si te da $-z^*$, invierte todos los signos.</div>
</section>
"""

# ---------------------------------------------------------------- Parte 2
P2 = r"""
<h2 class="part" id="p2">Bloque II — Rangos de validez</h2>

<section id="r1">
  <h3>6. ¿Hasta cuándo vale el precio sombra? Rango del lado derecho</h3>
  <p>El precio sombra es una <b>derivada</b>, y la derivada de una función lineal a trozos cambia en los quiebres. El precio sombra $\pi_i$ es válido mientras <b>la base óptima no cambie</b>, es decir mientras el mismo conjunto de restricciones siga activo.</p>
  <h4>La cuenta</h4>
  <p>Si aumentamos $b_i$ en $\Delta$, las variables básicas se mueven según</p>
  $$x_B(\Delta) \;=\; B^{-1}b + \Delta\,B^{-1}e_i \;=\; x_B^* + \Delta\,\beta^{(i)},$$
  <p>donde $\beta^{(i)}$ es la $i$-ésima <b>columna de $B^{-1}$</b>. La base sigue siendo factible mientras $x_B(\Delta)\ge0$, lo que da una <b>razón mínima</b> por cada lado:</p>
  $$\boxed{\;-\min_{k:\,\beta_k^{(i)}>0}\frac{x_{B_k}^*}{\beta_k^{(i)}}\;\le\;\Delta\;\le\;\min_{k:\,\beta_k^{(i)}<0}\frac{x_{B_k}^*}{-\beta_k^{(i)}}\;}$$
  <p>En 2 variables no hace falta invertir nada: basta escribir el sistema de las dos restricciones activas con $b_i$ como letra, despejar $x^*(b_i)$ y exigir <b>(a)</b> no negatividad y <b>(b)</b> que las restricciones inactivas <i>sigan</i> siendo satisfechas. El Ejemplo 1 lo hace paso a paso.</p>
  <div class="key"><b>Dentro del rango:</b> $z^*(b_i+\Delta) = z^* + \pi_i\Delta$, <b>exacto</b>, no aproximado. El plan de producción cambia (las $x_j$ se mueven), pero <b>quiénes son las básicas</b> no.<br>
  <b>Fuera del rango:</b> cambia la base y $\pi_i$ toma otro valor. En un <b>máximo</b>, $z^*(b)$ es <b>cóncava</b>: los precios sombra van <b>bajando</b> por tramos, así que extrapolar sobreestima la ganancia.</div>
  <div class="tip"><b>Error clásico.</b> "El precio sombra de la bodega es 20, entonces arrendar 40 m² más me da 800 de utilidad extra." <b>Falso</b> si el rango llega hasta +3,57 m². Lo correcto: gano $20\times3{,}57$ y desde ahí <b>hay que volver a resolver</b>, porque otro recurso pasó a ser el cuello de botella.</div>
</section>

<section id="r2">
  <h3>7. Rango de validez de un coeficiente objetivo $c_j$</h3>
  <p>Aquí la lógica es la contraria: cambiar $c_j$ <b>no mueve la región factible</b>, así que el óptimo <i>no se mueve</i> hasta que la isobeneficio rota lo suficiente como para "caerse" a otro vértice. La condición es <b>optimalidad</b> (que todos los costos reducidos mantengan su signo), no factibilidad.</p>
  <table>
    <tr><th class="l">Caso</th><th class="l">Condición</th><th class="l">Forma del rango</th></tr>
    <tr><td class="l"><b>$x_j$ no básica</b> ($x_j^*=0$)</td><td class="l">basta que siga sin convenir: $rc_j\le0$</td><td class="l">un solo lado: $c_j \le c_j^{\text{actual}} - rc_j$</td></tr>
    <tr><td class="l"><b>$x_j$ básica</b> ($x_j^*&gt;0$)</td><td class="l">todos los $rc_k$ de las no básicas deben seguir $\le0$</td><td class="l">intervalo cerrado por ambos lados</td></tr>
  </table>
  <div class="key"><b>Dentro del rango de $c_j$ la solución $x^*$ es la misma</b> (mismo plan de producción), pero <b>$z^*$ sí cambia</b>: $z^*(c_j) = z^* + (c_j - c_j^{\text{actual}})\,x_j^*$. La pendiente es $x_j^*$. Y $z^*(c_j)$ es <b>convexa</b> a trozos (al revés que $z^*(b)$).</div>
  <div class="app"><b>Pregunta típica.</b> "Si el margen del durazno cae de 30 a 22 mil, ¿cambia el plan?" Como $22\in[20,40]$: <b>no cambia el plan</b>, se siguen procesando 10 t de durazno y 35 de cereza; solo cae el beneficio en $8\times10=80$ mil.</div>
</section>

<section id="r3">
  <h3>8. Cuando cambian varios parámetros a la vez: la regla del 100 %</h3>
  <p>Los rangos anteriores son <b>"ceteris paribus"</b>: valen cambiando <b>un</b> parámetro a la vez. Si cambian varios, se usa la <b>regla del 100 %</b>: para cada parámetro se calcula qué fracción de su rango permitido se está consumiendo, y</p>
  $$\sum_j \frac{|\Delta_j|}{\text{rango permitido en esa dirección}} \;\le\; 1 \;\;\Longrightarrow\;\; \text{la base óptima no cambia.}$$
  <div class="tip"><b>Es suficiente, no necesaria.</b> Si la suma pasa de 1, <b>no se puede concluir nada</b>: puede que la base igual aguante. La única respuesta segura en ese caso es <b>volver a resolver</b>. Y ojo: la regla se aplica por separado a los $b_i$ y a los $c_j$; no se mezclan en la misma suma.</div>
</section>
"""

# ---------------------------------------------------------------- Ejemplos
E1 = r"""
<h2 class="part" id="p3">Bloque III — Ejemplos resueltos</h2>

<section id="e1">
  <span class="badge">Ejemplo 1 · completo · 2 variables</span>
  <h3>Conservera: precios sombra, rango de $b$ y rango de $c$</h3>
  <div class="app"><b>Enunciado.</b> Una empresa de alimentos planifica la temporada de <b>duraznos</b> ($x_1$) y <b>cerezas</b> ($x_2$) en conserva, en toneladas por semana. La fruta pasa por <b>revisión y clasificación</b> (1 h/t de durazno, 2 h/t de cereza; 80 h disponibles), luego por <b>despalillado y lavado</b> (5 h/t y 3 h/t; 180 h disponibles), y finalmente se guarda en una <b>bodega</b> con capacidad para 45 t semanales en total. El beneficio es de 30 mil \$/t de durazno y 40 mil \$/t de cereza.</div>
  $$\max\;\; 30x_1+40x_2 \qquad \text{s.a.}\quad
  \begin{cases}
  x_1+2x_2 \le 80 & \text{(R1 clasificación)}\\
  5x_1+3x_2 \le 180 & \text{(R2 despalillado)}\\
  x_1+x_2 \le 45 & \text{(R3 bodega)}\\
  x_1,x_2\ge0
  \end{cases}$$

  <h4>Paso 1 — Resolver (gráficamente)</h4>
  """ + img("region") + r"""
  <p>El óptimo está en la intersección de <b>R1 y R3</b>:</p>
  $$\begin{cases} x_1+2x_2=80\\ x_1+x_2=45\end{cases}\;\Longrightarrow\;x_2=35,\;x_1=10,\qquad z^*=30(10)+40(35)=\mathbf{1700}.$$
  <p>Verificamos R2: $5(10)+3(35)=155\le180$, sobra una <b>holgura de 25 h</b>. Por holgura complementaria, ya sabemos que $\boxed{\pi_2=0}$ sin calcular nada.</p>

  <h4>Paso 2 — El dual</h4>
  $$\min\;\;80y_1+180y_2+45y_3\qquad\text{s.a.}\quad
  \begin{cases}
  y_1+5y_2+y_3 \ge 30 & (x_1)\\
  2y_1+3y_2+y_3 \ge 40 & (x_2)\\
  y_1,y_2,y_3\ge0
  \end{cases}$$
  <p>Como $x_1^*&gt;0$ y $x_2^*&gt;0$, <b>ambas restricciones duales son igualdades</b> (holgura complementaria). Y como $s_2=25&gt;0$, $y_2=0$. Queda un sistema $2\times2$ que se resuelve a mano:</p>
  $$\begin{cases} y_1+y_3=30\\ 2y_1+y_3=40\end{cases}\;\Longrightarrow\;\boxed{y_1=\pi_1=10,\quad y_3=\pi_3=20,\quad \pi_2=0}$$
  <p><b>Chequeo de dualidad fuerte:</b> $80(10)+180(0)+45(20)=800+900=1700=z^*$ ✓.</p>

  <h4>Paso 3 — Interpretación de negocio</h4>
  <table>
    <tr><th class="l">Recurso</th><th>$b_i$</th><th>Holgura</th><th>$\pi_i$ (mil\$/unidad)</th><th class="l">Lectura</th></tr>
    <tr><td class="l">R1 Clasificación</td><td>80 h</td><td>0</td><td><b>10</b></td><td class="l">una hora más de clasificación vale 10 mil</td></tr>
    <tr><td class="l">R2 Despalillado</td><td>180 h</td><td>25 h</td><td><b>0</b></td><td class="l">sobra: no pagues <b>nada</b> por horas extra aquí</td></tr>
    <tr><td class="l">R3 Bodega</td><td>45 t</td><td>0</td><td><b>20</b></td><td class="l">una tonelada más de bodega vale 20 mil — <b>el cuello de botella caro</b></td></tr>
  </table>
  <div class="app"><b>Decisión.</b> Si arrendar una tonelada extra de bodega cuesta 14 mil \$/semana, <b>conviene</b> (gano 6 mil netos por tonelada). Si contratar una hora extra de clasificación cuesta 12 mil, <b>no conviene</b>. Y capacitar gente para despalillado es <b>plata tirada</b> hoy: ese recurso sobra.</div>

  <h4>Paso 4 — Rango de validez de $b_1$ (horas de clasificación)</h4>
  <p>Mantenemos activas R1 y R3 y dejamos $b_1$ como letra:</p>
  $$\begin{cases} x_1+2x_2=b_1\\ x_1+x_2=45\end{cases}\;\Longrightarrow\;x_2=b_1-45,\qquad x_1=90-b_1.$$
  <p>Tres condiciones deben seguir cumpliéndose:</p>
  <table>
    <tr><th class="l">Condición</th><th class="l">Cuenta</th><th class="l">Cota</th></tr>
    <tr><td class="l">$x_1\ge0$</td><td class="l">$90-b_1\ge0$</td><td class="l">$b_1\le \mathbf{90}$</td></tr>
    <tr><td class="l">$x_2\ge0$</td><td class="l">$b_1-45\ge0$</td><td class="l">$b_1\ge 45$</td></tr>
    <tr><td class="l">R2 sigue holgada</td><td class="l">$5(90-b_1)+3(b_1-45)=315-2b_1\le180$</td><td class="l">$b_1\ge \mathbf{67{,}5}$</td></tr>
  </table>
  $$\boxed{\;b_1\in[67{,}5\;;\;90]\;}\qquad\text{y en ese rango}\quad z^*(b_1)=900+10\,b_1.$$
  <div class="tip"><b>Nota sobre la solución de clase.</b> La clave de respuestas de la <b>Clase 23</b> indica $62{,}5$ como cota inferior de este rango. El valor correcto es <b>$67{,}5$</b>: la cota la impone la restricción de despalillado, $5(90-b_1)+3(b_1-45)=315-2b_1\le180 \Rightarrow b_1\ge 135/2 = 67{,}5$. Gurobi lo confirma (<code>SARHSLow = 67.5</code>, ver la sección 9), y en $b_1=62{,}5$ el plan $(x_1,x_2)=(27{,}5\,;\,17{,}5)$ requeriría $5(27{,}5)+3(17{,}5)=190$ horas de despalillado, más que las 180 disponibles: sería <b>infactible</b>. Con $67{,}5$ el consumo da exactamente $180$.</div>
  """ + img("b1", "Izquierda: al mover $b_1$ el vértice óptimo se desliza sobre la recta de la bodega. Derecha: $z^*(b_1)$ es cóncava y lineal a trozos; el precio sombra es la pendiente del tramo.") + r"""
  <div class="key"><b>Qué muestra el gráfico (b).</b> En $b_1=90$ el vértice llega a $x_1=0$: la clasificación deja de ser cuello de botella y $\pi_1$ cae a <b>0</b> — regalar más horas ya no sirve de nada. En $b_1=67{,}5$ el despalillado (R2) se activa y $\pi_1$ salta a $110/7\approx15{,}7$. Los precios sombra <b>decrecen</b> de izquierda a derecha: eso es la concavidad de $z^*(b)$, y es la razón matemática por la que <b>extrapolar sobreestima</b>.</div>
  <div class="tip"><b>Pregunta con trampa.</b> "¿Cuánto gano con 20 horas extra de clasificación?" El rango permite solo $+10$. Respuesta correcta: <b>$10\times10=100$ mil</b> por las primeras 10 horas, y las 10 siguientes valen <b>0</b>. Contestar $20\times10=200$ es el error más frecuente en el certamen.</div>

  <h4>Paso 5 — Rango de validez de $c_1$ (margen del durazno)</h4>
  <p>El vértice $(10,35)$ está fijo; lo que puede fallar es la <b>optimalidad</b>. Rehacemos el sistema dual dejando $c_1$ como letra:</p>
  $$\begin{cases} y_1+y_3=c_1\\ 2y_1+y_3=40\end{cases}\;\Longrightarrow\;y_1=40-c_1,\qquad y_3=2c_1-40.$$
  <p>Exigimos factibilidad dual $y_1,y_3\ge0$:</p>
  $$40-c_1\ge0 \;\Rightarrow\; c_1\le40, \qquad 2c_1-40\ge0 \;\Rightarrow\; c_1\ge20 \qquad\Longrightarrow\qquad \boxed{\;c_1\in[20\,;\,40]\;}$$
  """ + img("c1", "Izquierda: al mover $c_1$ la isobeneficio rota pero el vértice óptimo no se mueve. Derecha: $z^*(c_1)$ es convexa a trozos y su pendiente es $x_1^*=10$.") + r"""
  <div class="key">Nótese la <b>simetría</b> con el caso de $b$: la pendiente de $z^*(b_i)$ es $\pi_i$ y la función es <b>cóncava</b>; la pendiente de $z^*(c_j)$ es $x_j^*$ y la función es <b>convexa</b>. En ambos casos, salir del rango significa cambiar de tramo.</div>
</section>
"""

E2 = r"""
<section id="e2">
  <span class="badge">Ejemplo 2 · dual completo · reducción de un recurso</span>
  <h3>Distribuidora de gas: ¿hasta dónde puedo recortar?</h3>
  <div class="app"><b>Enunciado.</b> Una distribuidora arma dos <i>packs</i> promocionales. <b>Super65</b> lleva un balón de 5 kg, uno de 15 kg y un cilindro de 45 kg; <b>Extra170</b> lleva uno de 5 kg, <b>dos</b> de 15 kg y <b>tres</b> cilindros de 45 kg. Hay 40 balones de 5 kg, 50 de 15 kg y 66 cilindros de 45 kg. El beneficio es 10 mil \$ por Super65 y 24 mil \$ por Extra170.</div>
  $$\max\;10x_1+24x_2\quad\text{s.a.}\quad x_1+x_2\le40,\;\; x_1+2x_2\le50,\;\; x_1+3x_2\le66,\;\;x\ge0$$
  <p>Nos dicen que en el óptimo <b>se ofrecen ambos packs</b> y $z^*=564$. Eso basta para todo lo demás.</p>

  <h4>a) El dual</h4>
  $$\min\;40y_1+50y_2+66y_3\quad\text{s.a.}\quad y_1+y_2+y_3\ge10,\;\; y_1+2y_2+3y_3\ge24,\;\;y\ge0$$

  <h4>b) Resolverlo con holgura complementaria (sin Simplex)</h4>
  <p>Como $x_1^*&gt;0$ y $x_2^*&gt;0$, <b>las dos restricciones duales son igualdades</b>. Faltaba una ecuación: la da el primal. Si las tres restricciones primales fueran activas, el sistema $3\times3$ sería incompatible en general; probamos con las dos "más apretadas" (R2 y R3):</p>
  $$\begin{cases} x_1+2x_2=50\\ x_1+3x_2=66 \end{cases}\Rightarrow x_2=16,\;x_1=18 \quad\Rightarrow\quad z=10(18)+24(16)=564\;✓$$
  <p>El dato $z^*=564$ <b>confirma</b> la elección. Además $x_1+x_2=34&lt;40$: sobran <b>6 balones de 5 kg</b>, luego $y_1=0$. Con eso:</p>
  $$\begin{cases} y_2+y_3=10\\ 2y_2+3y_3=24\end{cases}\Rightarrow \boxed{y^*=(0,\;6,\;4)}$$
  <p>Chequeo: $40(0)+50(6)+66(4)=300+264=564$ ✓.</p>
  <div class="app"><b>Lectura.</b> Un balón adicional de <b>15 kg</b> vale 6 mil \$; un cilindro de <b>45 kg</b>, 4 mil \$. Los balones de 5 kg <b>no valen nada al margen</b>: hay 6 durmiendo en bodega.</div>

  <h4>c) ¿Hasta cuánto puede <i>bajar</i> la disponibilidad de balones de 15 kg?</h4>
  <p>Con $b_2$ como letra, manteniendo R2 y R3 activas: $x_1+2x_2=b_2$, $x_1+3x_2=66$, de donde $x_2=66-b_2$ y $x_1=3b_2-132$.</p>
  <table>
    <tr><th class="l">Condición</th><th class="l">Cuenta</th><th class="l">Cota</th></tr>
    <tr><td class="l">$x_1\ge0$</td><td class="l">$3b_2-132\ge0$</td><td class="l">$b_2\ge\mathbf{44}$</td></tr>
    <tr><td class="l">$x_2\ge0$</td><td class="l">$66-b_2\ge0$</td><td class="l">$b_2\le66$</td></tr>
    <tr><td class="l">R1 sigue holgada</td><td class="l">$x_1+x_2=2b_2-66\le40$</td><td class="l">$b_2\le\mathbf{53}$</td></tr>
  </table>
  $$\boxed{\;b_2\in[44\,;\,53]\;}$$
  <p>Es decir, la disponibilidad puede bajar hasta <b>44 balones de 15 kg</b> sin cambiar la combinación de packs.</p>
  <p>Bajar de 50 a 44 cuesta $6\times6=36$ mil de beneficio. Bajo 44 <b>hay que volver a resolver</b>: el pack Super65 desaparece del plan.</p>
</section>
"""

E3 = r"""
<section id="e3">
  <span class="badge">Ejemplo 3 · 3 variables · costo reducido</span>
  <h3>Juguetes <i>Otto Kraus</i>: el producto que no conviene fabricar</h3>
  <div class="app"><b>Enunciado.</b> Se fabrican <b>trenes</b> ($x_1$), <b>camiones</b> ($x_2$) y <b>autos</b> ($x_3$) en tres máquinas de ensamblaje con 430, 460 y 420 minutos diarios.</div>
  <table>
    <tr><th class="l">Juguete</th><th>Máq. 1</th><th>Máq. 2</th><th>Máq. 3</th><th>Precio</th></tr>
    <tr><td class="l">Tren $x_1$</td><td>1</td><td>3</td><td>1</td><td>3</td></tr>
    <tr><td class="l">Camión $x_2$</td><td>2</td><td>0</td><td>4</td><td>2</td></tr>
    <tr><td class="l">Auto $x_3$</td><td>1</td><td>2</td><td>0</td><td>5</td></tr>
  </table>
  $$\max\;3x_1+2x_2+5x_3\quad\text{s.a.}\quad x_1+2x_2+x_3\le430,\;\;3x_1+2x_3\le460,\;\;x_1+4x_2\le420$$
  <p>El óptimo es $x^*=(0,\,100,\,230)$ con $z^*=1350$: <b>no se fabrican trenes</b>.</p>

  <h4>Precios sombra</h4>
  <p>M3 tiene holgura ($400\le420$) $\Rightarrow y_3=0$. Como $x_2,x_3&gt;0$, sus restricciones duales son igualdades:</p>
  $$\begin{cases} 2y_1+4y_3=2 \;\Rightarrow\; y_1=1\\ y_1+2y_2=5 \;\Rightarrow\; y_2=2\end{cases}\qquad \boxed{y^*=(1,\,2,\,0)}$$
  <p>Chequeo: $430(1)+460(2)+420(0)=430+920=1350$ ✓.</p>

  <h4>El costo reducido del tren</h4>
  $$rc_1 = c_1 - \big(y_1a_{11}+y_2a_{21}+y_3a_{31}\big) = 3-\big(1\cdot1+2\cdot3+0\cdot1\big) = 3-7 = \boxed{-4}$$
  <div class="app"><b>Lectura de negocio.</b> Un tren se vende en 3, pero <b>consume 7</b> en minutos de máquina valorados a su precio de escasez (es carísimo en la máquina 2, que es el recurso más valioso). Cada tren que se fabrique destruye 4 de valor.<br><br>
  <b>¿A cuánto tendría que subir el precio del tren para que convenga?</b> A $3-(-4)=\mathbf{7}$. A exactamente 7 hay <b>empate</b> (óptimos alternativos); sobre 7, entra a la base.</div>
  <div class="key"><b>Precios sombra y decisión.</b> Un minuto extra de la máquina 2 vale <b>2</b>; de la máquina 1, <b>1</b>; de la máquina 3, <b>0</b>. Si el mantenimiento preventivo obliga a apagar una máquina 30 minutos, hágalo en la <b>máquina 3</b>: cuesta cero.</div>
</section>
"""

E4 = r"""
<section id="e4">
  <span class="badge">Ejemplo 4 · restricción $\ge$ · precio sombra NEGATIVO</span>
  <h3>Taller de muebles: cuánto cuesta un compromiso de venta</h3>
  <div class="app"><b>Enunciado.</b> Un taller produce sillas ($x_1$), mesas ($x_2$) y cómodas ($x_3$). Además de la madera, la pintura y el pegamento, tiene <b>ventas ya comprometidas</b> que está obligado a cumplir.</div>
  $$\max\; 10x_1+40x_2+35x_3$$
  $$\begin{array}{llll}
  \text{R1 madera:} & 2x_1+10x_2+25x_3 \le 200 &\quad \text{R4:} & x_1\ge10\\
  \text{R2 pintura:} & 2x_1+5x_2+5x_3 \le 120 &\quad \text{R5:} & x_2\ge4\\
  \text{R3 pegamento:} & x_1+4x_2+5x_3 \le 230 &\quad \text{R6:} & x_3\ge2
  \end{array}$$
  <p>El óptimo es $x^*=(35,\,8,\,2)$ con $z^*=740$. Activas: R1 ($=200$), R2 ($=120$) y <b>R6</b> ($x_3=2$, pegado a su mínimo). R3, R4 y R5 tienen holgura.</p>

  <h4>Precios sombra</h4>
  <p>Como $x_1,x_2$ son básicas y R3, R4, R5 están holgadas ($y_3=y_4=y_5=0$):</p>
  $$\begin{cases} 2y_1+2y_2=10\\ 10y_1+5y_2=40\end{cases}\;\Longrightarrow\;\boxed{y_1=3,\quad y_2=2}$$
  <p>Y para $x_3$, que está <b>en su cota inferior</b> por culpa de R6:</p>
  $$25y_1+5y_2 = 75+10 = 85 \;>\; 35 = c_3 \qquad\Rightarrow\qquad rc_3 = 35-85 = -50 \qquad\Rightarrow\qquad \boxed{\pi_6 = -50}$$
  <table>
    <tr><th class="l">Restricción</th><th>Tipo</th><th>$\pi_i$</th><th class="l">Interpretación</th></tr>
    <tr><td class="l">R1 madera</td><td>$\le$</td><td><b>+3</b></td><td class="l">un metro más de madera aporta 3</td></tr>
    <tr><td class="l">R2 pintura</td><td>$\le$</td><td><b>+2</b></td><td class="l">un barril más de pintura aporta 2</td></tr>
    <tr><td class="l">R3 pegamento</td><td>$\le$</td><td><b>0</b></td><td class="l">sobra: no pague por más pegamento</td></tr>
    <tr><td class="l">R6 cómodas $\ge2$</td><td>$\ge$</td><td><b>−50</b></td><td class="l">cada cómoda comprometida <b>destruye 50</b> de utilidad</td></tr>
  </table>
  <div class="tip"><b>Este es el signo que confunde a todo el mundo.</b> $\pi_6=-50$ <b>no</b> es un error de cálculo ni de software: en un problema de <b>máximo</b>, una restricción $\ge$ activa <i>obliga</i> a hacer algo que el modelo no quería hacer, y por lo tanto <b>empeora</b> el óptimo. La regla de signo de la sección 2 lo anticipaba.</div>
  <div class="app"><b>La decisión que habilita.</b> La cómoda consume 25 unidades de madera —el recurso escaso a 3 c/u— y 5 de pintura, y solo devuelve 35. Si el cliente permite <b>renegociar el compromiso</b>, el taller debería estar dispuesto a pagar <b>hasta 50 mil por cada cómoda que lo liberen de fabricar</b>. Equivalentemente: si logra vender la cómoda a más de $85$, el compromiso deja de ser una pérdida.</div>
</section>
"""

E5 = r"""
<section id="e5">
  <span class="badge">Ejemplo 5 · minimización · leer el tableau</span>
  <h3>Problema de dieta: los precios sombra estaban en la fila $z$</h3>
  <p>Este es el <b>Ejercicio 18</b> que el profesor resolvió por Simplex matricial y por el dual en la Clase 22. Aquí lo usamos para <b>leer los duales directamente del tableau</b>.</p>
  $$\min\;25x_1+20x_2\quad\text{s.a.}\quad 4x_1+3x_2\ge250,\;\;3x_1+4x_2\ge270,\;\;2x_1+5x_2\ge300,\;\;x\ge0$$
  <p>El óptimo es $x^*=(25,\,50)$ con $z^*=1625$. El tableau óptimo que quedó en clase (fila $z$ y columnas de holgura) es:</p>
  <table>
    <tr><th>V. Básica</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>LD</th></tr>
    <tr><td>$z$</td><td>0</td><td>0</td><td><b>$85/14$</b></td><td>0</td><td><b>$5/14$</b></td><td>$-1625$</td></tr>
    <tr><td>$x_1$</td><td>1</td><td>0</td><td>$-5/14$</td><td>0</td><td>$3/14$</td><td>25</td></tr>
    <tr><td>$s_2$</td><td>0</td><td>0</td><td>$-1/2$</td><td>1</td><td>$-1/2$</td><td>5</td></tr>
    <tr><td>$x_2$</td><td>0</td><td>1</td><td>$1/7$</td><td>0</td><td>$-10/35$</td><td>50</td></tr>
  </table>
  <p>Los coeficientes de la fila $z$ bajo las <b>holguras</b> son los precios sombra:</p>
  $$\boxed{\;\pi_1=\tfrac{85}{14}\approx6{,}071,\qquad \pi_2=0,\qquad \pi_3=\tfrac{5}{14}\approx0{,}357\;}$$
  <p>Chequeo de dualidad fuerte: $250\cdot\tfrac{85}{14}+300\cdot\tfrac{5}{14} = \tfrac{21250+1500}{14}=\tfrac{22750}{14}=1625$ ✓.</p>
  <div class="key"><b>Todo cuadra sin resolver nada más.</b> $s_2$ es <b>básica</b> con valor 5 (la segunda restricción tiene holgura de 5) $\Rightarrow \pi_2=0$, tal como dice la holgura complementaria. Y $x_1, x_2$ básicas $\Rightarrow$ costos reducidos nulos, que es el $0$ bajo sus columnas.</div>
  <div class="app"><b>Lectura en un problema de mínimo.</b> Aquí $\pi_i\ge0$ significa <b>costo</b>: subir el requerimiento 1 en una unidad <b>encarece</b> la dieta en 6,07. Al revés, si se logra <b>relajar</b> ese requerimiento en una unidad, se <b>ahorran</b> 6,07. El requerimiento 2 se cumple "de yapa": relajarlo no ahorra nada.</div>
</section>
"""

E6 = r"""
<section id="e6">
  <span class="badge">Ejemplo 6 · MIP · lo que hicimos en la Ayudantía 7</span>
  <h3>Cuando hay binarias: fijarlas para poder hablar de precios sombra</h3>
  <div class="tip"><b>Un MIP no tiene precios sombra.</b> El análisis de sensibilidad vive en el <b>tableau óptimo del Simplex</b>, y un problema con enteras se resuelve por <i>branch and bound</i>: no hay una base óptima única, no hay dual. Si le pide <code>.Pi</code> a un modelo con enteras, Gurobi devuelve error.</div>
  <h4>La técnica</h4>
  <ol>
    <li>Resolver el MIP y guardar el valor óptimo de las binarias, $y^*$.</li>
    <li><b>Fijarlas</b> en ese valor ($lb=ub=y^*$) — con <code>m.fixed()</code> o reconstruyendo el modelo con $y^*$ como <b>dato</b>.</li>
    <li>Ahora es un <b>LP puro</b>: tiene duales, holguras y rangos. Verificar que <code>IsMIP == 0</code> y que el valor objetivo <b>coincide</b> con el del MIP.</li>
    <li>Hacer el análisis de sensibilidad sobre ese LP.</li>
  </ol>
  <div class="key"><b>Qué se gana y qué se pierde.</b> Se gana toda la maquinaria de sensibilidad. Se pierde la libertad de la binaria: los duales describen el sistema <b>con esa configuración discreta congelada</b>. Cualquier pregunta cuya respuesta implique <i>cambiar</i> $y^*$ (abrir otra planta, agregar un camión, encender otro turno) queda <b>fuera del alcance</b> de esos duales.</div>

  <h4>Por qué la extrapolación falla en los dos sentidos</h4>
  <p>En un LP, $z^*(b)$ es <b>cóncava</b> (en máx), así que el precio sombra siempre <b>sobreestima</b> fuera del rango. En un MIP no: $z^*(b)$ es el <b>máximo</b> de las curvas cóncavas de cada configuración discreta, y un máximo de cóncavas <b>no es cóncavo</b>.</p>
  """ + img("mip", "Modelo ilustrativo: $\\max\\,8x_1+6x_2-20y$ con $x_1+x_2\\le10+15y$ y $2x_1+x_2\\le b$. Cada línea a trazos es el LP con la binaria congelada; la banda azul es el MIP.") + r"""
  <div class="key"><b>Cómo leer el gráfico.</b> Hoy $b=12$ y el óptimo tiene $y^*=0$: se trabaja sin turno extra. El LP con $y$ fija reporta $\pi=2$, válido hasta $b=20$. Pero en $b=15$ al MIP <b>le empieza a convenir encender el turno</b> y salta a la curva verde, cuya pendiente es <b>6</b>. Resultado: con $b=20$ el valor real es <b>100</b> y la extrapolación con el precio sombra predecía <b>80</b>. En un LP puro esto es <i>imposible</i>: la extrapolación siempre sobreestima. En un MIP puede fallar <b>para cualquier lado</b>.</div>
  <div class="app"><b>Lo que vimos en Kütral Café (Ayudantía 7).</b> Con $y^*=(0,0,1)$ el LP daba $\pi_{\text{volumen camión}}=1062{,}5$ y $\pi_{\text{tostado}}=3{,}84$. Dentro del rango la predicción era <b>exacta al centavo</b>. Fuera del rango falló en <b>ambas direcciones</b>: $+0{,}4$ m³ de bodega <b>sobreestimó 3,3 veces</b> (concavidad del LP), pero $+1{,}0$ m³ de camión <b>subestimó</b> (1.062,5 predicho contra 1.496,75 real) porque el óptimo cambió a $y^*=(0,1,1)$ — se encendió otro turno. Y para el <b>salto discreto</b> de un segundo camión, el precio sombra predecía 6.837,5 de ganancia contra <b>896,75</b> reales.</div>
  <div class="tip"><b>Regla práctica.</b> El precio sombra de un MIP-con-binaria-fija sirve para <b>ajustes chicos y continuos</b> (un poco más de horas, un poco más de m³). Para <b>decisiones discretas</b> (¿abro la planta? ¿arriendo el camión?) <b>no sirve</b>: hay que resolver los dos escenarios y comparar los valores objetivo.</div>
</section>
"""

GUR = r"""
<h2 class="part" id="p4">Bloque IV — Gurobi y trampas</h2>

<section id="gur">
  <h3>9. Todo esto en <code>gurobipy</code></h3>
  <table>
    <tr><th class="l">Atributo</th><th class="l">Se pide a</th><th class="l">Qué entrega</th></tr>
    <tr><td class="l"><code>.Pi</code></td><td class="l">restricción</td><td class="l"><b>precio sombra</b> $\pi_i=\partial z^*/\partial b_i$</td></tr>
    <tr><td class="l"><code>.Slack</code></td><td class="l">restricción</td><td class="l">holgura $s_i$ (negativa en las $\ge$: es excedente)</td></tr>
    <tr><td class="l"><code>.SARHSLow</code> / <code>.SARHSUp</code></td><td class="l">restricción</td><td class="l"><b>rango de validez</b> de $b_i$</td></tr>
    <tr><td class="l"><code>.RC</code></td><td class="l">variable</td><td class="l"><b>costo reducido</b> $rc_j$</td></tr>
    <tr><td class="l"><code>.SAObjLow</code> / <code>.SAObjUp</code></td><td class="l">variable</td><td class="l"><b>rango de validez</b> de $c_j$</td></tr>
    <tr><td class="l"><code>.IsMIP</code></td><td class="l">modelo</td><td class="l">1 si hay enteras → <b>no hay duales</b></td></tr>
    <tr><td class="l"><code>.fixed()</code></td><td class="l">modelo</td><td class="l">devuelve el LP con las enteras fijadas en su óptimo</td></tr>
  </table>

  <h4>El Ejemplo 1 completo, con su tabla de sensibilidad</h4>
<pre><code class="language-python">import gurobipy as gp
from gurobipy import GRB

m = gp.Model("conservas")
m.Params.OutputFlag = 0

x1 = m.addVar(name="durazno")          # toneladas de durazno
x2 = m.addVar(name="cereza")           # toneladas de cereza

m.setObjective(30*x1 + 40*x2, GRB.MAXIMIZE)

# Nombrar las restricciones es clave: despues se piden los duales por nombre
m.addConstr(1*x1 + 2*x2 &lt;= 80,  name="clasificacion")
m.addConstr(5*x1 + 3*x2 &lt;= 180, name="despalillado")
m.addConstr(1*x1 + 1*x2 &lt;= 45,  name="bodega")

m.optimize()

print(f"z* = {m.ObjVal:,.2f}   x* = ({x1.X:.1f}, {x2.X:.1f})\n")

print(f"{'restriccion':&lt;16}{'RHS':&gt;8}{'holgura':&gt;10}{'pi':&gt;9}{'rango de validez':&gt;24}")
for c in m.getConstrs():
    print(f"{c.ConstrName:&lt;16}{c.RHS:&gt;8.1f}{c.Slack:&gt;10.2f}{c.Pi:&gt;9.2f}"
          f"{'[' + format(c.SARHSLow, '.2f') + ' ; ' + format(c.SARHSUp, '.2f') + ']':&gt;24}")

print(f"\n{'variable':&lt;16}{'valor':&gt;8}{'c_j':&gt;10}{'RC':&gt;9}{'rango de validez':&gt;24}")
for v in m.getVars():
    print(f"{v.VarName:&lt;16}{v.X:&gt;8.1f}{v.Obj:&gt;10.2f}{v.RC:&gt;9.2f}"
          f"{'[' + format(v.SAObjLow, '.2f') + ' ; ' + format(v.SAObjUp, '.2f') + ']':&gt;24}")

# Verificacion de dualidad fuerte
print(f"\nSuma pi_i * b_i = {sum(c.Pi*c.RHS for c in m.getConstrs()):,.2f}  (debe ser z*)")
</code></pre>
  <p>Salida:</p>
<pre><code>z* = 1,700.00   x* = (10.0, 35.0)

restriccion          RHS   holgura       pi        rango de validez
clasificacion       80.0      0.00    10.00         [67.50 ; 90.00]
despalillado       180.0     25.00     0.00          [155.00 ; inf]
bodega              45.0      0.00    20.00         [40.00 ; 48.57]

variable           valor       c_j       RC        rango de validez
durazno             10.0     30.00     0.00         [20.00 ; 40.00]
cereza              35.0     40.00     0.00         [30.00 ; 60.00]

Suma pi_i * b_i = 1,700.00  (debe ser z*)
</code></pre>
  <div class="key">Todo lo que calculamos a mano en el Ejemplo 1 está ahí: $\pi=(10,0,20)$, el rango $[67{,}5\,;\,90]$ para la clasificación y $[20\,;\,40]$ para el margen del durazno. <b>El desarrollo a mano no es folklore: es lo que le permite saber si el número que devolvió el software tiene sentido.</b></div>

  <h4>Un MIP: fijar la binaria para obtener los duales</h4>
<pre><code class="language-python">m.optimize()                      # 1) resolver el MIP
ystar = {t: round(y[t].X) for t in T}

fx = m.fixed()                    # 2) LP con las enteras fijadas en su optimo
fx.Params.OutputFlag = 0
fx.optimize()

print(fx.IsMIP, fx.ObjVal == m.ObjVal)   # 3) debe ser 0 y True

for c in fx.getConstrs():         # 4) ahora si hay duales
    if abs(c.Pi) &gt; 1e-9:
        print(f"{c.ConstrName:&lt;20} pi = {c.Pi:10.4f}   holgura = {c.Slack:8.3f}")
</code></pre>
  <div class="tip"><b>Dos detalles que arruinan pautas.</b> (1) Ponga <code>m.Params.MIPGap = 0.0</code> cuando vaya a comparar escenarios: con el gap por defecto ($10^{-4}$) un escenario <i>con más recurso</i> puede dar un objetivo <i>menor</i> y el análisis queda incoherente. (2) Los rangos <code>SARHSLow/Up</code> se leen mejor si el lado derecho quedó <b>numérico</b>; si el modelo tiene la binaria multiplicando dentro de la restricción, conviene <b>reconstruirlo</b> pasando $y^*$ como número en vez de usar <code>m.fixed()</code>.</div>
</section>

<section id="trampas">
  <h3>10. Diez trampas clásicas</h3>
  <table>
    <tr><th>#</th><th class="l">Trampa</th><th class="l">Lo correcto</th></tr>
    <tr><td>1</td><td class="l">Multiplicar $\pi_i$ por un $\Delta$ que se sale del rango</td><td class="l">Multiplicar solo hasta el borde del rango; más allá, <b>volver a resolver</b></td></tr>
    <tr><td>2</td><td class="l">Creer que $\pi_i=0$ significa "recurso inútil"</td><td class="l">Significa "recurso <b>que sobra hoy</b>". Si se reduce mucho, pasa a valer</td></tr>
    <tr><td>3</td><td class="l">Reportar $\pi_i$ sin unidad</td><td class="l">Siempre \$/hora, \$/m³, \$/tonelada...</td></tr>
    <tr><td>4</td><td class="l">Confundir el rango de $b_i$ con el rango de $x_j$</td><td class="l">El rango de $b_i$ dice hasta dónde vale $\pi_i$, no cuánto se produce</td></tr>
    <tr><td>5</td><td class="l">Pensar que dentro del rango "no cambia nada"</td><td class="l">En el rango de $b_i$: <b>cambian las $x_j$</b>, no la base. En el rango de $c_j$: <b>cambia $z^*$</b>, no las $x_j$</td></tr>
    <tr><td>6</td><td class="l">Pedirle duales a un MIP</td><td class="l">Fijar las enteras, verificar <code>IsMIP=0</code> y recién ahí leer <code>.Pi</code></td></tr>
    <tr><td>7</td><td class="l">Asumir $\pi_i\ge0$ siempre</td><td class="l">Las $\ge$ activas en un máximo dan $\pi_i&lt;0$ (Ejemplo 4)</td></tr>
    <tr><td>8</td><td class="l">Ignorar la <b>degeneración</b></td><td class="l">Con un vértice degenerado hay <b>dos</b> precios sombra (izquierdo y derecho) — ver abajo</td></tr>
    <tr><td>9</td><td class="l">Ignorar los <b>óptimos alternativos</b></td><td class="l">Si una no básica tiene $rc_j=0$, hay otra solución con el mismo $z^*$; el dual reportado es <b>uno</b> de varios</td></tr>
    <tr><td>10</td><td class="l">Cambiar varios parámetros y usar los rangos individuales</td><td class="l">Aplicar la <b>regla del 100 %</b>, y si se pasa de 1, resolver de nuevo</td></tr>
  </table>

  <h4>La degeneración con lupa</h4>
  <p>Un vértice es <b>degenerado</b> cuando hay más restricciones activas que variables. Ahí $z^*(b)$ tiene un <b>quiebre justo en el punto actual</b> y la derivada por la izquierda no coincide con la derivada por la derecha:</p>
  """ + img("degen", "$\\max\\,x_1+x_2$ con $x_1\\le4$, $x_2\\le4$, $x_1+x_2\\le8$: tres restricciones activas en $(4,4)$.") + r"""
  <div class="tip"><b>Qué reporta el software.</b> Para este modelo Gurobi entrega $\pi_1=1$ con rango $[0\,;\,4]$: el <b>límite superior del rango coincide con el valor actual</b> de $b_1$. Esa es la señal de alarma de degeneración. La lectura honesta es: <b>quitar</b> una unidad de $b_1$ cuesta 1, pero <b>agregar</b> una unidad no aporta nada, porque $x_1+x_2\le8$ ya está tope. Un rango de longitud cero por algún lado ⟹ <b>desconfíe y verifique resolviendo</b>.</div>
</section>
"""

CHEAT = r"""
<h2 class="part" id="p5">Bloque V — Resumen y práctica</h2>

<section id="cheat">
  <h3>Cheat-sheet</h3>
  <div class="grid2">
    <div>
      <h4>Definiciones</h4>
      $$\pi_i=\frac{\partial z^*}{\partial b_i}=y_i^*\qquad rc_j = c_j - y^{*\top}A_j$$
      $$y^{*\top}=c_B^\top B^{-1}\qquad x_B=B^{-1}b\qquad z^*=c_B^\top B^{-1}b$$
      <h4>Dualidad</h4>
      $$\max\{c^\top x: Ax\le b, x\ge0\}\;\longleftrightarrow\;\min\{b^\top y: A^\top y\ge c, y\ge0\}$$
      $$\text{débil: } c^\top x\le b^\top y \qquad \text{fuerte: } c^\top x^* = b^\top y^*$$
      <h4>Holgura complementaria</h4>
      $$\pi_i s_i = 0 \qquad x_j\,rc_j = 0$$
    </div>
    <div>
      <h4>Rangos</h4>
      $$b_i:\;\; x_B^* + \Delta B^{-1}e_i \ge 0 \;\;\Rightarrow\;\; \Delta\in[\Delta^-,\Delta^+]$$
      $$z^*(b_i+\Delta)=z^*+\pi_i\Delta \quad\text{(dentro del rango)}$$
      $$c_j:\;\; rc_k \le 0\;\;\forall k \text{ no básica}$$
      $$z^*(c_j+\delta)=z^*+\delta\,x_j^* \quad\text{(dentro del rango)}$$
      <h4>Formas de $z^*$</h4>
      <table style="font-size:.88rem">
        <tr><th></th><th>en máx</th><th>pendiente</th></tr>
        <tr><td class="l">$z^*(b_i)$</td><td>cóncava</td><td>$\pi_i$</td></tr>
        <tr><td class="l">$z^*(c_j)$</td><td>convexa</td><td>$x_j^*$</td></tr>
        <tr><td class="l">MIP $z^*(b)$</td><td><b>ninguna</b></td><td>—</td></tr>
      </table>
    </div>
  </div>
  <h4>Los cinco chequeos antes de entregar</h4>
  <ol>
    <li>$\sum_i \pi_i b_i = z^*$ (dualidad fuerte).</li>
    <li>Toda restricción con holgura tiene $\pi_i=0$.</li>
    <li>Toda variable positiva tiene $rc_j=0$.</li>
    <li>Los signos de $\pi_i$ respetan la tabla de la sección 2.</li>
    <li>Cada $\pi_i$ que se reporte lleva <b>unidad</b> y su <b>rango de validez</b>.</li>
  </ol>
</section>

<section id="prac">
  <h3>Ejercicios propuestos</h3>

  <h4>P1 — Panadería (precios sombra y decisión)</h4>
  <p>Una panadería produce <b>hallullas</b> ($x_1$) y <b>marraquetas</b> ($x_2$), en cientos de unidades.</p>
  $$\max\;24x_1+18x_2\quad\text{s.a.}\quad 3x_1+2x_2\le240\;(\text{harina}),\;\;2x_1+3x_2\le210\;(\text{horno}),\;\;x_1+x_2\le100\;(\text{personal})$$
  <p><b>a)</b> Resuelva gráficamente. <b>b)</b> Obtenga los tres precios sombra usando holgura complementaria. <b>c)</b> Un proveedor ofrece 30 sacos extra de harina a 5 mil c/u, ¿conviene? <b>d)</b> ¿Y contratar 20 horas más de personal?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Activas harina y horno: $3x_1+2x_2=240$, $2x_1+3x_2=210$ ⟹ $x^*=(60,\,30)$, $z^*=24(60)+18(30)=\mathbf{1980}$. Personal: $90\le100$, holgura 10.</p>
  <p><b>b)</b> $y_3=0$ por holgura complementaria. Ambas variables positivas ⟹ dos igualdades duales: $3y_1+2y_2=24$ y $2y_1+3y_2=18$. Resolviendo: $\boxed{y^*=(7{,}2;\;1{,}2;\;0)}$. Chequeo: $240(7{,}2)+210(1{,}2)=1728+252=1980$ ✓.</p>
  <p><b>c)</b> El rango de la harina es $[140\,;\,290]$, así que los 30 sacos caben enteros. Ganancia: $30\times7{,}2=216$; costo: $30\times5=150$. <b>Conviene</b>, gana 66 mil netos.</p>
  <p><b>d)</b> <b>No</b>: al personal le sobran 10 horas, $\pi_3=0$. Pagar por más horas es pérdida pura.</p>
  </details>

  <h4>P2 — Mueblería con contrato (precio sombra negativo)</h4>
  $$\max\;50x_1+80x_2+60x_3$$
  $$4x_1+6x_2+5x_3\le600\;(\text{corte}),\qquad 2x_1+4x_2+3x_3\le320\;(\text{armado}),\qquad x_2\ge40\;(\text{contrato})$$
  <p>El óptimo es $x^*=(80,\,40,\,0)$ con $z^*=7200$. <b>a)</b> ¿Cuáles restricciones están activas? <b>b)</b> Calcule los tres precios sombra. <b>c)</b> Interprete el signo del dual del contrato. <b>d)</b> ¿A cuánto tendría que subir el precio de $x_3$ para que convenga producirlo?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Corte: $320+240=560\le600$, <b>holgura 40</b> ⟹ $\pi_{\text{corte}}=0$. Armado: $160+160=320$, <b>activa</b>. Contrato: $x_2=40$, <b>activa</b>.</p>
  <p><b>b)</b> $x_1&gt;0$ y $\pi_{\text{corte}}=0$ ⟹ $2\pi_{\text{arm}}=50$ ⟹ $\pi_{\text{arm}}=25$. Para $x_2$: $4(25)+\pi_{\text{contr}}=80$ ⟹ $\boxed{\pi_{\text{contr}}=-20}$. Chequeo: $600(0)+320(25)+40(-20)=8000-800=7200$ ✓.</p>
  <p><b>c)</b> Cada unidad de $x_2$ que el contrato obliga a fabricar <b>destruye 20</b> de utilidad: consume 4 horas de armado (valen 100) y solo aporta 80. La empresa debería pagar hasta 20 por unidad para que la liberen del compromiso.</p>
  <p><b>d)</b> $rc_3 = 60-(5\cdot0+3\cdot25)=60-75=-15$. Hay que subir el precio a $\mathbf{75}$.</p>
  </details>

  <h4>P3 — Rangos y regla del 100 %</h4>
  <p>Vuelva al Ejemplo 1 (conservera). Los rangos son: $b_1\in[67{,}5;90]$, $b_3\in[40;48{,}57]$, $c_1\in[20;40]$, $c_2\in[30;60]$.</p>
  <p><b>a)</b> Si $b_1$ sube a 85 y $b_3$ baja a 43, ¿se puede usar la regla del 100 %? ¿Cuál es el nuevo $z^*$? <b>b)</b> Si $c_1$ baja a 25 y $c_2$ sube a 45, ¿cambia el plan de producción? ¿Cuál es el nuevo $z^*$?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> $b_1$: $+5$ de un permitido de $+10$ ⟹ 50 %. $b_3$: $-2$ de un permitido de $-5$ ⟹ 40 %. Total <b>90 % ≤ 100 %</b>: la base aguanta. $z^* = 1700 + 10(5) + 20(-2) = 1700+50-40=\mathbf{1710}$.</p>
  <p><b>b)</b> $c_1$: $-5$ de un permitido de $-10$ ⟹ 50 %. $c_2$: $+5$ de un permitido de $+20$ ⟹ 25 %. Total <b>75 %</b>: el plan <b>no cambia</b>, sigue $x^*=(10,35)$. Nuevo $z^* = 25(10)+45(35)=250+1575=\mathbf{1825}$.</p>
  </details>

  <h4>P4 — Holgura complementaria pura (estilo certamen)</h4>
  $$\max\;6x_1+4x_2+3x_3+5x_4+2x_5$$
  $$4x_1+2x_2+2x_3+3x_4+x_5\le30,\qquad 3x_1+x_2+5x_3+2x_4+2x_5\ge25$$
  <p>Se sabe que la solución óptima del <b>dual</b> es $y^*=(2,\,0)$. <b>a)</b> Encuentre $z^*$ sin resolver el primal. <b>b)</b> Encuentre una solución óptima primal. <b>c)</b> ¿Es única?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Por dualidad fuerte, $z^* = b^\top y^* = 30(2)+25(0)=\mathbf{60}$.</p>
  <p><b>b)</b> Como $y_2=0$ y $y_1=2&gt;0$, la primera restricción es <b>activa</b>. Calculamos los costos reducidos $rc_j=c_j-2a_{1j}$:</p>
  <table><tr><th>$j$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
  <tr><th>$c_j$</th><td>6</td><td>4</td><td>3</td><td>5</td><td>2</td></tr>
  <tr><th>$2a_{1j}$</th><td>8</td><td>4</td><td>4</td><td>6</td><td>2</td></tr>
  <tr><th>$rc_j$</th><td><b>−2</b></td><td>0</td><td><b>−1</b></td><td><b>−1</b></td><td>0</td></tr></table>
  <p>Los $rc_j&lt;0$ fuerzan $x_1=x_3=x_4=0$. Quedan $x_2,x_5$ con $2x_2+x_5=30$, y hay que respetar la segunda: $x_2+2x_5\ge25$. Dos soluciones válidas: $x=(0,0,0,0,30)$ con $2(30)=60\ge25$ ✓, o $x=(0,\tfrac{35}{3},0,0,\tfrac{20}{3})$. Ambas dan $z=60$.</p>
  <p><b>c)</b> <b>No es única.</b> Dos variables tienen $rc_j=0$ ($x_2$ y $x_5$), lo que es exactamente la señal de <b>óptimos alternativos</b>: todo el segmento entre las dos soluciones anteriores es óptimo. Ojo con esto en el certamen: si su respuesta no coincide con la pauta pero $z^*$ sí, revise si son óptimos alternativos.</p>
  </details>

  <h4>P5 — El MIP tramposo</h4>
  <p>Una planta tiene capacidad de 10 unidades y puede <b>habilitar un turno extra</b> de 15 unidades pagando un fijo de 20. Los productos rinden 8 y 6, y hay un recurso escaso $b$:</p>
  $$\max\;8x_1+6x_2-20y\quad\text{s.a.}\quad x_1+x_2\le10+15y,\quad 2x_1+x_2\le b,\quad y\in\{0,1\}$$
  <p>Con $b=12$ el óptimo es $x^*=(2,\,8)$ con $y^*=0$ y $z^*=64$, y el LP con la binaria fija reporta $\pi=2$ para el recurso, con validez hasta $b=20$. <b>a)</b> ¿Por qué no se puede pedir <code>.Pi</code> directamente al MIP? <b>b)</b> Usando el precio sombra, estime $z^*$ para $b=20$. <b>c)</b> El valor real es 100. ¿Por qué falló la estimación, y por qué falló <i>hacia abajo</i>? <b>d)</b> ¿Cómo se contesta bien?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Porque un MIP se resuelve por <i>branch and bound</i>, no por Simplex: no hay base óptima ni tableau del cual leer duales. Gurobi devuelve error al pedir <code>.Pi</code> si <code>IsMIP=1</code>.</p>
  <p><b>b)</b> $64 + 2\,(20-12) = \mathbf{80}$.</p>
  <p><b>c)</b> Porque el precio sombra del LP con $y=0$ describe el sistema <b>con el turno extra apagado</b>, y $\pi=2$ es correcto <i>solo</i> mientras $y^*$ siga siendo 0. En $b=15$ al modelo le conviene <b>encender el turno</b>: salta a la curva de $y=1$, cuya pendiente es <b>6</b>. Como $z^*(b)$ es el <b>máximo</b> de dos funciones cóncavas, en el cruce hay un quiebre <b>hacia arriba</b> y la extrapolación queda <b>corta</b>. En un LP puro esto no puede pasar: $z^*(b)$ es cóncava y la extrapolación siempre <b>sobreestima</b>.</p>
  <p><b>d)</b> Resolviendo los dos MIP —con $b=12$ y con $b=20$— y restando los valores objetivo. Para decisiones discretas <b>no hay atajo dual</b>.</p>
  </details>
</section>

<footer>
  <b>IIP314W-2 · Optimización Aplicada a Negocios · 2026-T2</b><br>
  Universidad del Desarrollo · Profesor Rodrigo Trigo Vilches · Ayudante Vicente Ramírez<br>
  Recurso de estudio — Precios sombra y análisis de sensibilidad
</footer>
</body>
</html>
"""

HTML = HEAD + P1 + P2 + E1 + E2 + E3 + E4 + E5 + E6 + GUR + CHEAT

OUT = r"C:\Users\raalv\__Ayudantía Opti Inf\2026-T2\Recursos\Recurso_Precios_Sombra_Sensibilidad.html"
HTML, _informe = postproceso(HTML)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("escrito:", OUT, len(HTML) // 1024, "KB")
