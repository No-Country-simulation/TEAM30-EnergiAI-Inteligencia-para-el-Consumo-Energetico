# README_CD3

## Proyecto

**Hackathon -- Smart Home Energy**

Este paquete corresponde al entregable del **Científico de Datos 2
(CD2)**. El objetivo es proporcionar al equipo CD3 un conjunto de datos
preparado a nivel de hogar para la construcción del Índice de Eficiencia
Energética (IEE) y el entrenamiento del modelo de Machine Learning.

------------------------------------------------------------------------

# Archivos entregados

  -----------------------------------------------------------------------
  Archivo                        Descripción
  ------------------------------ ----------------------------------------
  `smart_home_train.csv`         Conjunto de entrenamiento (80 %).

  `smart_home_test.csv`          Conjunto de prueba (20 %).

  `feature_engineering.ipynb`    Notebook con el proceso completo de
                                 ingeniería de características.

  `diccionario_variables.xlsx`   Definición de variables, metadatos y
                                 reglas de negocio.

  `README_CD3.md`                Guía de uso de los entregables.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Unidad de análisis

Cada fila del dataset representa **un único hogar (Home ID)**.

La información de todos los electrodomésticos pertenecientes a un mismo
hogar fue agregada para obtener una representación compatible con la API
que consumirá el modelo.

------------------------------------------------------------------------

# Variables disponibles

  -----------------------------------------------------------------------
  Variable                       Descripción
  ------------------------------ ----------------------------------------
  Home ID                        Identificador único del hogar. **No debe
                                 utilizarse como predictor.**

  consumo_kwh                    Consumo energético total del hogar.

  cantidad_personas              Número de habitantes del hogar.

  cantidad_equipos               Número de tipos de electrodomésticos
                                 presentes en el hogar.

  temperatura_exterior           Temperatura exterior promedio del hogar.

  uso_horario_pico               Indicador booleano de uso predominante
                                 en horario pico.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Preparación del dataset

Durante el proceso de ingeniería de características se realizaron las
siguientes actividades:

-   Agrupación de registros por `Home ID`.
-   Cálculo del consumo total del hogar.
-   Conservación de la cantidad de personas.
-   Conteo de tipos de electrodomésticos.
-   Promedio de temperatura exterior.
-   Construcción de la variable `uso_horario_pico`.
-   Validación de valores nulos.
-   Verificación de un único registro por hogar.
-   División Train/Test (80/20) con `random_state = 42`.
-   Verificación de ausencia de hogares repetidos entre entrenamiento y
    prueba.

------------------------------------------------------------------------

# Recomendaciones para CD3

1.  Utilizar **únicamente** `smart_home_train.csv` para entrenar el
    modelo.
2.  Reservar `smart_home_test.csv` exclusivamente para evaluación.
3.  Excluir la columna `Home ID` del entrenamiento.
4.  Mantener la estructura de variables para garantizar compatibilidad
    con la API.
5.  Consultar `diccionario_variables.xlsx` antes de realizar nuevas
    transformaciones.

------------------------------------------------------------------------

# Consideraciones

-   No existen valores nulos.
-   Cada hogar aparece una única vez.
-   Los conjuntos Train y Test son mutuamente excluyentes.
-   La estructura del dataset está alineada con la interfaz esperada por
    la API.

------------------------------------------------------------------------

## Responsable

**Equipo CD2 -- Ingeniería de Datos**

Documento preparado para la integración con el equipo CD3.
