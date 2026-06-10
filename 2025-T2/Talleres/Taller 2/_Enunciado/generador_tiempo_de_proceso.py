# Cada grupo debe generar sus propios valores del 
# parametro tiempos de procesos. Estos valores se generan usando  
# el siguiente programa y el número de RUT del ayudante de la sección.
# El programa generará un archivo de texto llamado tiempo_proceso.txt.
# Este archivo separado por comas con todos los valores debe ser usado
# como input en su modelo.

# IMPORTANTE: Debe tener numpy instalado en su distribución de python, si no funciona
#               prueba abrir un terminal e instalarlo usando:
#                   
#                   pip install numpy
#


# Parámetros Iniciales.
# Complete segun corresponda

n_etapas = 10 # Reemplazar por la cantidad de máquinas.
n_trabajos = 7 # Reemplazar por la cantidad de trabajos.

RUT = 21231928 # RUT del ayudante sin verificador, NO CAMBIAR.

######## No necesita modificar nada desde este punto en adelante ######
def generar_tiempos_de_trabajo(n_etapas, n_trabajos , rut):

    import numpy as np
    import os
    randomstate = np.random.RandomState(seed=RUT)
    filename = 'tiempo_proceso.txt'

    maquinas_lista = [i+1 for i in range(n_etapas)]
    trabajos_lista = [f'Trabajo_{i+1}' for i in range(n_trabajos)]
    t_trabajo_en_maquina = {}

    for i in maquinas_lista:
        for j in trabajos_lista:
            t_trabajo_en_maquina[j,i] = randomstate.randint(60, 500+1)

    f = open(filename, 'w', newline='\n')
    f.write('#Trabajo,Etapa,Tiempo\n')
    for key,val in t_trabajo_en_maquina.items():
        f.write(f'{key[0]},{key[1]},{val}\n')

    print(f'Archivo {filename} se ha creado con exito en {os.path.abspath(filename)}')

generar_tiempos_de_trabajo(n_etapas,n_trabajos,RUT)