# EnergiAI API

Microservicio de inferencia desarrollado por CD4 para el proyecto EnergiAI.

Este servicio será responsable de:

- Validar solicitudes.
- Ejecutar la predicción del modelo de Machine Learning.
- Aplicar reglas de negocio.
- Calcular métricas de impacto.
- Generar recomendaciones.
- Exponer un endpoint REST para el Backend desarrollado en Spring Boot.

## Arquitectura

El microservicio sigue una arquitectura por capas:

- **routers/**: define los endpoints HTTP.
- **services/**: contiene la lógica de predicción y reglas de negocio.
- **schemas/**: modelos de entrada y salida con Pydantic.
- **core/**: configuración y componentes transversales.
- **utils/**: funciones auxiliares reutilizables.
- **tests/**: pruebas del microservicio.

## Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt

## Contrato de datos

El microservicio define sus contratos mediante modelos Pydantic.

### Entrada

- consumo_kwh
- cantidad_personas
- cantidad_equipos
- temperatura_exterior
- uso_horario_pico

### Salida

- categoria
- iee
- probabilidad
- costo_estimado_mensual
- ahorro_potencial_mensual
- ahorro_potencial_anual
- recomendaciones
