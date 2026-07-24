
# ENTREGA CD2 -> CD3

## Sistema Inteligente para el Análisis de Consumo Energético

Este directorio contiene los artefactos preparados por el
Científico de Datos 2 para las etapas posteriores del proyecto.

## DATA

smart_home_train.csv
- Dataset de entrenamiento Smart Home.

smart_home_test.csv
- Dataset de prueba Smart Home.

uci_train.csv
- Dataset de entrenamiento UCI.
- Conserva orden cronológico.

uci_test.csv
- Dataset de prueba UCI.
- Comienza exactamente después del último registro TRAIN.

## REPORTS

reporte_entrega_cd2_cd3.txt
- Documentación metodológica completa del procesamiento realizado.

manifest_cd3.json
- Especificación estructurada de datasets, objetivos, predictores
  y estrategia de partición.

## IMPORTANTE PARA CD3

No volver a realizar la división TRAIN/TEST.

No utilizar variables excluidas como predictores.

Para Smart Home:

Target:
Energy Consumption (kWh)

Para UCI:

Target:
Global_active_power

La partición UCI debe conservarse obligatoriamente en orden temporal
para evitar fuga de información futura.

Los archivos entregados no contienen valores nulos en las variables
finales.

Estado:
CD2 COMPLETADO Y VALIDADO.
