# Generador de Datos - Taller 2: Optimización de Red de Suministro Multi-Período
# Cada grupo debe generar sus propios valores usando el número de RUT del ayudante
# El programa generará un archivo CSV llamado datos_inventarios.csv
# Este archivo debe ser usado como input en su modelo de optimización

# IMPORTANTE: Debe tener numpy y pandas instalados. Si no funciona, ejecute:
#               pip install numpy pandas

# Parámetros Iniciales
# Complete según corresponda

RUT = 21231928

######## No necesita modificar nada desde este punto en adelante ######

def generar_datos_inventarios(rut):
    """
    Genera datos para el problema de optimización de red de suministro multi-período.
    
    Los datos incluyen:
    - Capacidades (producción, inventario)
    - Demandas por tienda y período
    - Costos (apertura, producción, transporte, inventario, penalización)
    """
    import numpy as np
    import pandas as pd
    import os
    
    # Configurar generador aleatorio con seed
    randomstate = np.random.RandomState(seed=rut)
    
    # Conjuntos
    plantas = ['P1', 'P2', 'P3', 'P4']
    cds = ['CD1', 'CD2', 'CD3']
    tiendas = ['T1', 'T2', 'T3', 'T4', 'T5']
    periodos = list(range(1, 8))  # 7 días
    
    data_rows = []
    
    # ============= CAPACIDADES DE PLANTAS =============
    # Capacidad de producción por planta y período (en unidades)
    # Varía ligeramente por período para simularidad realismo
    for p in plantas:
        capacidad_base = randomstate.randint(1200, 2000)
        for d in periodos:
            variacion = randomstate.uniform(0.8, 1.2)
            cap_produccion = int(capacidad_base * variacion)
            data_rows.append({
                'tipo': 'CAPACIDAD_PRODUCCION',
                'planta': p,
                'cd': None,
                'tienda': None,
                'periodo': d,
                'valor': cap_produccion
            })
    
    # Capacidad de inventario en plantas (unidades)
    for p in plantas:
        cap_inv = randomstate.randint(3000, 5000)
        data_rows.append({
            'tipo': 'CAPACIDAD_INVENTARIO_PLANTA',
            'planta': p,
            'cd': None,
            'tienda': None,
            'periodo': None,
            'valor': cap_inv
        })
    
    # Capacidad de inventario en CDs (unidades)
    for c in cds:
        cap_inv = randomstate.randint(2000, 3500)
        data_rows.append({
            'tipo': 'CAPACIDAD_INVENTARIO_CD',
            'planta': None,
            'cd': c,
            'tienda': None,
            'periodo': None,
            'valor': cap_inv
        })
    
    # ============= DEMANDAS =============
    # Demanda mínima por tienda y período
    demanda_promedio = randomstate.randint(300, 600)  # promedio general
    for t in tiendas:
        for d in periodos:
            # Agregar variabilidad día a día
            factor_dia = randomstate.uniform(0.7, 1.3)
            factor_tienda = randomstate.uniform(0.8, 1.2)
            demanda = int(demanda_promedio * factor_dia * factor_tienda)
            data_rows.append({
                'tipo': 'DEMANDA_MINIMA',
                'planta': None,
                'cd': None,
                'tienda': t,
                'periodo': d,
                'valor': demanda
            })
    
    # ============= COSTOS DE APERTURA =============
    # Costo fijo de apertura de cada planta (por todo el trimestre)
    for p in plantas:
        costo_apertura = randomstate.randint(15000, 35000)
        data_rows.append({
            'tipo': 'COSTO_APERTURA_PLANTA',
            'planta': p,
            'cd': None,
            'tienda': None,
            'periodo': None,
            'valor': costo_apertura
        })
    
    # ============= COSTOS DE PRODUCCIÓN =============
    # Costo variable de producción ($/unidad)
    # Las plantas tienen diferentes eficiencias
    for p in plantas:
        costo_base = randomstate.uniform(8, 15)  # base diferente por planta
        for d in periodos:
            # Pequeña variación por período
            costo = costo_base * randomstate.uniform(0.95, 1.05)
            data_rows.append({
                'tipo': 'COSTO_PRODUCCION',
                'planta': p,
                'cd': None,
                'tienda': None,
                'periodo': d,
                'valor': round(costo, 2)
            })
    
    # ============= COSTOS DE INVENTARIO EN PLANTAS =============
    # Costo de mantener inventario en planta ($/unidad/día)
    for p in plantas:
        costo = round(randomstate.uniform(0.5, 1.5), 2)
        for d in periodos:
            data_rows.append({
                'tipo': 'COSTO_INVENTARIO_PLANTA',
                'planta': p,
                'cd': None,
                'tienda': None,
                'periodo': d,
                'valor': costo
            })
    
    # ============= COSTOS DE INVENTARIO EN CDS =============
    # Costo de mantener inventario en CD ($/unidad/día)
    for c in cds:
        costo = round(randomstate.uniform(0.3, 0.8), 2)
        for d in periodos:
            data_rows.append({
                'tipo': 'COSTO_INVENTARIO_CD',
                'planta': None,
                'cd': c,
                'tienda': None,
                'periodo': d,
                'valor': costo
            })
    
    # ============= COSTOS DE TRANSPORTE PLANTA -> CD =============
    # Costo de transporte por unidad entre plantas y CDs
    for p in plantas:
        for c in cds:
            for d in periodos:
                # Costo base + variación aleatoria
                costo = round(randomstate.uniform(1.5, 4.5), 2)
                data_rows.append({
                    'tipo': 'COSTO_TRANSPORTE_PLANTA_CD',
                    'planta': p,
                    'cd': c,
                    'tienda': None,
                    'periodo': d,
                    'valor': costo
                })
    
    # ============= COSTOS DE TRANSPORTE CD -> TIENDA =============
    # Costo de transporte por unidad entre CDs y tiendas
    for c in cds:
        for t in tiendas:
            for d in periodos:
                # Costo base (generalmente más bajo que planta->CD)
                costo = round(randomstate.uniform(0.8, 2.5), 2)
                data_rows.append({
                    'tipo': 'COSTO_TRANSPORTE_CD_TIENDA',
                    'planta': None,
                    'cd': c,
                    'tienda': t,
                    'periodo': d,
                    'valor': costo
                })
    
    # ============= COSTO DE DEMANDA INSATISFECHA =============
    # Penalización por cada unidad de demanda no satisfecha (venta perdida + reputación)
    for t in tiendas:
        for d in periodos:
            costo_penalizacion = round(randomstate.uniform(25, 50), 2)
            data_rows.append({
                'tipo': 'COSTO_DEMANDA_INSATISFECHA',
                'planta': None,
                'cd': None,
                'tienda': t,
                'periodo': d,
                'valor': costo_penalizacion
            })
    
    # ============= CREAR DATAFRAME Y GUARDAR =============
    df = pd.DataFrame(data_rows)
    
    # Crear archivo CSV
    filename = 'datos_inventarios.csv'
    df.to_csv(filename, index=False)
    
    print(f'✓ Archivo {filename} creado exitosamente')
    print(f'✓ Ubicación: {os.path.abspath(filename)}')
    print(f'✓ Total de registros: {len(df)}')
    print(f'✓ Tipos de datos incluidos:')
    for tipo in sorted(df['tipo'].unique()):
        count = len(df[df['tipo'] == tipo])
        print(f'    - {tipo}: {count} registros')
    
    return df

# Ejecutar generador
if __name__ == '__main__':
    df = generar_datos_inventarios(RUT)
