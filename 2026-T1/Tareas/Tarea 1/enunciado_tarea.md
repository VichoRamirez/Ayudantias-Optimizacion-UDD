# Tarea: Optimización con Métodos de Gradiente Descendente

---

## Ejercicio: Optimización de una Función Multi-Modal

**En parejas o grupos de 3** (ni más ni menos) considere la siguiente función de dos variables, que posee exactamente cuatro mínimos locales bien diferenciados:

$$ f(x, y) = -e^{-(x-1)^2-(y-1)^2} - 0.8e^{-(1.5x+1.5)^2-(y+0.5)^2}- 0.9e^{-(x-2)^2-(2y+2)^2} - 1.1e^{-(1.5x-4.5)^2-(0.7y-2)^2} $$

Esta función está compuesta por la suma de cuatro gaussianas invertidas (negativas), cada una centrada en un punto diferente del plano. Esto crea cuatro valles locales claros y profundos, proporcionando un excelente caso de estudio para analizar cómo diferentes métodos de optimización convergen a distintos mínimos dependiendo del punto inicial.

---

### Desarrollo:

**Parte A: Análisis Gráfico**
1. Visualice la función en una gráfica 3D para identificar la estructura de sus mínimos locales.
2. Genere un mapa de curvas de nivel para mejor comprensión de los valles y regiones planas.

**Parte B: Gradiente Descendente con Paso Fijo**
1. Implemente el algoritmo de gradiente descendente con un tamaño de paso fijo.
2. Pruebe con al menos 4 puntos iniciales diferentes, seleccionados estratégicamente en distintas regiones del dominio.
3. Registre el mínimo local encontrado y el valor de la función en cada caso.
4. Visualice las trayectorias de convergencia en el mapa de curvas de nivel.

**Parte C: Gradiente Descendente con Dirección Normalizada**
1. Implemente el algoritmo de gradiente descendente con dirección normalizada.
2. Use los mismos puntos iniciales que en la Parte B.
3. Registre el mínimo local encontrado y el valor de la función en cada caso.
4. Visualice las trayectorias de convergencia en el mapa de curvas de nivel.

**Parte D: Método de Newton-Raphson**
1. Investigue del método Newton Raphson para encontrar raíces de una función, y úsela para encontrar los puntos críticos.
2. Al igual que los dos métodos anteriores, use los mismos puntos iniciales.
3. Registre el mínimo local encontrado y el valor de la función en cada caso.
4. Visualice las trayectorias de convergencia en el mapa de curvas de nivel.

**Parte E: Análisis Comparativo**
1. En un gráfico comparativo (lado a lado o en vertical), muestre las trayectorias de los 3 métodos partiendo desde los mismos puntos iniciales.
2. Analice las diferencias en términos de:
   - Número de iteraciones hasta convergencia.
   - Sensibilidad al tamaño del paso.
   - Robustez ante distintos puntos iniciales.
   - Diferencia entre los mínimos locales reales y los encontrados (Gap).

---

### Informe:
**Estructura mínima**

Un informe siempre debe tener, por lo menos:
* Introducción: Descripción del problema (_Pueden definir objetivos generales y especificos aquí, por esta vez_)
* Objetivos (_opcional_): Si no se definen objetivos en la introducción, pueden tener su sección aparte, con objetivos generales y específicos.
* Marco teórico o conceptos importantes: Definir los conceptos importantes que se utilizarán, tales como el aprendizaje, gradiente, tolerancia, entre otros.
* Desarrollo o métodología: Aquí definen cómo van a realizar la tarea/experimento/problemática, explicando de inicio a fin lo usado.
* Resultados: Aquí entregan los resultados puros y duros (iteraciones por método, Gap, tabla comparativa, gráficos). 
    > Ojo: Son **Resultados**, aquí no van interpretaciones.
* Conclusiones: aquí concluyen respecto a como percibieron la importancia de los parámetros, si cumplieron sus objetivos, etc. Algunos pueden encontrar poco significativos algunos parámetros que otros no, sean específicos (no quiero conclusiones generales como "Los parametros son muy importantes" o "los modelos funcionan").

**Formalidades**
* Tipo de letra: el que estimen conveniente dentro de las típicas (Times New Roman, Arial u otra)
* Tamaño de letra: 12
* Texto Justificado

Se pueden extender lo que necesiten, pero por favor, sean breves en sus explicaciones. No es necesario rellenar con "chamuyo". Sean directos y tajantes. Prefiero un análisis breve que sea directo y correcto, que un análisis de 5 párrafos que sea principalmente relleno.

---

### Entregables:
- Código en un Jupyter Notebook (.ipynb) comentado con las tres implementaciones, los gráficos solicitados y la tabla resumen con resultados para cada punto inicial. Por ejemplo (lo pueden usar, aunque si estiman conveniente, pueden agregar más campos):

La pueden copiar en markdown desde aquí:
```markdown
|punto inicial|minimo local encontrado|minimo local real|gap|iteraciones|
|---|---|---|---|---|
|(X0,Y0)|(Xa,Ya)|(Xb,Yb)|m%|n|
```
Y se vería así similar a lo siguiente:
|punto inicial|minimo local encontrado|minimo local real|gap|iteraciones|
|---|---|---|---|---|
|(X0,Y0)|(Xa,Ya)|(Xb,Yb)|m%|n|

- Informe con la estructura mínima requerida.

La fecha de entrega, en primera instancia, sería el Domingo 22 de Marzo

---

### A modo de ayuda

* Pueden usar softwares para derivar y encontrar los puntos reales, o lo pueden hacer a mano. En cualquier caso, debe quedar plasmado en el informe.
* Si la función se ve mal en el enunciado, peguenla en su jupyter notebook, en una celda markdown, y debería verse bien:
```markdown
$$ f(x, y) = -e^{-(x-1)^2-(y-1)^2} - 0.8e^{-(1.5x+1.5)^2-(y+0.5)^2}- 0.9e^{-(x-2)^2-(2y+2)^2} - 1.1e^{-(1.5x-4.5)^2-(0.7y-2)^2} $$
```