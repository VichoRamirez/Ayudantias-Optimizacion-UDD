# -*- coding: utf-8 -*-
"""Genera el Recurso HTML de Simplex: Tableau y Matricial (IIP314W, 2026-T2)."""
import io, os, base64, sys
import numpy as np
from numpy.linalg import inv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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
NARANJA = "#c47f17"
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
    X, Y = np.meshgrid(np.linspace(*xlim, n), np.linspace(*ylim, n))
    m = (X >= 0) & (Y >= 0)
    for a, bb, c, s in cons:
        m &= (a * X + bb * Y <= c) if s == "<" else (a * X + bb * Y >= c)
    ax.contourf(X, Y, m.astype(float), levels=[.5, 1.5], colors=[color], alpha=alpha)


# =====================================================================
# F1 — el camino del Simplex, en los dos ejemplos
# =====================================================================
def fig_camino():
    fig, axs = plt.subplots(1, 2, figsize=(12.8, 5.2))

    # (a) COMPUTADORES: max 500x1+300x2 ; 4x1+2x2<=12 ; 4x1+x2<=10 ; x1+x2<=4
    ax = axs[0]
    x = np.linspace(0, 6, 400)
    region(ax, [(4, 2, 12, "<"), (4, 1, 10, "<"), (1, 1, 4, "<")], (0, 6), (0, 6))
    ax.plot(x, (12 - 4 * x) / 2, color=AZUL, lw=2.2, label=r"inversión: $4x_1+2x_2\leq12$")
    ax.plot(x, 10 - 4 * x, color=ACC, lw=2.2, label=r"horas: $4x_1+x_2\leq10$")
    ax.plot(x, 4 - x, color=VERDE, lw=2.2, label=r"mostrador: $x_1+x_2\leq4$")
    cam = [(0, 0), (2.5, 0), (2, 2)]
    for i in range(len(cam) - 1):
        ax.annotate("", xy=cam[i + 1], xytext=cam[i],
                    arrowprops=dict(arrowstyle="-|>", color="#111", lw=2.4,
                                    shrinkA=9, shrinkB=9))
    for (px, py), lab, off in zip(cam,
                                  [r"$\{s_1,s_2,s_3\}$" "\n" r"$z=0$",
                                   r"$\{s_1,x_1,s_3\}$" "\n" r"$z=1250$",
                                   r"$\{s_1,x_1,x_2\}$" "\n" r"$z=1600$"],
                                  [(-6, 16), (10, 14), (16, 12)]):
        ax.plot(px, py, "o", color="#111", ms=9, zorder=6)
        ax.annotate(lab, (px, py), textcoords="offset points", xytext=off, fontsize=8.6,
                    fontweight="bold",
                    bbox=dict(fc="white", ec="#888", alpha=.92, boxstyle="round,pad=.25"))
    ax.annotate("las TRES rectas pasan por $(2,2)$\n→ vértice DEGENERADO ($s_1=0$ básica)",
                xy=(2.05, 2.05), xytext=(2.28, 4.55), fontsize=8.8, color=NARANJA,
                fontweight="bold",
                bbox=dict(fc="white", ec=NARANJA, alpha=.95, boxstyle="round,pad=.28"),
                arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.5))
    ax.set_xlim(0, 4.4); ax.set_ylim(0, 5.6)
    ax.set_xlabel(r"$x_1$ — computador A"); ax.set_ylabel(r"$x_2$ — computador B")
    ax.set_title("(a) Computadores (Clases 17 y 18)", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.4, loc="upper left")

    # (b) CERVECERIA: max 30x1+50x2 ; x1+2x2<=16 ; x1+x2<=9 ; 3x1+2x2<=24
    ax = axs[1]
    x = np.linspace(0, 12, 400)
    region(ax, [(1, 2, 16, "<"), (1, 1, 9, "<"), (3, 2, 24, "<")], (0, 12), (0, 12))
    ax.plot(x, (16 - x) / 2, color=AZUL, lw=2.2, label=r"malta: $x_1+2x_2\leq16$")
    ax.plot(x, 9 - x, color=ACC, lw=2.2, label=r"fermentación: $x_1+x_2\leq9$")
    ax.plot(x, (24 - 3 * x) / 2, color=VERDE, lw=2.2, label=r"embotellado: $3x_1+2x_2\leq24$")
    cam = [(0, 0), (0, 8), (2, 7)]
    for i in range(len(cam) - 1):
        ax.annotate("", xy=cam[i + 1], xytext=cam[i],
                    arrowprops=dict(arrowstyle="-|>", color="#111", lw=2.4,
                                    shrinkA=9, shrinkB=9))
    for (px, py), lab, off in zip(cam,
                                  [r"$\{s_1,s_2,s_3\}$" "\n" r"$z=0$",
                                   r"$\{x_2,s_2,s_3\}$" "\n" r"$z=400$",
                                   r"$\{x_2,x_1,s_3\}$" "\n" r"$z=410$"],
                                  [(12, 8), (12, 10), (30, 20)]):
        ax.plot(px, py, "o", color="#111", ms=9, zorder=6)
        ax.annotate(lab, (px, py), textcoords="offset points", xytext=off, fontsize=8.6,
                    fontweight="bold",
                    bbox=dict(fc="white", ec="#888", alpha=.92, boxstyle="round,pad=.25"))
    ax.annotate("el embotellado nunca aprieta:\n$s_3=4$ se queda en la base",
                xy=(5.4, 3.9), xytext=(4.15, 5.15), fontsize=8.8, color=VERDE, fontweight="bold",
                bbox=dict(fc="white", ec=VERDE, alpha=.95, boxstyle="round,pad=.28"),
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=1.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xlabel(r"$x_1$ — Golden Ale (barriles)"); ax.set_ylabel(r"$x_2$ — Doble IPA")
    ax.set_title("(b) Cervecería Los Andes (Ayudantía 6)", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.4, loc="upper right")

    fig.suptitle("El Simplex camina por los VÉRTICES: cada base es una esquina de la región",
                 fontsize=12.5, fontweight="bold", color=AZUL, y=1.02)
    fig.tight_layout()
    return b64(fig)


IMG["camino"] = fig_camino()


# =====================================================================
# F2 — anatomia del tableau optimo
# =====================================================================
def fig_anatomia():
    filas = [["CR", "0", "0", "20", "10", "0", "410"],
             ["$x_2$", "0", "1", "1", "-1", "0", "7"],
             ["$x_1$", "1", "0", "-1", "2", "0", "2"],
             ["$s_3$", "0", "0", "1", "-4", "1", "4"]]
    cab = ["Base", "$x_1$", "$x_2$", "$s_1$", "$s_2$", "$s_3$", "RHS"]
    nc, nf = 7, 5
    W, H = 1.0, 0.62
    fig, ax = plt.subplots(figsize=(12.2, 6.4))
    ax.set_xlim(-2.3, nc * W + 3.6); ax.set_ylim(-2.5, nf * H + 1.7)
    ax.axis("off")

    def xy(i, j):          # i = fila (0 = cabecera), j = columna
        return j * W, (nf - 1 - i) * H

    # bloques de color
    ax.add_patch(Rectangle((xy(1, 1)[0], xy(1, 1)[1]), 2 * W, H, fc="#fdf0d5", ec="none"))
    ax.add_patch(Rectangle((xy(1, 3)[0], xy(1, 3)[1]), 3 * W, H, fc="#fdeaf1", ec="none"))
    ax.add_patch(Rectangle((xy(2, 3)[0], xy(4, 3)[1]), 3 * W, 3 * H, fc="#e7f0f7", ec="none"))
    ax.add_patch(Rectangle((xy(2, 6)[0], xy(4, 6)[1]), W, 3 * H, fc="#e8f5ec", ec="none"))
    ax.add_patch(Rectangle((xy(1, 6)[0], xy(1, 6)[1]), W, H, fc="#e2d9f3", ec="none"))

    for j, txt in enumerate(cab):
        x0, y0 = xy(0, j)
        ax.add_patch(Rectangle((x0, y0), W, H, fc=AZUL, ec="white", lw=1.4))
        ax.text(x0 + W / 2, y0 + H / 2, txt, ha="center", va="center",
                color="white", fontweight="bold", fontsize=11)
    for i, fila in enumerate(filas, start=1):
        for j, txt in enumerate(fila):
            x0, y0 = xy(i, j)
            ax.add_patch(Rectangle((x0, y0), W, H, fc="none", ec="#b9c7d4", lw=1.1))
            ax.text(x0 + W / 2, y0 + H / 2, txt, ha="center", va="center", fontsize=11,
                    fontweight="bold" if j == 0 or i == 1 else "normal")

    def flecha(txt, celda, dest, color, fs=9.4, ha="left"):
        i, j = celda
        x0, y0 = xy(i, j)
        ax.annotate(txt, xy=(x0 + W / 2, y0 + H / 2), xytext=dest, fontsize=fs, color=color,
                    fontweight="bold", ha=ha, va="center",
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.6))

    flecha("costos reducidos de las NO básicas\n(todos $\\geq0$ ⟹ ÓPTIMO)",
           (1, 1), (-2.2, nf * H + 0.35), NARANJA)
    ax.annotate("fila CR bajo las HOLGURAS = los PRECIOS SOMBRA  $y^*=(20,10,0)$",
                xy=(xy(1, 4)[0] + W / 2, xy(1, 4)[1] + H), xytext=(3.9, nf * H + 1.05),
                fontsize=9.4, color=ACC, fontweight="bold", ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=ACC, lw=1.6))
    flecha("las columnas de las holguras iniciales\nSON la matriz $B^{-1}$",
           (3, 4), (nc * W + 0.35, 2.0 * H), AZUL2)
    flecha("columna RHS = $x_B=B^{-1}b$\n$x_2=7,\\;x_1=2,\\;s_3=4$",
           (2, 6), (nc * W + 0.35, 0.35 * H), VERDE)
    flecha("celda objetivo = $z^*=410$", (1, 6), (nc * W + 0.35, nf * H + 0.35), "#5b3fa0")
    ax.annotate("la columna de una variable BÁSICA\nes siempre un vector de la identidad",
                xy=(xy(3, 1)[0] + W / 2, xy(3, 1)[1] + H / 2), xytext=(-2.2, -1.15),
                fontsize=9.4, color="#111", fontweight="bold", ha="left",
                arrowprops=dict(arrowstyle="->", color="#111", lw=1.6))
    ax.annotate("$s_3$ sigue en la base con valor 4:\nal embotellado le sobran 4 horas",
                xy=(xy(4, 0)[0] + W / 2, xy(4, 0)[1] + H / 2), xytext=(1.15, -2.05),
                fontsize=9.4, color=VERDE, fontweight="bold", ha="left",
                arrowprops=dict(arrowstyle="->", color=VERDE, lw=1.6))
    ax.set_title("Anatomía del tableau óptimo — Cervecería Los Andes",
                 color=AZUL, fontweight="bold", fontsize=13, pad=26)
    return b64(fig)


IMG["anatomia"] = fig_anatomia()


# =====================================================================
# F3 — casos especiales
# =====================================================================
def fig_especiales():
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.9))

    ax = axs[0]
    x = np.linspace(0, 12, 400)
    region(ax, [(-1, 1, 1, "<"), (1, -1, 1, "<")], (0, 12), (0, 12))
    ax.plot(x, x + 1, color=AZUL, lw=2.2, label=r"$-x_1+x_2\leq1$")
    ax.plot(x, x - 1, color=ACC, lw=2.2, label=r"$x_1-x_2\leq1$")
    ax.annotate("", xy=(9.3, 9.3), xytext=(2.3, 2.3),
                arrowprops=dict(arrowstyle="-|>", color="#111", lw=2.6))
    ax.text(3.0, 6.6, r"$z\to+\infty$", fontsize=13, fontweight="bold", color="#111")
    ax.text(.4, 9.4, "en el tableau: la columna que\nentra NO tiene ningún elemento\npositivo "
                     "⟹ no hay razón mínima\n⟹ NO ACOTADO",
            fontsize=9.2, color=NARANJA, fontweight="bold", va="top",
            bbox=dict(fc="white", ec=NARANJA, alpha=.92, boxstyle="round,pad=.35"))
    ax.set_xlim(0, 11); ax.set_ylim(0, 11)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(a) No acotado: $\max\,x_1+x_2$", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")

    ax = axs[1]
    x = np.linspace(0, 6, 400)
    region(ax, [(1, 1, 4, "<"), (1, 0, 3, "<"), (0, 1, 3, "<")], (0, 6), (0, 6))
    ax.plot(x, 4 - x, color=AZUL, lw=2.2, label=r"$x_1+x_2\leq4$")
    ax.axvline(3, color=ACC, lw=2.2, label=r"$x_1\leq3$")
    ax.axhline(3, color=VERDE, lw=2.2, label=r"$x_2\leq3$")
    ax.plot([1, 3], [3, 1], color="#111", lw=6, alpha=.45, solid_capstyle="round")
    ax.plot([1, 3], [3, 1], "o", color="#111", ms=10, zorder=6)
    ax.text(1.35, 1.85, "TODO el segmento\nes óptimo, $z=8$", fontsize=10, fontweight="bold",
            color="#111", rotation=-45, rotation_mode="anchor")
    ax.text(3.35, 4.3, "en el tableau: una variable\nNO básica con $CR=0$\n"
                       "⟹ ÓPTIMOS ALTERNATIVOS",
            fontsize=9.2, color=NARANJA, fontweight="bold", va="top",
            bbox=dict(fc="white", ec=NARANJA, alpha=.92, boxstyle="round,pad=.35"))
    ax.set_xlim(0, 5.6); ax.set_ylim(0, 5.6)
    ax.set_xlabel(r"$x_1$"); ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(b) Óptimos alternativos: $\max\,2x_1+2x_2$", color=AZUL, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")
    fig.tight_layout()
    return b64(fig)


IMG["especiales"] = fig_especiales()


# =====================================================================
# F4 — refinerias: primal de minimo con >= (no hay base factible obvia)
# =====================================================================
def fig_refinerias():
    fig, ax = plt.subplots(figsize=(7.8, 5.8))
    x = np.linspace(0, 170, 600)
    region(ax, [(4, 3, 250, ">"), (3, 4, 270, ">"), (2, 5, 300, ">")],
           (0, 170), (0, 130), color="#cfe3f2")
    ax.plot(x, (250 - 4 * x) / 3, color=AZUL, lw=2.2, label=r"alto: $4x_1+3x_2\geq250$")
    ax.plot(x, (270 - 3 * x) / 4, color=ACC, lw=2.2, label=r"medio: $3x_1+4x_2\geq270$")
    ax.plot(x, (300 - 2 * x) / 5, color=VERDE, lw=2.2, label=r"bajo: $2x_1+5x_2\geq300$")
    for z, st in [(2600, ":"), (2100, ":"), (1625, "-")]:
        ax.plot(x, (z - 25 * x) / 20, color="#333", ls=st, lw=1.9 if z == 1625 else 1.1,
                label=(r"$z=1625$ (óptimo)" if z == 1625 else None))
    ax.plot(25, 50, "o", color="#111", ms=10, zorder=6)
    ax.annotate(r"$x^*=(25,\,50)$,  $z^*=1625$", (25, 50), textcoords="offset points",
                xytext=(34, 34), fontsize=10.5, fontweight="bold",
                bbox=dict(fc="white", ec="#111", alpha=.95, boxstyle="round,pad=.3"),
                arrowprops=dict(arrowstyle="->", color="#111"))
    ax.plot(150, 0, "s", color=NARANJA, ms=9, zorder=6)
    MOR = "#5b3fa0"
    ax.plot(0, 0, "X", color=MOR, ms=13, zorder=7)
    ax.annotate("EL ORIGEN NO ES FACTIBLE\n⟹ hacen falta ARTIFICIALES",
                xy=(1.5, 1.5), xytext=(9, 22), fontsize=9.4, color=MOR, fontweight="bold",
                va="bottom",
                bbox=dict(fc="white", ec=MOR, alpha=.96, boxstyle="round,pad=.3"),
                arrowprops=dict(arrowstyle="->", color=MOR, lw=1.8))
    ax.annotate("base factible del enunciado:\nsolo refinería 1, 150 días", xy=(148, 1.5),
                xytext=(88, 11), fontsize=9, color=NARANJA, fontweight="bold", ha="center",
                bbox=dict(fc="white", ec=NARANJA, alpha=.96, boxstyle="round,pad=.28"),
                arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.4))
    ax.set_xlim(0, 165); ax.set_ylim(0, 125)
    ax.set_xlabel(r"$x_1$ — días de la refinería 1"); ax.set_ylabel(r"$x_2$ — días de la refinería 2")
    ax.set_title("Refinerías: un mínimo con restricciones $\\geq$", color=AZUL, fontweight="bold")
    ax.legend(fontsize=8.8, loc="upper right")
    return b64(fig)


IMG["refinerias"] = fig_refinerias()

print("figuras listas:", {k: len(v) // 1024 for k, v in IMG.items()}, "KB")

# =====================================================================
#                               HTML
# =====================================================================
HEAD = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Recurso de estudio — Simplex Tableau y Matricial | IIP314W UDD</title>
__ASSETS__
<style>
:root{--azul:#0b3d62;--azul2:#1f5f8b;--acc:#d6336c;--verde:#2b8a3e;--nar:#c47f17;--bg:#f6f8fb;--card:#fff;--mut:#5b6b7b;}
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
.warn{border-left:4px solid var(--nar);background:#fdf6e7;padding:10px 14px;border-radius:0 8px 8px 0;margin:14px 0}
.warn b{color:var(--nar)}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.93rem}
th,td{border:1px solid #d8e2ec;padding:7px 10px;text-align:center}
th{background:var(--azul);color:#fff}
tr:nth-child(even) td{background:#f4f8fb}
td.l,th.l{text-align:left}
table.tab td{font-family:Consolas,monospace}
table.tab tr:nth-child(even) td{background:#fff}
td.cr{background:#fdf0d5 !important;font-weight:600}
td.piv{background:#ffe0e9 !important;font-weight:700;color:#a01746}
td.ent{background:#e2d9f3 !important}
td.bas{background:#e8f5ec !important}
pre{border-radius:10px;overflow:auto;font-size:.85rem;margin:12px 0}
code{font-family:"SFMono-Regular",Consolas,Menlo,monospace}
p code,li code,td code{background:#eef2f6;color:#b5266b;padding:1px 5px;border-radius:4px;font-size:.9em}
img.plot{display:block;max-width:100%;height:auto;margin:14px auto;border:1px solid #e7edf3;border-radius:8px}
.muted{color:var(--mut);font-size:.9rem}
details{margin:8px 0;background:#f4f8fb;border:1px solid #dde7f0;border-radius:8px;padding:6px 12px}
summary{cursor:pointer;font-weight:600;color:var(--azul2)}
footer{text-align:center;color:var(--mut);font-size:.85rem;padding:30px 18px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.scroll{overflow-x:auto}
@media(max-width:680px){nav.toc ol{columns:1}.grid2{grid-template-columns:1fr}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="badge" style="background:rgba(255,255,255,.2);color:#fff">IIP314W-2 · 2026-T2</div>
    <h1>Recurso de estudio — Método Simplex: Tableau y Matricial</h1>
    <div class="sub">Forma estándar, bases y vértices, el algoritmo en sus dos formas, cómo leer un tableau y qué hacer cuando hay restricciones $\geq$</div>
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
    <li><a href="#s1">1. Forma estándar</a></li>
    <li><a href="#s2">2. Bases, vértices y el teorema fundamental</a></li>
    <li><a href="#s3">3. Las tres convenciones de signo</a></li>
    <li><a href="#s4">4. Anatomía del tableau</a></li>
    <li><a href="#s5">5. El algoritmo, paso a paso</a></li>
    <li><a href="#s6">6. Las cinco fórmulas matriciales</a></li>
    <li><a href="#s7">7. El cruce: dónde vive $B^{-1}$</a></li>
    <li><a href="#s8">8. Casos especiales</a></li>
    <li><a href="#s9">9. Restricciones $\geq$: artificiales, Gran M y dos fases</a></li>
    <li><a href="#x1">Ej. 1 — Computadores: tableau y matricial</a></li>
    <li><a href="#x2">Ej. 2 — Cervecería: la otra convención</a></li>
    <li><a href="#x3">Ej. 3 — Completar un tableau</a></li>
    <li><a href="#x4">Ej. 4 — Refinerías: un mínimo con $\geq$</a></li>
    <li><a href="#x5">Ej. 5 — Contar y elegir bases</a></li>
    <li><a href="#gur">10. Código: el Simplex en numpy</a></li>
    <li><a href="#trampas">11. Doce trampas clásicas</a></li>
    <li><a href="#cheat">Resumen / cheat-sheet</a></li>
    <li><a href="#prac">Ejercicios propuestos</a></li>
  </ol>
</nav>

<section id="intro">
  <h3>Cómo usar este recurso</h3>
  <p>El Simplex es el <b>motor</b> que resuelve los programas lineales. La idea de fondo cabe en una frase: <b>el óptimo de un LP siempre está en un vértice</b>, así que basta con ir saltando de vértice en vértice, siempre mejorando, hasta que ninguno de los vecinos sea mejor. Lo que cambia entre la forma <b>tableau</b> y la forma <b>matricial</b> no es el algoritmo — es solo <i>cómo se anotan las cuentas</i>.</p>
  <p>El documento cubre la <b>preparación</b> (secciones 1–3), el <b>tableau</b> (4–5), la <b>forma matricial</b> (6–7), los <b>casos raros</b> (8), las <b>restricciones $\geq$</b> (9), <b>cinco ejemplos resueltos</b> completos, y cierra con código, trampas, cheat-sheet y práctica.</p>
  <div class="warn"><b>Lo primero que hay que ordenar: los signos.</b> En el curso conviven <b>tres convenciones</b> distintas para la fila de costos reducidos —la Clase 17 usa una, la Clase 18 la contraria, y la Ayudantía 6 una tercera. Las tres son correctas y dan el mismo resultado. La <b>sección 3</b> las pone lado a lado y explica cómo traducir entre ellas; conviene leerla antes que nada, porque es de donde salen la mitad de los errores en el certamen.</div>
  <div class="tip"><b>Relación con los otros recursos.</b> El tableau óptimo contiene <b>también</b> la solución del dual y todo el análisis de sensibilidad. Aquí se explica dónde está cada cosa; el uso está en los recursos de <b>Primal y Dual</b> y de <b>Precios sombra y sensibilidad</b>.</div>
</section>
"""

# ---------------------------------------------------------------- Bloque I
B1 = r"""
<h2 class="part" id="p1">Bloque I — Antes de iterar</h2>

<section id="s1">
  <h3>1. Forma estándar</h3>
  <p>El Simplex no sabe trabajar con desigualdades: necesita un <b>sistema de ecuaciones</b> con todas las variables no negativas. Llevar un modelo a esa forma es puramente mecánico.</p>
  <table>
    <tr><th class="l">Si el modelo tiene...</th><th class="l">se hace...</th><th class="l">y queda</th></tr>
    <tr><td class="l">restricción $\;a^\top x\le b$</td><td class="l">sumar una <b>holgura</b> $s\ge0$</td><td class="l">$a^\top x + s = b$</td></tr>
    <tr><td class="l">restricción $\;a^\top x\ge b$</td><td class="l">restar un <b>excedente</b> $h\ge0$</td><td class="l">$a^\top x - h = b$</td></tr>
    <tr><td class="l">restricción $\;a^\top x = b$</td><td class="l">nada (ya es ecuación)</td><td class="l">$a^\top x = b$</td></tr>
    <tr><td class="l">lado derecho $b_i&lt;0$</td><td class="l">multiplicar la fila por $-1$</td><td class="l">(y se <b>da vuelta</b> la desigualdad)</td></tr>
    <tr><td class="l">variable $x_j$ <b>libre</b></td><td class="l">escribir $x_j=x_j^+-x_j^-$</td><td class="l">$x_j^+,x_j^-\ge0$</td></tr>
    <tr><td class="l">variable $x_j\le0$</td><td class="l">sustituir $x_j=-x_j'$</td><td class="l">$x_j'\ge0$</td></tr>
    <tr><td class="l">objetivo de máximo</td><td class="l">$\max\,p^\top x=-\min\,(-p^\top x)$</td><td class="l">$z^*=-w^*$</td></tr>
  </table>
  <div class="key"><b>El punto de las holguras.</b> No son un truco de notación: la holgura $s_i$ <b>es</b> el recurso $i$ que sobra, y su valor en el óptimo se lee directamente en el tableau. Cuando $s_i=0$ la restricción está <b>activa</b>; cuando $s_i&gt;0$, sobra — y su precio sombra es cero.</div>
  <div class="tip"><b>El excedente NO alcanza para armar la base inicial.</b> En $a^\top x - h = b$ el coeficiente de $h$ es $\mathbf{-1}$, no $+1$: esa columna <b>no</b> es un vector de la identidad, así que las $h$ no forman una base factible de partida. Ese es exactamente el problema que resuelven las variables <b>artificiales</b> (sección 9).</div>
</section>

<section id="s2">
  <h3>2. Bases, vértices y el teorema fundamental</h3>
  <p>Después de estandarizar tenemos $Ax=b$ con $A$ de tamaño $m\times n$ y $n&gt;m$: <b>hay más incógnitas que ecuaciones</b>, luego infinitas soluciones. El Simplex se restringe a un subconjunto finito:</p>
  <div class="key"><b>Solución básica.</b> Se eligen $m$ variables (las <b>básicas</b>, cuyas columnas forman una matriz $B$ invertible), se fijan las otras $n-m$ en <b>cero</b> (las <b>no básicas</b>) y se resuelve $x_B=B^{-1}b$. Si además $x_B\ge0$, es una <b>solución básica factible</b> (SBF).</div>
  <table>
    <tr><th class="l">Concepto</th><th class="l">Significado</th></tr>
    <tr><td class="l">Número de bases posibles</td><td class="l">a lo más $\dbinom{n}{m}$ — finito, pero crece muy rápido</td></tr>
    <tr><td class="l">SBF</td><td class="l">$x_B=B^{-1}b\ge0$ ⟹ corresponde a un <b>vértice</b> de la región factible</td></tr>
    <tr><td class="l">Solución básica <b>infactible</b></td><td class="l">$B$ es invertible pero alguna componente de $B^{-1}b$ sale <b>negativa</b>: es una esquina "fuera" de la región</td></tr>
    <tr><td class="l">Base <b>degenerada</b></td><td class="l">alguna variable <b>básica</b> vale $0$ (hay más restricciones activas que variables)</td></tr>
  </table>
  <div class="app"><b>Teorema fundamental de la programación lineal.</b> Si un LP tiene óptimo finito, <b>existe una solución básica factible óptima</b>. Es decir: aunque la región factible tenga infinitos puntos, basta revisar los <b>vértices</b>, que son finitos. El Simplex es un procedimiento inteligente para revisarlos: en vez de enumerarlos todos, salta solo a vecinos que <b>mejoran</b> el objetivo.</div>
  <div class="tip"><b>Por qué no se enumeran todos.</b> Un modelo mediano con $n=50$ y $m=20$ tiene $\binom{50}{20}\approx4{,}7\times10^{13}$ bases. El Simplex típicamente visita del orden de $2m$ a $3m$ — unas pocas decenas. Esa es toda la gracia del método.</div>
</section>

<section id="s3">
  <h3>3. Las tres convenciones de signo (y cómo traducirlas)</h3>
  <div class="warn"><b>Esta sección existe porque en el curso conviven tres formas de escribir la fila CR.</b> Todas llegan al mismo óptimo. Lo que <b>no</b> se puede hacer es mezclarlas a mitad de un ejercicio.</div>
  <div class="scroll">
  <table>
    <tr>
      <th class="l">Convención</th><th class="l">Fila CR</th><th class="l">Entra a la base</th>
      <th class="l">Criterio de parada</th><th class="l">Dónde aparece</th>
    </tr>
    <tr>
      <td class="l"><b>A. Máximo directo</b></td>
      <td class="l">$\bar c_j = c_j - z_j$<br><span class="muted">arranca con los márgenes <b>positivos</b></span></td>
      <td class="l">el <b>más positivo</b></td>
      <td class="l">todos $\le0$</td>
      <td class="l"><b>Clase 17</b></td>
    </tr>
    <tr>
      <td class="l"><b>B. Máximo con signo invertido</b></td>
      <td class="l">$z_j - c_j = c_BB^{-1}A_j-c_j$<br><span class="muted">arranca con los márgenes <b>negativos</b></span></td>
      <td class="l">el <b>más negativo</b></td>
      <td class="l">todos $\ge0$</td>
      <td class="l"><b>Clase 18</b></td>
    </tr>
    <tr>
      <td class="l"><b>C. Convertir a mínimo</b></td>
      <td class="l">$\bar c_j=c_j-z_j$ con $c=-\,$margen<br><span class="muted">se minimiza $w=-z$</span></td>
      <td class="l">el <b>más negativo</b></td>
      <td class="l">todos $\ge0$</td>
      <td class="l"><b>Ayudantía 6</b></td>
    </tr>
  </table>
  </div>
  <div class="key"><b>Las tres son la misma cuenta.</b> B es exactamente A con el signo cambiado. Y C es B disfrazada: al negar los coeficientes de la objetivo ($c=-p$), la expresión $c_j-z_j$ produce los mismos números que $z_j-c_j$ producía con los márgenes originales. Por eso B y C <b>comparten</b> el criterio (entra el más negativo, se para cuando todos son $\ge0$).</div>
  <h4>Cómo no equivocarse nunca</h4>
  <ol>
    <li><b>Declare la convención al empezar</b>, con una línea: <i>"trabajo en forma de minimización, $c=-p$"</i>. En el certamen eso vale puntos.</li>
    <li>Recuerde el <b>sentido</b>, no la fórmula: entra la variable que <b>mejora</b> el objetivo, y se para cuando <b>ninguna</b> lo mejora.</li>
    <li>Al terminar, <b>verifique con el enunciado original</b>: evalúe $p^\top x^*$ a mano. Si el número no coincide con la celda objetivo, hubo un cambio de signo perdido.</li>
    <li>Cuidado con el <b>valor objetivo</b>: en la convención C la celda guarda $w=-z$, así que hay que reportar $z^*=-w^*$. En la Clase 17 la celda muestra $-1600$ para un máximo de $1600$.</li>
  </ol>
  <div class="tip"><b>Y los precios sombra siguen la misma suerte.</b> En la convención A los duales se leen <b>directamente</b> en la fila CR bajo las holguras; en B y C aparecen con el signo cambiado ($-c_BB^{-1}$ contra $c_BB^{-1}$). El chequeo infalible es el de siempre: <b>$\sum_i y_i b_i$ tiene que dar $z^*$</b>. Si da $-z^*$, invierta todos los signos.</div>
</section>
"""

# ---------------------------------------------------------------- Bloque II
B2 = r"""
<h2 class="part" id="p2">Bloque II — El tableau</h2>

<section id="s4">
  <h3>4. Anatomía del tableau</h3>
  <p>Un tableau no es una tabla de números sueltos: <b>cada zona significa algo</b>, y al terminar el algoritmo se pueden leer de ahí la solución, el óptimo, los precios sombra, los costos reducidos y hasta la matriz $B^{-1}$.</p>
  """ + img("anatomia", "Tableau óptimo del Ejemplo 2 (Cervecería Los Andes), con cada zona etiquetada.") + r"""
  <table>
    <tr><th class="l">Zona</th><th class="l">Qué contiene</th></tr>
    <tr><td class="l">Columna "Base"</td><td class="l">qué variable es básica en cada fila</td></tr>
    <tr><td class="l">Fila <b>CR</b></td><td class="l">los costos reducidos $\bar c_j$; deciden si hay que seguir iterando</td></tr>
    <tr><td class="l">Fila CR bajo las <b>holguras iniciales</b></td><td class="l">los <b>precios sombra</b> $y^*$ (salvo signo, según la convención)</td></tr>
    <tr><td class="l">Fila CR, columna RHS</td><td class="l">el <b>valor objetivo</b> de la base actual</td></tr>
    <tr><td class="l">Columna <b>RHS</b> (filas de restricción)</td><td class="l">los valores $x_B=B^{-1}b$ de las variables básicas</td></tr>
    <tr><td class="l">Bloque bajo las <b>holguras iniciales</b></td><td class="l">la matriz $\mathbf{B^{-1}}$, literalmente</td></tr>
    <tr><td class="l">Columna de una variable <b>básica</b></td><td class="l">siempre un vector de la identidad</td></tr>
    <tr><td class="l">Columna de una variable <b>no básica</b></td><td class="l">$B^{-1}A_j$: cómo cambian las básicas si esa variable entra</td></tr>
  </table>
  <div class="app"><b>Una lectura que casi nadie hace.</b> La columna de una no básica $x_j$ dice, entrada por entrada, <b>cuánto baja cada variable básica por cada unidad que entre de $x_j$</b>. Si en la columna de $s_2$ aparece un $2$ en la fila de $x_1$, significa que subir $s_2$ en una unidad <b>reduce</b> $x_1$ en $2$. De ahí sale la prueba del cociente, y de ahí salen los rangos de sensibilidad.</div>
</section>

<section id="s5">
  <h3>5. El algoritmo, paso a paso</h3>
  <p>Escrito en la <b>convención C</b> (minimización), que es la de la Ayudantía 6. Para la convención A, invierta las palabras "negativo" y "positivo".</p>
  <table>
    <tr><th>Paso</th><th class="l">Qué se hace</th><th class="l">Detalle</th></tr>
    <tr><td><b>0</b></td><td class="l">Estandarizar</td><td class="l">holguras, $b\ge0$, base inicial $B=I$ (las holguras), $c=-\,$márgenes si era un máximo</td></tr>
    <tr><td><b>1</b></td><td class="l"><b>Optimalidad</b></td><td class="l">si todos los $\bar c_j\ge0$ ⟹ <b>ÓPTIMO</b>, detenerse</td></tr>
    <tr><td><b>2</b></td><td class="l"><b>Variable que entra</b></td><td class="l">la del $\bar c_j$ <b>más negativo</b> (regla de Dantzig). Su columna es la <b>columna pivote</b></td></tr>
    <tr><td><b>3</b></td><td class="l"><b>Prueba del cociente</b></td><td class="l">$\theta=\min\left\{\dfrac{x_{B_k}}{\bar a_{kj}}\;:\;\bar a_{kj}&gt;0\right\}$ — <b>solo</b> con denominadores positivos. La fila del mínimo es la <b>fila pivote</b> y su variable <b>sale</b></td></tr>
    <tr><td><b>4</b></td><td class="l"><b>Pivoteo</b> (Gauss-Jordan)</td><td class="l">dividir la fila pivote por el elemento pivote, y restar múltiplos de ella al resto (incluida la fila CR) para dejar ceros en la columna pivote</td></tr>
    <tr><td><b>5</b></td><td class="l">Volver al paso 1</td><td class="l">—</td></tr>
  </table>
  <div class="key"><b>Por qué el cociente usa solo denominadores positivos.</b> Al entrar $x_j$ con valor $\theta$, cada básica pasa a valer $x_{B_k}-\theta\,\bar a_{kj}$. Si $\bar a_{kj}\le0$, esa básica <b>crece o se queda igual</b> al aumentar $\theta$: nunca se vuelve negativa, así que no impone límite. Solo las de coeficiente <b>positivo</b> bajan, y la primera que llega a cero define hasta dónde se puede avanzar.</div>
  <div class="tip"><b>El error operativo más frecuente</b> es olvidar aplicar el pivoteo a la <b>fila CR</b>. El tableau queda con la columna pivote "sucia" y a partir de ahí todos los costos reducidos están mal. Chequeo rápido: después de pivotear, <b>la columna de la variable que entró debe ser un vector de la identidad, con $0$ también en la fila CR</b>.</div>
  """ + img("camino", "Cada flecha es una iteración del Simplex, y cada punto es una base. El algoritmo nunca entra al interior de la región: salta de vértice en vértice.") + r"""
</section>
"""

# ---------------------------------------------------------------- Bloque III
B3 = r"""
<h2 class="part" id="p3">Bloque III — La forma matricial</h2>

<section id="s6">
  <h3>6. Las cinco fórmulas</h3>
  <p>La forma matricial hace <b>exactamente las mismas iteraciones</b>, pero en vez de arrastrar toda la tabla, recalcula $B^{-1}$ y reconstruye solo lo que necesita. Dada una base $B$ con costos $c_B$:</p>
  <table>
    <tr><th class="l">Fórmula</th><th class="l">Qué es</th><th class="l">Casilla del tableau</th></tr>
    <tr><td class="l">$x_B=B^{-1}b$</td><td class="l">valores de las variables básicas</td><td class="l">la columna <b>RHS</b></td></tr>
    <tr><td class="l">$B^{-1}A_j$</td><td class="l">columna actualizada de la variable $j$</td><td class="l">la <b>columna</b> de $x_j$</td></tr>
    <tr><td class="l">$\bar c_j = c_j-c_BB^{-1}A_j$</td><td class="l">costo reducido de la variable $j$</td><td class="l">la <b>fila CR</b></td></tr>
    <tr><td class="l">$y^\top=c_B^\top B^{-1}$</td><td class="l">los <b>precios sombra</b></td><td class="l">fila CR bajo las holguras</td></tr>
    <tr><td class="l">$w=c_B^\top B^{-1}b$</td><td class="l">valor objetivo de esa base</td><td class="l">celda CR/RHS</td></tr>
  </table>
  <div class="key">Con estas cinco expresiones se puede <b>saltar directamente</b> a cualquier base sin pasar por las intermedias: si alguien le dice "considere la base $\{x_1,h_1,h_2\}$", usted arma $B$, la invierte y reconstruye el tableau completo. Eso es exactamente lo que piden los ejercicios tipo <i>"muestre que esta solución básica no es óptima"</i> (Ejemplos 3 y 4).</div>
  <div class="app"><b>Por qué existe la forma matricial.</b> En un problema real con miles de variables, arrastrar el tableau completo es imposible: la mayoría de las columnas nunca se usa. El Simplex <b>revisado</b> —que es lo que usa Gurobi por dentro— mantiene solo $B^{-1}$ (en forma factorizada) y calcula $B^{-1}A_j$ <b>a demanda</b>, únicamente para las columnas candidatas. La forma matricial que se ve en clase es la versión didáctica de eso.</div>
</section>

<section id="s7">
  <h3>7. El cruce: dónde vive $B^{-1}$</h3>
  <p>Esta es la identidad que conecta las dos formas y la que hace que "armar el tableau" y "calcular con $B^{-1}$" sean <b>lo mismo</b>. El sistema estandarizado se escribe $[\,A\mid I\mid b\,]$, con $I$ las columnas de las holguras. Cualquier tableau intermedio es el original <b>multiplicado por $B^{-1}$</b>:</p>
  $$\boxed{\;B^{-1}\,[\,A\mid I\mid b\,]\;=\;[\;B^{-1}A\;\mid\; B^{-1}\;\mid\; B^{-1}b\;]\;}$$
  <div class="key">La consecuencia es directa y muy útil: <b>las columnas que ocupaban las holguras iniciales contienen, en cualquier iteración, la matriz $B^{-1}$ de esa base</b>. No hay que invertir nada a mano — si tiene el tableau, ya tiene $B^{-1}$ escrita ahí.</div>
  <h4>Ejemplo concreto</h4>
  <p>En el tableau óptimo de la Cervecería (Ejemplo 2), el bloque bajo $s_1,s_2,s_3$ es</p>
  $$B^{-1}=\begin{pmatrix}1&-1&0\\-1&2&0\\1&-4&1\end{pmatrix}$$
  <p>Verifiquémoslo: la base óptima es $\{x_2,x_1,s_3\}$, cuyas columnas <b>originales</b> son $(2,1,2)^\top$, $(1,1,3)^\top$ y $(0,0,1)^\top$, luego</p>
  $$B=\begin{pmatrix}2&1&0\\1&1&0\\2&3&1\end{pmatrix}\qquad\text{y}\qquad B^{-1}b=\begin{pmatrix}1&-1&0\\-1&2&0\\1&-4&1\end{pmatrix}\begin{pmatrix}16\\9\\24\end{pmatrix}=\begin{pmatrix}7\\2\\4\end{pmatrix},$$
  <p>que son justamente $x_2=7$, $x_1=2$, $s_3=4$ ✓.</p>
  <h4>Cuándo conviene cada forma</h4>
  <table>
    <tr><th class="l">Use <b>tableau</b> si...</th><th class="l">Use <b>matricial</b> si...</th></tr>
    <tr><td class="l">tiene que hacer <b>todas</b> las iteraciones desde el inicio</td><td class="l">le dan una base y le piden evaluarla <b>sin</b> iterar desde cero</td></tr>
    <tr><td class="l">el problema es chico (2–3 restricciones)</td><td class="l">le piden $B^{-1}$, los precios sombra o los rangos explícitamente</td></tr>
    <tr><td class="l">quiere ver el <b>camino</b> completo</td><td class="l">le dan un tableau <b>incompleto</b> y hay que reconstruirlo</td></tr>
  </table>
</section>

<section id="s8">
  <h3>8. Casos especiales</h3>
  <table>
    <tr><th class="l">Lo que ve en el tableau</th><th class="l">Qué significa</th><th class="l">Qué hacer</th></tr>
    <tr><td class="l"><b>Empate</b> en el costo reducido más negativo</td><td class="l">dos variables candidatas a entrar</td><td class="l">elegir cualquiera; solo cambia el camino, no el óptimo</td></tr>
    <tr><td class="l"><b>Empate</b> en la prueba del cociente</td><td class="l">la próxima base será <b>degenerada</b> (una básica valdrá 0)</td><td class="l">elegir cualquiera y seguir; ojo con el ciclado</td></tr>
    <tr><td class="l">La columna que entra <b>no tiene ningún elemento positivo</b></td><td class="l">problema <b>NO ACOTADO</b></td><td class="l">detenerse y reportarlo: falta una restricción en el modelo</td></tr>
    <tr><td class="l">Una variable <b>no básica</b> con $\bar c_j=0$ en el tableau óptimo</td><td class="l"><b>ÓPTIMOS ALTERNATIVOS</b></td><td class="l">hacer una iteración más entrega otro óptimo; todo el segmento entre ambos es óptimo</td></tr>
    <tr><td class="l">Una variable <b>básica</b> con valor $0$</td><td class="l">vértice <b>DEGENERADO</b></td><td class="l">seguir; puede haber iteraciones que no mejoren $z$</td></tr>
    <tr><td class="l">Una <b>artificial</b> básica y positiva al terminar la Fase I</td><td class="l">problema <b>INFACTIBLE</b></td><td class="l">detenerse: no existe solución</td></tr>
  </table>
  """ + img("especiales") + r"""
  <div class="warn"><b>Degeneración y ciclado.</b> En un vértice degenerado el Simplex puede hacer una iteración que <b>cambia la base pero no mueve el punto</b> ($\theta=0$), y en teoría podría dar vueltas para siempre. En la práctica casi nunca ocurre, y los solvers usan reglas anti-ciclado (Bland, perturbación). Lo que <b>sí</b> pasa seguido es que la degeneración produce <b>precios sombra no únicos</b> — lo vemos en el Ejemplo 1.</div>
</section>

<section id="s9">
  <h3>9. Restricciones $\geq$: artificiales, Gran M y dos fases</h3>
  <p>Con restricciones $\le$ y $b\ge0$, la base inicial sale gratis: las holguras, con $x_B=b\ge0$. Con una restricción $\ge$ eso <b>se rompe</b>: la columna del excedente es $-1$, no forma identidad, y además <b>el origen suele ser infactible</b>.</p>
  <div class="key"><b>La solución: variables artificiales.</b> A cada restricción $\ge$ (o $=$) se le agrega una variable $\alpha_i\ge0$ con coeficiente $+1$:
  $$a_i^\top x - h_i + \alpha_i = b_i.$$
  Ahora las $\alpha_i$ <b>sí</b> forman una identidad y dan una base inicial. Pero son <b>mentira</b>: si $\alpha_i&gt;0$ la restricción original no se cumple. Hay que forzarlas a cero.</div>
  <div class="grid2">
    <div>
      <h4>Método de la Gran M</h4>
      <p>Se penaliza cada artificial en la objetivo con un costo $M$ enorme:</p>
      $$\min\; c^\top x + M\sum_i \alpha_i$$
      <p>Como $M$ es gigantesco, el Simplex las expulsa apenas puede. Se resuelve <b>una sola vez</b>.</p>
      <p class="muted"><b>Contra:</b> si $M$ es demasiado grande hay problemas numéricos; si es muy chico, la solución puede quedar contaminada.</p>
    </div>
    <div>
      <h4>Método de las dos fases</h4>
      <p><b>Fase I:</b> ignorar la objetivo real y resolver $\min\sum_i\alpha_i$. Si el mínimo es $0$, se encontró una base factible; si es $&gt;0$, el problema es <b>infactible</b>.</p>
      <p><b>Fase II:</b> partir de esa base, borrar las artificiales y resolver con la objetivo verdadera.</p>
      <p class="muted"><b>A favor:</b> sin constantes mágicas, y la Fase I <b>diagnostica</b> la infactibilidad.</p>
    </div>
  </div>
  <div class="tip"><b>Un atajo que sirve muy seguido.</b> Si el enunciado ya le <b>regala</b> una solución básica factible —como el "opere solo la refinería 1 durante 150 días" del Ejemplo 4—, no hace falta ninguna de las dos: se arma $B$ con esas variables, se calcula $B^{-1}$ y se arranca el Simplex desde ahí. Por eso los certámenes suelen dar el punto de partida.</div>
</section>
"""

# ---------------------------------------------------------------- Ejemplos
X1 = r"""
<h2 class="part" id="p4">Bloque IV — Ejemplos resueltos</h2>

<section id="x1">
  <span class="badge">Ejemplo 1 · las dos formas sobre el mismo problema · Clases 17 y 18</span>
  <h3>Computadores: tableau y matricial, lado a lado</h3>
  <div class="app"><b>Enunciado.</b> Se venden dos computadores al día. El <b>A</b> se vende a US\$900 y usa <b>4 horas</b> de armado y US\$400 de componentes; el <b>B</b> se vende a US\$500 y usa <b>1 hora</b> y US\$200 de componentes. Hay 10 horas diarias, US\$1.200 para invertir y un mostrador donde caben a lo más <b>4</b> computadores (no hay bodega).</div>
  <p>Los <b>márgenes</b> son $900-400=500$ y $500-200=300$. La restricción de inversión $400x_1+200x_2\le1200$ se simplifica dividiendo por 100:</p>
  $$\max\; z=500x_1+300x_2\qquad\text{s.a.}\quad
  \begin{cases}
  4x_1+2x_2\le12 & \text{(inversión)}\\
  4x_1+x_2\le10 & \text{(horas)}\\
  x_1+x_2\le4 & \text{(mostrador)}\\
  x_1,x_2\ge0
  \end{cases}$$
  <p>Forma estándar con holguras $s_1,s_2,s_3$. Usamos la <b>convención A</b> (máximo directo): la fila CR arranca con los márgenes positivos, entra el más positivo, se para cuando todos son $\le0$.</p>

  <h4>Tableau 0 — Base $\{s_1,s_2,s_3\}$, $\;x=(0,0)$, $\;z=0$</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th><th class="l">cociente</th></tr>
    <tr><td class="cr">CR</td><td class="cr ent">500</td><td class="cr">300</td><td class="cr">0</td><td class="cr">0</td><td class="cr">0</td><td class="cr">0</td><td class="l">—</td></tr>
    <tr><td>$s_1$</td><td>4</td><td>2</td><td>1</td><td>0</td><td>0</td><td>12</td><td class="l">$12/4=3$</td></tr>
    <tr><td>$s_2$</td><td class="piv">4</td><td>1</td><td>0</td><td>1</td><td>0</td><td>10</td><td class="l">$10/4=\mathbf{2{,}5}$ ←</td></tr>
    <tr><td>$s_3$</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>4</td><td class="l">$4/1=4$</td></tr>
  </table></div>
  <p>Entra $x_1$ ($\bar c=500$ es el más positivo). Cocientes $3;\,2{,}5;\,4$ ⟹ mínimo $2{,}5$ ⟹ <b>sale $s_2$</b>, pivote $=4$.</p>

  <h4>Tableau 1 — Base $\{s_1,x_1,s_3\}$, $\;x=(2{,}5;\,0)$, $\;z=1250$</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th><th class="l">cociente</th></tr>
    <tr><td class="cr">CR</td><td class="cr">0</td><td class="cr ent">175</td><td class="cr">0</td><td class="cr">−125</td><td class="cr">0</td><td class="cr">1250</td><td class="l">—</td></tr>
    <tr><td>$s_1$</td><td>0</td><td class="piv">1</td><td>1</td><td>−1</td><td>0</td><td>2</td><td class="l">$2/1=\mathbf{2}$ ←</td></tr>
    <tr><td>$x_1$</td><td>1</td><td>0,25</td><td>0</td><td>0,25</td><td>0</td><td>2,5</td><td class="l">$2{,}5/0{,}25=10$</td></tr>
    <tr><td>$s_3$</td><td>0</td><td>0,75</td><td>0</td><td>−0,25</td><td>1</td><td>1,5</td><td class="l">$1{,}5/0{,}75=2$</td></tr>
  </table></div>
  <p>Entra $x_2$ ($\bar c=175&gt;0$). <b>Hay empate</b> en el cociente ($2$ y $2$): elegimos la fila de $s_1$. El empate anticipa que la próxima base será <b>degenerada</b>.</p>

  <h4>Tableau 2 — Base $\{s_1,x_1,x_2\}$ — ÓPTIMO</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th></tr>
    <tr><td class="cr">CR</td><td class="cr">0</td><td class="cr">0</td><td class="cr">0</td><td class="cr">$-\frac{200}{3}$</td><td class="cr">$-\frac{700}{3}$</td><td class="cr">1600</td></tr>
    <tr><td class="bas">$s_1$</td><td>0</td><td>0</td><td>1</td><td>$-\frac{2}{3}$</td><td>$-\frac{4}{3}$</td><td class="bas"><b>0</b></td></tr>
    <tr><td class="bas">$x_1$</td><td>1</td><td>0</td><td>0</td><td>$\frac{1}{3}$</td><td>$-\frac{1}{3}$</td><td class="bas"><b>2</b></td></tr>
    <tr><td class="bas">$x_2$</td><td>0</td><td>1</td><td>0</td><td>$-\frac{1}{3}$</td><td>$\frac{4}{3}$</td><td class="bas"><b>2</b></td></tr>
  </table></div>
  <p>Todos los CR son $\le0$ ⟹ <b>óptimo</b>: $\;x^*=(2,2)$, $z^*=1600$. Es exactamente el tableau final de la Clase 17.</p>

  <h4>La misma cosa en forma matricial</h4>
  <p>Base óptima $\{s_1,x_1,x_2\}$. Sus columnas originales son $(1,0,0)^\top$, $(4,4,1)^\top$ y $(2,1,1)^\top$:</p>
  $$B=\begin{pmatrix}1&4&2\\0&4&1\\0&1&1\end{pmatrix},\qquad
    B^{-1}=\begin{pmatrix}1&-\frac{2}{3}&-\frac{4}{3}\\[2pt]0&\frac{1}{3}&-\frac{1}{3}\\[2pt]0&-\frac{1}{3}&\frac{4}{3}\end{pmatrix},\qquad c_B=(0,\,500,\,300)$$
  $$x_B=B^{-1}b=B^{-1}\begin{pmatrix}12\\10\\4\end{pmatrix}=\begin{pmatrix}0\\2\\2\end{pmatrix},\qquad z=c_B^\top x_B=1600,\qquad y^\top=c_B^\top B^{-1}=\left(0,\;\tfrac{200}{3},\;\tfrac{700}{3}\right)$$
  <div class="key"><b>Compare con el tableau.</b> El bloque bajo $s_1,s_2,s_3$ del Tableau 2 <b>es</b> $B^{-1}$; la columna RHS <b>es</b> $B^{-1}b$; y la fila CR bajo las holguras es $-y^\top$. No son dos métodos: es la misma matriz mirada de dos maneras.</div>

  <h4>Lo interesante de este ejemplo: es degenerado</h4>
  <p>En $(2,2)$ se cumplen las <b>tres</b> restricciones con igualdad: $8+4=12$ ✓, $8+2=10$ ✓, $2+2=4$ ✓. Tres rectas pasan por el mismo punto de un plano de 2 variables. Por eso $s_1$ queda <b>básica con valor 0</b>.</p>
  <div class="warn"><b>Y por eso los precios sombra NO son únicos.</b> El tableau de arriba entrega $y=(0;\;200/3;\;700/3)\approx(0;\,66{,}7;\,233{,}3)$. Pero si se resuelve el mismo modelo en Gurobi, reporta $y=(100,\,0,\,100)$. <b>Ambos son correctos</b>: los dos verifican dualidad fuerte,
  $$12(0)+10\tfrac{200}{3}+4\tfrac{700}{3}=\tfrac{2000+2800}{3}=1600\;✓\qquad 12(100)+10(0)+4(100)=1600\;✓$$
  y los dos son duales óptimos. La degeneración primal produce <b>múltiples soluciones duales</b>, y cada base óptima entrega una distinta. Si su respuesta no coincide con la pauta, <b>verifique dualidad fuerte antes de suponer que se equivocó</b>.</div>
</section>
"""

X2 = r"""
<section id="x2">
  <span class="badge">Ejemplo 2 · convención de minimización · Ayudantía 6</span>
  <h3>Cervecería Los Andes: el mismo algoritmo con los signos al revés</h3>
  <div class="app"><b>Enunciado.</b> Se producen dos estilos por lote semanal: <b>Golden Ale</b> ($x_1$) y <b>Doble IPA</b> ($x_2$), en barriles, con márgenes de \$30 y \$50 mil. Limitan la malta (1 y 2 sacos por barril, 16 disponibles), la fermentación (1 y 1 día-tanque, 9 disponibles) y el embotellado (3 y 2 horas, 24 disponibles).</div>
  $$\max\; z=30x_1+50x_2 \quad\text{s.a.}\quad x_1+2x_2\le16,\;\;x_1+x_2\le9,\;\;3x_1+2x_2\le24,\;\;x\ge0$$
  <p>Ahora usamos la <b>convención C</b>: se minimiza $w=-z$ con $c=(-30,-50,0,0,0)$, entra el CR <b>más negativo</b> y se para cuando todos son $\ge0$. La celda objetivo la escribimos con el valor de $z=-w$ para no perdernos.</p>

  <h4>Tableau 0 — Base $\{s_1,s_2,s_3\}$</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th><th class="l">cociente</th></tr>
    <tr><td class="cr">CR</td><td class="cr">−30</td><td class="cr ent">−50</td><td class="cr">0</td><td class="cr">0</td><td class="cr">0</td><td class="cr">0</td><td class="l">—</td></tr>
    <tr><td>$s_1$</td><td>1</td><td class="piv">2</td><td>1</td><td>0</td><td>0</td><td>16</td><td class="l">$16/2=\mathbf{8}$ ←</td></tr>
    <tr><td>$s_2$</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>9</td><td class="l">$9/1=9$</td></tr>
    <tr><td>$s_3$</td><td>3</td><td>2</td><td>0</td><td>0</td><td>1</td><td>24</td><td class="l">$24/2=12$</td></tr>
  </table></div>
  <p>Entra $x_2$ (más negativo, $-50$); sale $s_1$; pivote $=2$.</p>

  <h4>Tableau 1 — Base $\{x_2,s_2,s_3\}$, $\;x=(0,8)$, $\;z=400$</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th><th class="l">cociente</th></tr>
    <tr><td class="cr">CR</td><td class="cr ent">−5</td><td class="cr">0</td><td class="cr">25</td><td class="cr">0</td><td class="cr">0</td><td class="cr">400</td><td class="l">—</td></tr>
    <tr><td>$x_2$</td><td>0,5</td><td>1</td><td>0,5</td><td>0</td><td>0</td><td>8</td><td class="l">$8/0{,}5=16$</td></tr>
    <tr><td>$s_2$</td><td class="piv">0,5</td><td>0</td><td>−0,5</td><td>1</td><td>0</td><td>1</td><td class="l">$1/0{,}5=\mathbf{2}$ ←</td></tr>
    <tr><td>$s_3$</td><td>2</td><td>0</td><td>−1</td><td>0</td><td>1</td><td>8</td><td class="l">$8/2=4$</td></tr>
  </table></div>
  <p>Entra $x_1$ ($-5$); sale $s_2$; pivote $=0{,}5$.</p>

  <h4>Tableau 2 — Base $\{x_2,x_1,s_3\}$ — ÓPTIMO</h4>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th></tr>
    <tr><td class="cr">CR</td><td class="cr">0</td><td class="cr">0</td><td class="cr">20</td><td class="cr">10</td><td class="cr">0</td><td class="cr">410</td></tr>
    <tr><td class="bas">$x_2$</td><td>0</td><td>1</td><td>1</td><td>−1</td><td>0</td><td class="bas"><b>7</b></td></tr>
    <tr><td class="bas">$x_1$</td><td>1</td><td>0</td><td>−1</td><td>2</td><td>0</td><td class="bas"><b>2</b></td></tr>
    <tr><td class="bas">$s_3$</td><td>0</td><td>0</td><td>1</td><td>−4</td><td>1</td><td class="bas"><b>4</b></td></tr>
  </table></div>
  $$\boxed{x^*=(2,\,7),\qquad z^*=30(2)+50(7)=410}$$
  <p>Todos los CR son $\ge0$ ⟹ óptimo. Y este es el tableau que se diseccionó en la <b>sección 4</b>: los precios sombra son $y^*=(20,\,10,\,0)$, la matriz $B^{-1}$ está bajo $s_1,s_2,s_3$, y $s_3=4$ dice que al embotellado le sobran 4 horas.</p>
  <div class="key"><b>Chequeo de dualidad fuerte:</b> $16(20)+9(10)+24(0)=320+90=410=z^*$ ✓. Este chequeo <b>también</b> detecta errores de signo: si le hubiera dado $-410$, la convención se le dio vuelta en algún paso.</div>
  <div class="tip"><b>Compare con el Ejemplo 1.</b> Mismo algoritmo, distinta convención. Ahí la fila CR partía en $(500,300)$ y se paraba con todos $\le0$; acá parte en $(-30,-50)$ y se para con todos $\ge0$. <b>Lo único que cambia es el signo con que se escribe la fila.</b></div>
</section>
"""

X3 = r"""
<section id="x3">
  <span class="badge">Ejemplo 3 · el ejercicio de certamen · Clase 25A</span>
  <h3>Completar un tableau incompleto</h3>
  <p>Este tipo de pregunta mide si uno entiende <b>de dónde sale cada número</b>, no si sabe pivotear.</p>
  $$\max\;x_1+3x_2\qquad\text{s.a.}\quad 5x_1+2x_2\ge30,\quad 3x_1-2x_2\le18,\quad x_1+2x_2\le22,\quad x\ge0$$
  <p><b>Forma estándar</b> (en minimización, $c=(-1,-3,0,0,0)$): la primera restricción es $\ge$, así que lleva un <b>excedente</b> $s_1$ con coeficiente $-1$; las otras dos llevan holguras $h_1,h_2$:</p>
  $$5x_1+2x_2-s_1=30,\qquad 3x_1-2x_2+h_1=18,\qquad x_1+2x_2+h_2=22$$
  <p>Se entrega el siguiente tableau, con tres valores borrados:</p>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$h_1$</th><th>$h_2$</th><th>$-z$</th></tr>
    <tr><td class="cr">F. Obj.</td><td class="cr">0</td><td class="cr">$-\frac{13}{5}$</td><td class="cr">$-\frac{1}{5}$</td><td class="cr ent">$\boldsymbol\alpha$</td><td class="cr">0</td><td class="cr ent">$\boldsymbol\gamma$</td></tr>
    <tr><td>$x_1$</td><td>1</td><td>$\frac{2}{5}$</td><td>$-\frac{1}{5}$</td><td>0</td><td>0</td><td class="ent">$\boldsymbol\beta$</td></tr>
    <tr><td>$h_1$</td><td>0</td><td>$-\frac{16}{5}$</td><td>$\frac{3}{5}$</td><td>1</td><td>0</td><td>0</td></tr>
    <tr><td>$h_2$</td><td>0</td><td>$\frac{8}{5}$</td><td>$\frac{1}{5}$</td><td>0</td><td>1</td><td>16</td></tr>
  </table></div>

  <h4>$\alpha$ — sin calcular nada</h4>
  <p>$h_1$ es una variable <b>básica</b>, y el costo reducido de toda variable básica es <b>cero</b>. Además su columna es $(0,1,0)^\top$, un vector de la identidad, lo que lo confirma.</p>
  $$\boxed{\alpha=0}$$

  <h4>$\beta$ — reconstruyendo $B^{-1}b$</h4>
  <p>La base es $\{x_1,h_1,h_2\}$. Sus columnas originales son $(5,3,1)^\top$, $(0,1,0)^\top$ y $(0,0,1)^\top$:</p>
  $$B=\begin{pmatrix}5&0&0\\3&1&0\\1&0&1\end{pmatrix},\qquad
    B^{-1}=\begin{pmatrix}\frac{1}{5}&0&0\\-\frac{3}{5}&1&0\\-\frac{1}{5}&0&1\end{pmatrix},\qquad
    x_B=B^{-1}\begin{pmatrix}30\\18\\22\end{pmatrix}=\begin{pmatrix}6\\0\\16\end{pmatrix}$$
  $$\boxed{\beta=6}$$
  <p>Los otros dos valores de $x_B$ coinciden con el tableau ($h_1=0$, $h_2=16$) ✓. <b>Atajo aún más rápido:</b> la columna de $s_1$ en la fila de $x_1$ vale $-1/5$, y $B^{-1}A_{s_1}=B^{-1}(-1,0,0)^\top$ es la primera columna de $B^{-1}$ cambiada de signo — de ahí se lee $1/5$, y entonces $x_1=\frac{1}{5}(30)=6$.</p>

  <h4>$\gamma$ — el valor objetivo</h4>
  <p>Con $x_1=6$ y $x_2=0$: $\;z=1(6)+3(0)=6$.</p>
  $$\boxed{\gamma=6}$$

  <h4>¿Es óptimo? (la parte que vale más puntos)</h4>
  <p>Estamos en forma de <b>minimización</b>, así que se necesita que <b>todos</b> los costos reducidos sean $\ge0$. Pero hay dos negativos: $-\frac{13}{5}$ (en $x_2$) y $-\frac{1}{5}$ (en $s_1$). <b>No es óptimo.</b></p>
  <p>Entra el más negativo, $x_2$. Prueba del cociente sobre su columna $\left(\frac{2}{5},-\frac{16}{5},\frac{8}{5}\right)$, <b>solo con entradas positivas</b>:</p>
  <table>
    <tr><th class="l">Fila</th><th>$x_{B_k}$</th><th>$\bar a_{k,x_2}$</th><th class="l">cociente</th></tr>
    <tr><td class="l">$x_1$</td><td>6</td><td>$\frac{2}{5}$</td><td class="l">$6\big/\frac{2}{5}=15$</td></tr>
    <tr><td class="l">$h_1$</td><td>0</td><td>$-\frac{16}{5}$</td><td class="l">negativo ⟹ <b>no participa</b></td></tr>
    <tr><td class="l">$h_2$</td><td>16</td><td>$\frac{8}{5}$</td><td class="l">$16\big/\frac{8}{5}=\mathbf{10}$ ←</td></tr>
  </table>
  <p>Sale $h_2$. Nueva base $\{x_1,h_1,x_2\}$ con $x_2=10$ y $x_1=6-\frac{2}{5}(10)=2$:</p>
  $$\boxed{x^*=(2,\,10),\qquad z^*=2+30=32}$$
  <div class="tip"><b>El detalle que se le escapa a casi todos:</b> la fila de $h_1$ tiene $x_{B}=0$ (base degenerada) <b>y</b> coeficiente negativo. Es tentador calcular $0/(-16/5)=0$ y concluir que sale $h_1$ con $\theta=0$. <b>Está mal</b>: la prueba del cociente <b>excluye</b> los denominadores no positivos, sin importar el numerador. Un coeficiente negativo significa que esa básica <b>crece</b>, no que se agote.</div>
</section>
"""

X4 = r"""
<section id="x4">
  <span class="badge">Ejemplo 4 · mínimo con $\geq$ · Clase 18</span>
  <h3>Refinerías: arrancar desde una base que le regalan</h3>
  <div class="app"><b>Enunciado.</b> Una petrolera tiene dos refinerías. La <b>1</b> cuesta US\$25M al día y produce diariamente 4 tanques de alto octanaje, 3 de medio y 2 de bajo. La <b>2</b> cuesta US\$20M y produce 3, 4 y 5. Hay órdenes por 250, 270 y 300 tanques respectivamente.</div>
  $$\min\;25x_1+20x_2\qquad\text{s.a.}\quad 4x_1+3x_2\ge250,\quad 3x_1+4x_2\ge270,\quad 2x_1+5x_2\ge300,\quad x\ge0$$
  <p>donde $x_1,x_2$ son <b>días de operación</b> de cada refinería.</p>

  <h4>(a) Forma estándar</h4>
  <p>Las tres son $\ge$, así que se resta un excedente en cada una:</p>
  $$\begin{cases}
  4x_1+3x_2-h_1=250\\
  3x_1+4x_2-h_2=270\\
  2x_1+5x_2-h_3=300
  \end{cases}\qquad
  c^\top=(25,\,20,\,0,\,0,\,0),\quad
  A=\begin{pmatrix}4&3&-1&0&0\\3&4&0&-1&0\\2&5&0&0&-1\end{pmatrix},\quad
  b=\begin{pmatrix}250\\270\\300\end{pmatrix}$$
  """ + img("refinerias") + r"""
  <div class="warn"><b>Fíjese en el gráfico: el origen NO es factible.</b> La base "obvia" $\{h_1,h_2,h_3\}$ daría $h=-b&lt;0$: es una solución básica <b>infactible</b>. Por eso este problema necesita <b>artificiales</b> (Gran M o dos fases)... <b>a menos</b> que el enunciado regale un punto de partida, que es lo que hace la parte (b).</div>

  <h4>(b) Verificar que "solo la refinería 1 durante 150 días" no es óptimo</h4>
  <p>El punto es $x=(150,\,0)$. Chequeamos factibilidad: $4(150)=600\ge250$ ✓, $3(150)=450\ge270$ ✓, $2(150)=300\ge300$ ✓ (¡esta última <b>justo</b>). Los excedentes son $h_1=350$, $h_2=180$, $h_3=0$.</p>
  <p>Variables no nulas: $x_1,h_1,h_2$. Esa es la base, y $h_3=0$ la hace <b>degenerada</b>. Sus columnas:</p>
  $$B=\begin{pmatrix}4&-1&0\\3&0&-1\\2&0&0\end{pmatrix},\qquad c_B=(25,\,0,\,0)$$
  <p>El precio sombra es $y^\top=c_B^\top B^{-1}$. Como solo la primera componente de $c_B$ es no nula, $y^\top$ es $25$ veces la <b>primera fila</b> de $B^{-1}$, que resulta $(0,\,0,\,\tfrac12)$, luego $y=(0,\,0,\,12{,}5)$. Los costos reducidos de las <b>no básicas</b> $x_2$ y $h_3$ son:</p>
  $$\bar c_{x_2}=20-y^\top\!\begin{pmatrix}3\\4\\5\end{pmatrix}=20-62{,}5=\mathbf{-42{,}5},\qquad
    \bar c_{h_3}=0-y^\top\!\begin{pmatrix}0\\0\\-1\end{pmatrix}=+12{,}5$$
  <div class="key">Estamos <b>minimizando</b>, así que se exige $\bar c_j\ge0$. Como $\bar c_{x_2}=-42{,}5&lt;0$, <b>la solución no es óptima</b>: cada día que se opere la refinería 2 <b>baja</b> el costo total en 42,5. En lenguaje de negocio: la refinería 2 es más barata y más productiva en medio y bajo octanaje; usar solo la 1 es un desperdicio.</div>

  <h4>(c) Iterar hasta el óptimo</h4>
  <p>Entra $x_2$. Siguiendo el Simplex desde esa base se llega a</p>
  $$\boxed{x^*=(25,\,50),\qquad z^*=25(25)+20(50)=625+1000=1625}$$
  <p>Activas: la primera ($4(25)+3(50)=250$) y la tercera ($2(25)+5(50)=300$). La segunda queda con excedente: $3(25)+4(50)=275&gt;270$, sobran <b>5 tanques</b> de medio octanaje.</p>
  <p>Los precios sombra del óptimo son $y=\left(\tfrac{85}{14},\,0,\,\tfrac{5}{14}\right)\approx(6{,}07;\;0;\;0{,}36)$, y se verifican con dualidad fuerte: $250\cdot\tfrac{85}{14}+300\cdot\tfrac{5}{14}=\tfrac{22750}{14}=1625$ ✓.</p>
  <div class="app"><b>Lectura.</b> Un tanque más de alto octanaje encarece el plan en 6,07 millones; uno de bajo, en 0,36. El requerimiento de <b>medio</b> octanaje se cumple de sobra: exigir uno más <b>no cuesta nada</b>. Si el área comercial quiere negociar un pedido, que negocie el <b>alto</b> octanaje: es el que aprieta.</div>
</section>
"""

X5 = r"""
<section id="x5">
  <span class="badge">Ejemplo 5 · bases y $B^{-1}$ · Clase 25A</span>
  <h3>Contar bases, elegir una factible y leer $B^{-1}$</h3>
  $$\max\;3x_1+2x_2\qquad\text{s.a.}\quad -x_1+x_2\le1,\quad 5x_1+3x_2\le15,\quad x_2\ge1,\quad x\ge0$$

  <h4>(a) Estandarizar y contar bases</h4>
  <p>Dos holguras ($x_3,x_4$) y un excedente ($x_5$):</p>
  $$-x_1+x_2+x_3=1,\qquad 5x_1+3x_2+x_4=15,\qquad x_2-x_5=1$$
  <p>Quedan $n=5$ variables y $m=3$ ecuaciones, así que hay a lo más</p>
  $$\binom{5}{3}=10 \text{ bases posibles.}$$
  <div class="tip">"A lo más": algunas de esas 10 elecciones dan una $B$ <b>singular</b> (no invertible) y no son bases; y de las que sí lo son, varias dan soluciones <b>infactibles</b>. Solo las factibles corresponden a vértices.</div>

  <h4>(b) Elegir una base factible e iterar</h4>
  <table>
    <tr><th class="l">Base</th><th class="l">$x_B=B^{-1}b$</th><th>¿Factible?</th></tr>
    <tr><td class="l">$B_1=\{x_1,x_3,x_5\}$</td><td class="l">requiere $x_2=0$, pero la tercera pide $x_2-x_5=1$ con $x_5\ge0$… queda $x_5=-1$</td><td>NO</td></tr>
    <tr><td class="l">$B_2=\{x_2,x_3,x_5\}$</td><td class="l">$x_2=5$ (de la segunda), y entonces $x_3=1-5=-4$</td><td>NO</td></tr>
    <tr><td class="l">$B_3=\{x_2,x_4,x_5\}$</td><td class="l">$x_2=1$, $x_4=15-3=12$, $x_5=0$</td><td><b>SÍ</b></td></tr>
  </table>
  <p>Iteramos desde $B_3$, que corresponde al vértice $(0,1)$ con $z=2$. El costo reducido de $x_1$ resulta negativo (en forma de minimización), así que $x_1$ entra; sale $x_3$, y la nueva base $\{x_2,x_1,x_5\}$ da</p>
  $$\boxed{x^*=\left(\tfrac{3}{2},\;\tfrac{5}{2}\right),\qquad z^*=\tfrac{9}{2}+5=\tfrac{19}{2}=9{,}5}$$
  <p>Los costos reducidos de las no básicas quedan $-\frac18$ y $-\frac58$ en la convención de máximo (es decir, ambos con el signo "de parada") ⟹ <b>es óptimo</b>.</p>

  <h4>(c) ¿Qué pasa si $x_3$ aumenta en una unidad?</h4>
  <p>Esta pregunta es exactamente <b>"lea la columna de $x_3$ en el tableau"</b>. Con la base $\{x_1,x_2,x_5\}$, la columna actualizada es $B^{-1}A_{x_3}$, y el efecto sobre cada básica es</p>
  $$x_B(\theta)=x_B-\theta\,B^{-1}A_{x_3}.$$
  <p>Los coeficientes resultan: $x_1$ <b>aumenta</b> en $0{,}375$ por unidad, mientras que $x_2$ y $x_5$ <b>disminuyen</b> en $0{,}625$ cada una.</p>
  <div class="key"><b>Sentido económico.</b> $x_3$ es la holgura de $-x_1+x_2\le1$. Dejar una unidad de holgura sin usar equivale a relajar esa restricción hacia adentro: el plan se reacomoda produciendo más $x_1$ y menos $x_2$. Y como $x_2$ baja, el excedente $x_5$ de la restricción $x_2\ge1$ también baja. <b>La columna del tableau es una tabla de sensibilidad en miniatura.</b></div>
</section>
"""

GUR = r"""
<h2 class="part" id="p5">Bloque V — Código, trampas y práctica</h2>

<section id="gur">
  <h3>10. El Simplex matricial en <code>numpy</code></h3>
  <p>Implementarlo obliga a entender el algoritmo, y sirve para <b>verificar</b> los tableaus hechos a mano. Es la versión de la Ayudantía 6, en convención de minimización.</p>
<pre><code class="language-python">import numpy as np
from numpy.linalg import inv

# Simplex matricial en forma de MINIMIZACION.
# A ya incluye las columnas de holgura; la base inicial son las ultimas m columnas.
def simplex(c, A, b, nombres, verbose=True):
    m, n = A.shape
    base = list(range(n - m, n))              # las holguras arrancan en la base
    it = 0
    while True:
        B    = A[:, base]
        Binv = inv(B)
        cB   = c[base]
        xB   = Binv @ b                        # valores de las basicas
        z    = cB @ xB                         # valor objetivo
        cr   = c - cB @ Binv @ A               # costos reducidos de TODAS

        if verbose:
            print(f"it {it} | base {[nombres[i] for i in base]} | w = {z:.4f}")
            print(f"        x_B = {np.round(xB, 4)}")
            print(f"        CR  = {np.round(cr, 4)}")

        if np.all(cr &gt;= -1e-9):                # criterio de parada (minimizacion)
            return base, xB, z, Binv, -cB @ Binv

        e = int(np.argmin(cr))                 # entra la mas negativa (Dantzig)
        col = Binv @ A[:, e]                   # columna actualizada

        if np.all(col &lt;= 1e-9):                # ningun elemento positivo
            raise ValueError("problema NO ACOTADO")

        # prueba del cociente: SOLO denominadores positivos
        raz = np.array([xB[k] / col[k] if col[k] &gt; 1e-9 else np.inf for k in range(m)])
        s = int(np.argmin(raz))                # sale la del cociente minimo
        if verbose:
            print(f"        entra {nombres[e]}, sale {nombres[base[s]]}, theta = {raz[s]:.4f}\n")
        base[s] = e
        it += 1

# Cerveceria Los Andes: max 30x1+50x2  ->  min -30x1-50x2
A = np.array([[1., 2, 1, 0, 0],
              [1., 1, 0, 1, 0],
              [3., 2, 0, 0, 1]])
b = np.array([16., 9, 24])
c = np.array([-30., -50, 0, 0, 0])            # margenes con el signo cambiado
nom = ["x1", "x2", "s1", "s2", "s3"]

base, xB, w, Binv, y = simplex(c, A, b, nom)
print("solucion  :", {nom[i]: round(float(v), 4) for i, v in zip(base, xB)})
print("z* = -w*  :", -w)
print("B^-1      :\n", Binv)
print("precios sombra:", y)
</code></pre>
  <p>Salida:</p>
<pre><code>it 0 | base ['s1', 's2', 's3'] | w = 0.0000
        x_B = [16.  9. 24.]
        CR  = [-30. -50.   0.   0.   0.]
        entra x2, sale s1, theta = 8.0000

it 1 | base ['x2', 's2', 's3'] | w = -400.0000
        x_B = [8. 1. 8.]
        CR  = [-5.  0. 25.  0.  0.]
        entra x1, sale s2, theta = 2.0000

it 2 | base ['x2', 'x1', 's3'] | w = -410.0000
        x_B = [7. 2. 4.]
        CR  = [ 0.  0. 20. 10.  0.]
solucion  : {'x2': 7.0, 'x1': 2.0, 's3': 4.0}
z* = -w*  : 410.0
B^-1      :
 [[ 1. -1.  0.]
 [-1.  2.  0.]
 [ 1. -4.  1.]]
precios sombra: [20. 10.  0.]
</code></pre>
  <div class="key">Los tres tableaus impresos son <b>exactamente</b> los tres del Ejemplo 2, y la $B^{-1}$ coincide con el bloque bajo las holguras. Si su desarrollo a mano no calza con esta salida, el error está en el pivoteo.</div>
  <h4>Verificación con <code>scipy</code> y <code>gurobipy</code></h4>
<pre><code class="language-python">from scipy.optimize import linprog
res = linprog(c=[-30, -50], A_ub=[[1,2],[1,1],[3,2]], b_ub=[16,9,24],
              bounds=[(0,None),(0,None)], method="highs")
print(f"scipy : x=({res.x[0]:.2f}, {res.x[1]:.2f})  z*={-res.fun:.2f}")

import gurobipy as gp
from gurobipy import GRB
m = gp.Model("cerveceria"); m.Params.OutputFlag = 0
x1 = m.addVar(name="golden"); x2 = m.addVar(name="ipa")
m.setObjective(30*x1 + 50*x2, GRB.MAXIMIZE)
for coef, rhs, nm in [((1,2), 16, "malta"), ((1,1), 9, "fermentacion"), ((3,2), 24, "embotellado")]:
    m.addConstr(coef[0]*x1 + coef[1]*x2 &lt;= rhs, name=nm)
m.optimize()
print(f"gurobi: x=({x1.X:.2f}, {x2.X:.2f})  z*={m.ObjVal:.2f}")
for c_ in m.getConstrs():
    print(f"   {c_.ConstrName:&lt;13} y={c_.Pi:5.2f}  holgura={c_.Slack:5.2f}")
</code></pre>
  <div class="tip"><b>Ojo con <code>scipy</code>:</b> <code>linprog</code> <b>siempre minimiza</b>, así que hay que pasarle los coeficientes negados y recordar que el óptimo del máximo es <code>-res.fun</code>. Es la convención C, la misma del Ejemplo 2. Y <code>method="highs"</code> no es un Simplex de tableau: es un solver moderno que puede devolver un vértice <b>distinto</b> si hay óptimos alternativos.</div>
</section>

<section id="trampas">
  <h3>11. Doce trampas clásicas</h3>
  <table>
    <tr><th>#</th><th class="l">Trampa</th><th class="l">Lo correcto</th></tr>
    <tr><td>1</td><td class="l">Mezclar convenciones a mitad de camino</td><td class="l">Declararla al empezar y no soltarla (sección 3)</td></tr>
    <tr><td>2</td><td class="l">Incluir denominadores $\le0$ en la prueba del cociente</td><td class="l">Solo entradas <b>estrictamente positivas</b>, sin importar el numerador</td></tr>
    <tr><td>3</td><td class="l">Olvidar pivotear la <b>fila CR</b></td><td class="l">La columna que entra debe quedar con $0$ también en la fila CR</td></tr>
    <tr><td>4</td><td class="l">Usar holguras como base inicial habiendo restricciones $\ge$</td><td class="l">El excedente tiene coeficiente $-1$: hacen falta <b>artificiales</b></td></tr>
    <tr><td>5</td><td class="l">Dejar un $b_i&lt;0$ sin arreglar</td><td class="l">Multiplicar esa fila por $-1$ (y dar vuelta la desigualdad)</td></tr>
    <tr><td>6</td><td class="l">Reportar $w^*$ cuando el problema era un máximo</td><td class="l">$z^*=-w^*$ en la convención C</td></tr>
    <tr><td>7</td><td class="l">Ver una básica en $0$ y creer que hay un error</td><td class="l">Es <b>degeneración</b>, es normal y suele haber tres restricciones concurrentes</td></tr>
    <tr><td>8</td><td class="l">Suponer que los precios sombra son únicos</td><td class="l">Con degeneración hay <b>varios</b> duales óptimos (Ejemplo 1)</td></tr>
    <tr><td>9</td><td class="l">Ignorar un $\bar c_j=0$ en una <b>no</b> básica del tableau final</td><td class="l">Es la señal de <b>óptimos alternativos</b>; conviene mencionarlo</td></tr>
    <tr><td>10</td><td class="l">Concluir "no acotado" porque la región es infinita</td><td class="l">Solo lo es si la <b>columna que entra</b> no tiene ningún positivo</td></tr>
    <tr><td>11</td><td class="l">Invertir $B$ a mano teniendo el tableau</td><td class="l">$B^{-1}$ ya está escrita bajo las holguras iniciales</td></tr>
    <tr><td>12</td><td class="l">No verificar al final</td><td class="l">Evaluar $p^\top x^*$ con el enunciado original y chequear $\sum_i y_ib_i=z^*$</td></tr>
  </table>
</section>

<section id="cheat">
  <h3>Cheat-sheet</h3>
  <div class="grid2">
    <div>
      <h4>Las cinco fórmulas</h4>
      $$x_B=B^{-1}b\qquad \bar c_j=c_j-c_B^\top B^{-1}A_j$$
      $$y^\top=c_B^\top B^{-1}\qquad w=c_B^\top B^{-1}b$$
      $$B^{-1}[A\mid I\mid b]=[B^{-1}A\mid B^{-1}\mid B^{-1}b]$$
      <h4>Prueba del cociente</h4>
      $$\theta=\min_k\left\{\frac{x_{B_k}}{\bar a_{kj}}\;:\;\bar a_{kj}&gt;0\right\}$$
      <h4>Estandarizar</h4>
      <table style="font-size:.86rem">
        <tr><th>Original</th><th>Se agrega</th></tr>
        <tr><td>$\le b$</td><td>$+s$, &nbsp;$s\ge0$</td></tr>
        <tr><td>$\ge b$</td><td>$-h\;(+\alpha)$</td></tr>
        <tr><td>$= b$</td><td>$(+\alpha)$</td></tr>
      </table>
    </div>
    <div>
      <h4>Convenciones</h4>
      <table style="font-size:.86rem">
        <tr><th>Fila CR</th><th>Entra</th><th>Para si</th></tr>
        <tr><td>$c_j-z_j$ (máx)</td><td>más $+$</td><td>todos $\le0$</td></tr>
        <tr><td>$z_j-c_j$ (máx)</td><td>más $-$</td><td>todos $\ge0$</td></tr>
        <tr><td>$c_j-z_j$, $c=-p$</td><td>más $-$</td><td>todos $\ge0$</td></tr>
      </table>
      <h4>Diagnóstico en el tableau final</h4>
      <table style="font-size:.86rem">
        <tr><th class="l">Señal</th><th class="l">Diagnóstico</th></tr>
        <tr><td class="l">básica en $0$</td><td class="l">degenerado</td></tr>
        <tr><td class="l">no básica con $\bar c=0$</td><td class="l">óptimos alternativos</td></tr>
        <tr><td class="l">columna sin positivos</td><td class="l">no acotado</td></tr>
        <tr><td class="l">artificial básica $&gt;0$</td><td class="l">infactible</td></tr>
      </table>
    </div>
  </div>
  <h4>Los cinco chequeos antes de entregar</h4>
  <ol>
    <li>Cada columna básica es un vector de la <b>identidad</b>, con $0$ en la fila CR.</li>
    <li>La columna RHS es <b>no negativa</b> en todas las filas de restricción.</li>
    <li>El valor objetivo evaluado con el <b>enunciado original</b> coincide con la celda.</li>
    <li>$\sum_i y_i b_i = z^*$ (dualidad fuerte).</li>
    <li>Se reportó si hay <b>degeneración</b> u <b>óptimos alternativos</b>.</li>
  </ol>
</section>

<section id="prac">
  <h3>Ejercicios propuestos</h3>

  <h4>P1 — Simplex completo</h4>
  $$\max\;5x_1+4x_2\qquad\text{s.a.}\quad 6x_1+4x_2\le24,\quad x_1+2x_2\le6,\quad x\ge0$$
  <p><b>a)</b> Estandarice y arme el Tableau 0. <b>b)</b> Itere hasta el óptimo. <b>c)</b> Lea $x^*$, $z^*$, los precios sombra y $B^{-1}$. <b>d)</b> Verifique dualidad fuerte.</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> $6x_1+4x_2+s_1=24$, $x_1+2x_2+s_2=6$. Convención A (máximo directo): CR $=(5,4,0,0)$, RHS $=(24,6)$.</p>
  <p><b>b)</b> <i>Iteración 1:</i> entra $x_1$ (CR $=5$); cocientes $24/6=4$ y $6/1=6$ ⟹ sale $s_1$, pivote $6$. Nueva base $\{x_1,s_2\}$: $x_1=4$, $s_2=2$, $z=20$, CR $=(0;\,\frac{2}{3};\,-\frac{5}{6};\,0)$.<br>
  <i>Iteración 2:</i> entra $x_2$ (CR $=\frac23&gt;0$); columna de $x_2$ es $(\frac23,\frac43)$, cocientes $4/\frac23=6$ y $2/\frac43=\mathbf{1{,}5}$ ⟹ sale $s_2$. Nueva base $\{x_1,x_2\}$.</p>
  <p><b>c)</b> $x^*=(3,\,1{,}5)$, $z^*=15+6=\mathbf{21}$. Ambas restricciones activas: $18+6=24$ ✓ y $3+3=6$ ✓. Precios sombra: de $5=6y_1+y_2$ y $4=4y_1+2y_2$ se obtiene $y^*=\left(\tfrac{3}{4},\,\tfrac{1}{2}\right)$. Y
  $$B=\begin{pmatrix}6&4\\1&2\end{pmatrix},\qquad B^{-1}=\frac{1}{8}\begin{pmatrix}2&-4\\-1&6\end{pmatrix}=\begin{pmatrix}0{,}25&-0{,}5\\-0{,}125&0{,}75\end{pmatrix}$$</p>
  <p><b>d)</b> $24\left(\tfrac34\right)+6\left(\tfrac12\right)=18+3=21=z^*$ ✓.</p>
  </details>

  <h4>P2 — Completar el tableau</h4>
  <p>Para el problema $\max\,3x_1+5x_2$ s.a. $x_1\le4$, $2x_2\le12$, $3x_1+2x_2\le18$, se entrega este tableau (convención A):</p>
  <div class="scroll"><table class="tab">
    <tr><th>Base</th><th>$x_1$</th><th>$x_2$</th><th>$s_1$</th><th>$s_2$</th><th>$s_3$</th><th>RHS</th></tr>
    <tr><td class="cr">CR</td><td class="cr">3</td><td class="cr">0</td><td class="cr">0</td><td class="cr">$\alpha$</td><td class="cr">0</td><td class="cr">$\gamma$</td></tr>
    <tr><td>$s_1$</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>4</td></tr>
    <tr><td>$x_2$</td><td>0</td><td>1</td><td>0</td><td>0,5</td><td>0</td><td>$\beta$</td></tr>
    <tr><td>$s_3$</td><td>3</td><td>0</td><td>0</td><td>−1</td><td>1</td><td>6</td></tr>
  </table></div>
  <p><b>a)</b> Encuentre $\alpha,\beta,\gamma$. <b>b)</b> ¿Es óptimo? <b>c)</b> Si no, haga una iteración más.</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> $\beta$: de la fila de $x_2$, $2x_2=12$ ⟹ $\beta=6$. $\gamma=3(0)+5(6)=30$. $\alpha$: es el CR de $s_2$, que en la convención A vale $-y_2$; como $c_B=(0,5,0)$ y la columna de $s_2$ es $(0;\,0{,}5;\,-1)$, se tiene $\bar c_{s_2}=0-5(0{,}5)=\boldsymbol{-2{,}5}$.</p>
  <p><b>b)</b> <b>No.</b> El CR de $x_1$ es $+3&gt;0$ y estamos en la convención de máximo directo (se para con todos $\le0$).</p>
  <p><b>c)</b> Entra $x_1$; columna $(1,\,0,\,3)$; cocientes $4/1=4$ y $6/3=\mathbf{2}$ ⟹ sale $s_3$, pivote $3$. Queda $x_1=2$, $x_2=6$, $s_1=2$, y $z^*=6+30=\mathbf{36}$. Ese sí es el óptimo (los CR quedan $0;\,0;\,0;\,-1{,}5;\,-1$).</p>
  </details>

  <h4>P3 — Diagnóstico rápido</h4>
  <p>Para cada tableau final, diga qué está pasando y qué haría.</p>
  <p><b>a)</b> Todos los CR $\le0$ (convención A) y una variable básica vale $0$. <b>b)</b> Entra $x_2$ y su columna es $(-3,\,-1,\,-2)^\top$. <b>c)</b> Todos los CR $\le0$ y la no básica $x_3$ tiene $\bar c_3=0$. <b>d)</b> Terminó la Fase I con $\sum\alpha_i=4$.</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Óptimo <b>degenerado</b>. Es válido; conviene mencionar que los precios sombra pueden no ser únicos.</p>
  <p><b>b)</b> Ningún elemento positivo ⟹ no hay razón mínima ⟹ <b>problema no acotado</b>. En un modelo de negocio esto casi siempre significa que <b>falta una restricción</b> (una capacidad, un límite de demanda).</p>
  <p><b>c)</b> <b>Óptimos alternativos.</b> Hacer una iteración más entregando $x_3$ a la base da otro punto con el mismo $z^*$; todo el segmento entre ambos es óptimo.</p>
  <p><b>d)</b> El mínimo de la Fase I es $&gt;0$, luego no existe forma de expulsar todas las artificiales: <b>el problema es infactible</b>. Hay que revisar el modelo.</p>
  </details>

  <h4>P4 — De $B^{-1}$ al tableau</h4>
  <p>Para $\max\,4x_1+3x_2$ s.a. $2x_1+x_2\le10$, $x_1+x_2\le7$, $x_1\le4$, considere la base $\{x_1,x_2,s_3\}$.</p>
  <p><b>a)</b> Escriba $B$ y calcule $B^{-1}$. <b>b)</b> Obtenga $x_B$, $z$ y los precios sombra sin iterar. <b>c)</b> ¿Es óptima?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> Columnas: $x_1\to(2,1,1)^\top$, $x_2\to(1,1,0)^\top$, $s_3\to(0,0,1)^\top$.
  $$B=\begin{pmatrix}2&1&0\\1&1&0\\1&0&1\end{pmatrix},\qquad B^{-1}=\begin{pmatrix}1&-1&0\\-1&2&0\\-1&1&1\end{pmatrix}$$</p>
  <p><b>b)</b> $x_B=B^{-1}(10,7,4)^\top=(3,\,4,\,1)^\top$, o sea $x_1=3$, $x_2=4$, $s_3=1$. Con $c_B=(4,3,0)$: $z=12+12=\mathbf{24}$ y $y^\top=c_B^\top B^{-1}=(4-3,\;-4+6,\;0)=(1,\,2,\,0)$.</p>
  <p><b>c)</b> Sí. Los costos reducidos de las no básicas $s_1,s_2$ son $0-y_1=-1$ y $0-y_2=-2$, ambos $\le0$ (convención A) ⟹ <b>óptimo</b>. Chequeo: $10(1)+7(2)+4(0)=24$ ✓. Es el Molino Del Sur del recurso de <b>Primal y Dual</b>.</p>
  </details>

  <h4>P5 — ¿Cuántas iteraciones?</h4>
  <p><b>a)</b> Un LP tiene 8 variables y 5 restricciones $\le$. ¿Cuántas variables tiene la forma estándar y cuántas bases hay a lo más? <b>b)</b> ¿Cuántas variables son básicas en cada iteración? <b>c)</b> Si el Simplex visitara todas las bases, ¿sería un método práctico?</p>
  <details><summary>Ver solución</summary>
  <p><b>a)</b> $8+5=\mathbf{13}$ variables ($8$ originales $+$ $5$ holguras), $m=5$ ecuaciones. Bases posibles: $\binom{13}{5}=\mathbf{1287}$.</p>
  <p><b>b)</b> Siempre $m=\mathbf{5}$ básicas; las otras $8$ son no básicas y valen $0$.</p>
  <p><b>c)</b> No. Con 1287 bases todavía sería abordable, pero el número crece de forma explosiva: con 50 variables y 20 restricciones ya son $\approx4{,}7\times10^{13}$. La gracia del Simplex es que <b>solo visita bases que mejoran</b>, y en la práctica le bastan del orden de $2m$ a $3m$ iteraciones.</p>
  </details>
</section>

<footer>
  <b>IIP314W-2 · Optimización Aplicada a Negocios · 2026-T2</b><br>
  Universidad del Desarrollo · Profesor Rodrigo Trigo Vilches · Ayudante Vicente Ramírez<br>
  Recurso de estudio — Método Simplex: Tableau y Matricial
</footer>
</body>
</html>
"""

HTML = HEAD + B1 + B2 + B3 + X1 + X2 + X3 + X4 + X5 + GUR

OUT = r"C:\Users\raalv\__Ayudantía Opti Inf\2026-T2\Recursos\Recurso_Simplex_Tableau_Matricial.html"
HTML, _informe = postproceso(HTML)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("escrito:", OUT, len(HTML) // 1024, "KB")
