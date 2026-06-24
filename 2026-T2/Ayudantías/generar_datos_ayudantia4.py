# -*- coding: utf-8 -*-
"""
Generador de datos para la Ayudantia 4 (IIP314W - Modelamiento LP).

Crea archivos CSV con datos ALEATORIOS pero CONSISTENTES (con solucion factible
garantizada) para los dos ejercicios de modelamiento:

  Ejercicio 1 - Planificacion de entrenamiento militar (minimizar costos).
  Ejercicio 2 - Distribucion logistica de una empresa de helados (maximizar ingresos).

Los CSV se escriben en la carpeta  datos_ayudantia4/  (junto a este script).

Uso:
    py -3.13 generar_datos_ayudantia4.py

La factibilidad del Ejercicio 1 se garantiza CONSTRUYENDO primero una asignacion
factible y luego fijando las cotas de los recursos por sobre (o por debajo, segun
corresponda) del uso de esa asignacion. El Ejercicio 2 es factible trivialmente
(x = 0) y su optimo es no trivial porque precios y capacidades son positivos.
"""
import os
import csv
import numpy as np

SEED = 314                      # semilla fija -> datos reproducibles (codigo del curso)
rng = np.random.default_rng(SEED)

AQUI = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(AQUI, "datos_ayudantia4")
os.makedirs(DATA, exist_ok=True)


def escribir_csv(nombre, encabezado, filas):
    ruta = os.path.join(DATA, nombre)
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(encabezado)
        w.writerows(filas)
    print(f"  escrito: {nombre}  ({len(filas)} filas)")


# =====================================================================
# EJERCICIO 1 - Entrenamiento militar (minimizar costos)
# =====================================================================
print("Ejercicio 1 - entrenamiento militar:")

aeronaves = ["Caza", "Helicoptero", "Transporte"]
misiones = ["Navegacion", "Tiro", "Asalto"]

# Compatibilidad aeronave -> misiones que puede realizar
compat = {
    "Caza":        ["Navegacion", "Tiro"],
    "Helicoptero": ["Navegacion", "Tiro", "Asalto"],
    "Transporte":  ["Navegacion", "Asalto"],
}

# Requerimientos de horas de certificacion por mision (parametro r_j)
r = {
    "Navegacion": int(rng.integers(90, 140)),
    "Tiro":       int(rng.integers(45, 75)),
    "Asalto":     int(rng.integers(35, 60)),
}

# --- Construccion de una asignacion factible x_feas (garantiza factibilidad) ---
horas = {a: 0.0 for a in aeronaves}     # horas totales por aeronave
x_feas = {}                             # (aeronave, mision) -> horas
for j in misiones:
    elegibles = [a for a in aeronaves if j in compat[a]]
    w = rng.random(len(elegibles))
    w = w / w.sum()
    for a, wi in zip(elegibles, w):
        h = r[j] * float(wi)
        x_feas[(a, j)] = h
        horas[a] += h

# Parametros tecnicos / economicos de cada aeronave
fuel = {"Caza": int(rng.integers(2600, 3400)),     # combustible [L/h]
        "Helicoptero": int(rng.integers(700, 1000)),
        "Transporte": int(rng.integers(1300, 1800))}
oper = {"Caza": int(rng.integers(3500, 4500)),     # operacion/mantencion [$/h]
        "Helicoptero": int(rng.integers(1200, 1800)),
        "Transporte": int(rng.integers(1800, 2400))}
mproj = {"Caza": int(rng.integers(400, 600)),      # proyectiles [unid/h] en tiro
         "Helicoptero": int(rng.integers(250, 350)),
         "Transporte": 0}
ammo = {("Caza", "Tiro"): int(rng.integers(7000, 9000)),       # municiones [$/h]
        ("Helicoptero", "Tiro"): int(rng.integers(2500, 3500))}
precio_comb = round(float(rng.uniform(1.2, 1.8)), 2)           # [$/L]

# Cotas de recursos fijadas a partir de la asignacion factible (con holgura)
H = {a: int(np.ceil(horas[a] * rng.uniform(1.10, 1.40))) for a in aeronaves}
fuel_used = sum(fuel[a] * sum(x_feas[(a, j)] for j in compat[a]) for a in aeronaves)
Q = int(np.ceil(fuel_used * rng.uniform(1.05, 1.25)))          # combustible total [L]
proj_used = sum(mproj[a] * x_feas.get((a, "Tiro"), 0.0) for a in aeronaves)
S = int(np.ceil(proj_used * rng.uniform(1.05, 1.30)))          # stock de municiones [unid]
Hmin_caza = int(np.floor(horas["Caza"] * rng.uniform(0.60, 0.90)))  # horas minimas de caza

# Horas minimas por aeronave (solo la caza tiene un piso de certificacion > 0)
Hmin = {"Caza": Hmin_caza, "Helicoptero": 0, "Transporte": 0}

# --- Escritura de CSV ---
escribir_csv(
    "mil_aeronaves.csv",
    ["aeronave", "f", "o", "H", "m", "Hmin"],
    [[a, fuel[a], oper[a], H[a], mproj[a], Hmin[a]] for a in aeronaves],
)
escribir_csv(
    "mil_misiones.csv",
    ["mision", "r"],
    [[j, r[j]] for j in misiones],
)
escribir_csv(
    "mil_compat.csv",
    ["aeronave", "mision", "a"],
    [[a, j, ammo.get((a, j), 0)] for a in aeronaves for j in compat[a]],
)
escribir_csv(
    "mil_escalares.csv",
    ["parametro", "valor"],
    [["precio_combustible", precio_comb],
     ["combustible_total", Q],
     ["stock_municiones", S]],
)


# =====================================================================
# EJERCICIO 2 - Empresa de helados (maximizar ingresos)
# =====================================================================
print("Ejercicio 2 - empresa de helados:")

productos = ["Premium", "Clasico"]
plantas = ["Santiago", "Concepcion"]
mercados = ["Norte", "Centro", "Sur"]

# Precio de venta por (producto, mercado)  [miles de $ / caja]   -> ingresos
precio = {}
for i in mercados:
    precio[("Premium", i)] = int(rng.integers(26, 33))
    precio[("Clasico", i)] = int(rng.integers(14, 19))

# Capacidad de produccion por (producto, planta)  [cajas]
C = {}
for k in plantas:
    C[("Premium", k)] = int(rng.integers(2500, 4500))
    C[("Clasico", k)] = int(rng.integers(4000, 6500))

# Demanda maxima por (producto, mercado)  [cajas]
D = {}
for i in mercados:
    D[("Premium", i)] = int(rng.integers(1800, 3500))
    D[("Clasico", i)] = int(rng.integers(3000, 4800))

# Volumen por caja  [m3]
v = {"Premium": round(float(rng.uniform(0.045, 0.060)), 3),
     "Clasico": round(float(rng.uniform(0.035, 0.050)), 3)}

# Capacidad de la flota refrigerada por planta  [m3]
# Se fija como una fraccion del volumen maximo producible -> la logistica es un
# cuello de botella interesante, pero el problema sigue siendo factible (x = 0).
maxvol = {k: sum(v[p] * C[(p, k)] for p in productos) for k in plantas}
L = {k: int(np.ceil(maxvol[k] * rng.uniform(0.45, 0.70))) for k in plantas}

escribir_csv(
    "helados_precios.csv",
    ["producto", "mercado", "precio"],
    [[p, i, precio[(p, i)]] for p in productos for i in mercados],
)
escribir_csv(
    "helados_produccion.csv",
    ["producto", "planta", "capacidad"],
    [[p, k, C[(p, k)]] for p in productos for k in plantas],
)
escribir_csv(
    "helados_demanda.csv",
    ["producto", "mercado", "demanda"],
    [[p, i, D[(p, i)]] for p in productos for i in mercados],
)
escribir_csv(
    "helados_volumen.csv",
    ["producto", "volumen"],
    [[p, v[p]] for p in productos],
)
escribir_csv(
    "helados_flota.csv",
    ["planta", "capacidad_m3"],
    [[k, L[k]] for k in plantas],
)

print("\nListo. CSV generados en:", DATA)
