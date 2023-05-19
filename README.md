# promo-d-da-modulo3-sprint1-laura-maitane

Este repositorio incluye los ejercicios de Pair Programming de Laura Madrid y Maitane Portilla del Sprint 1 del Módulo 3 (primera evaluación del módulo 3) de la promo D del bootcamp de Data Analytics de Adalab.

La documentación se ha organizado en las siguientes carpetas:
- [**regresion-lineal:**](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/tree/main/regresion-lineal) Recoge los ejercicios de regresión lineal. Incluye los siguientes archivos y carpetas:
    * [***datos***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/tree/main/regresion-lineal/datos): contiene los archivos .csv y .jpeg utilizados/generados en los ejercicios.
    * [***reg-lin-1-machine-learning-intro.ipynb***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/blob/main/regresion-lineal/reg-lin-1-machine-learning-intro.ipynb): contiene los ejercicios de la lección 1 de regresión lineal (EDA del dataset).
- [**regresion-logistica:**](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/tree/main/regresion-logistica) recoge los ejercicios de regresión logística. Incluye los siguientes archivos y carpetas:
    * [***datos***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/tree/main/regresion-logistica/datos): contiene los archivos .csv y .pkl utilizados/generados en los ejercicios.
    * [***reg-log-1-eda.ipynb***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/blob/main/regresion-logistica/reg-log-1-eda.ipynb): contiene los ejercicios de la lección 1 de regresión logística (EDA del dataset).
- [**src:**](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/tree/main/src) Incluye los siguientes archivos para facilitar la lectura de los notebooks:
    * [***soporte_funciones.py***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/blob/main/src/soporte_funciones.py): archivo .py con las funciones utilizadas en los notebooks.
    * [***soporte_variables.py***](https://github.com/Adalab/promo-d-da-modulo3-sprint1-laura-maitane/blob/main/src/soporte_variables.py): archivo .py con las variables de gran tamaño utilizadas en los notebooks.

A continuación se incluye un listado de las librerías utilizadas:
    - pandas
    - numpy
    - warnings
    - sys
    - matplotlib
    - seaborn
    - sklearn

**DESCRIPCIÓN DEL PROCESO:**
---
**1. REGRESIÓN LINEAL:**  

1.1 EXPLORACIÓN:  

En primer lugar hemos procedido a realizar la exploración del dataset tanto de forma analítica como numérica. Entre las actividades más importantes destacan:
- Selección de la variable respuesta
- Selección inicial de variables relevantes
- Renombrado de columnas
- Exploración general de los datos
- Cambio de tipo de datos y desdoblado de las columnas
- Gestión de valores nulos
- Análisis de las variables categóricas y numéricas en relación a la variable respuesta
- Correlación entre las variables numéricas, eliminación de columnas redundantes
- Gestión de outliers
- Guardado del dataset modificado

1.2. ANÁLISIS DETALLADO DE LAS VARIABLES
- Tests estadísticos para la variable respuesta: asimetría, curtosis, normalidad.
- Covarianza y correlación entre variables numéricas
- Asunciones: normalidad de la variable respuesta, independencia y homocedasticidad de las variables predictoras
- ANOVA

1.3. PROCESADO:
- Normalización de la variable respuesta
- Estandarización de variables numéricas
- Encoding de variables categóricas
- Balanceo y codificación de la variable respuesta

1.4. MODELO DE REGRESIÓN LINEAL
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Matriz de confusión
- Cross Validation
- Métricas
- Comparación con otros modelos

1.5. MODELO DE DECISION TREE
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos

1.6. MODELO DE RANDOM FOREST
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos

**2. REGRESIÓN LOGÍSTICA:**  

2.1 EXPLORACIÓN:  
En primer lugar hemos procedido a realizar la exploración del dataset tanto de forma analítica como numérica. Entre las actividades más importantes destacan:
- Selección de la variable respuesta
- Renombrado de columnas
- Exploración general de los datos
- Cambio de tipo de datos de las columnas
- Análisis de las variables categóricas y numéricas en relación a la variable respuesta
- Correlación entre las variables numéricas, eliminación de columnas redundantes
- Gestión de outliers
- Guardado del dataset modificado

2.2. PROCESADO:
- Estandarización de variables numéricas
- Encoding de variables categóricas
- Balanceo y codificación de la variable respuesta

2.3. MODELO DE REGRESIÓN LOGÍSTICA
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Matriz de confusión
- Métricas
- Comparación con otros modelos

2.4. MODELO DE DECISION TREE
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos

2.5. MODELO DE RANDOM FOREST
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos
