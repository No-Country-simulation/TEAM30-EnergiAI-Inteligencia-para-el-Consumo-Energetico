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