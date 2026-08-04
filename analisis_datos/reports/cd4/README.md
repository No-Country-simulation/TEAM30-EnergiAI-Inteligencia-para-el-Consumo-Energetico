# Documentación CD4
# EnergiAI – Inteligencia para el Consumo Energético

## Hackathon ONE G9 – Alura + Oracle

Esta carpeta contiene la documentación técnica elaborada por el **Científico de Datos 4 (CD4)** correspondiente al desarrollo del microservicio de Inteligencia Artificial del proyecto **EnergiAI**.

---

# Objetivo

Documentar el diseño, implementación e integración del microservicio desarrollado en **FastAPI**, encargado de consumir el modelo de Machine Learning, aplicar las reglas de negocio y comunicarse con el Backend desarrollado en **Java Spring Boot**.

---

# Contenido

## API_CONTRACT.md

Define el contrato oficial de integración entre el Backend y el microservicio de IA.

Incluye:

- Endpoint.
- JSON de entrada.
- JSON de salida.
- Validaciones.
- Manejo de errores.
- Flujo de procesamiento.
- Compatibilidad entre versiones.

---

## BUSINESS_RULES.md

Documenta todas las reglas de negocio implementadas dentro del microservicio.

Incluye:

- Cálculo del costo estimado mensual.
- Cálculo del ahorro potencial mensual.
- Cálculo del ahorro potencial anual.
- Motor de recomendaciones.
- Explicaciones generadas por el sistema.
- Configuración de parámetros.

---

## REPORTE_CD4.md

Informe técnico del trabajo desarrollado por el Científico de Datos 4.

Incluye:

- Objetivos.
- Arquitectura implementada.
- Integración del modelo.
- Decisiones arquitectónicas.
- Buenas prácticas aplicadas.
- Resultados obtenidos.
- Trabajo futuro.

---

# Arquitectura implementada

```text
Cliente

        │

        ▼

Backend Spring Boot

        │

POST /analisis-energetico

        │

        ▼

Microservicio FastAPI

        │

        ├── Validación
        ├── Predicción
        ├── Reglas de negocio
        └── Respuesta JSON

        │

        ▼

Backend
```

---

# Tecnologías utilizadas

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- Scikit-learn
- Joblib
- Logging
- PEP 8
- Arquitectura por capas

---

# Principios aplicados

Durante el desarrollo del microservicio se aplicaron las siguientes buenas prácticas:

- Arquitectura limpia.
- Separación de responsabilidades.
- Código reutilizable.
- Configuración desacoplada.
- Tipado estático.
- Docstrings en español.
- Logging centralizado.
- Manejo de excepciones.
- Validación de datos.
- Preparación para futuras versiones del modelo.

---

# Entregables CD4

| Documento | Descripción |
|-----------|-------------|
| API_CONTRACTO.md | Contrato oficial de integración con Backend |
| REGLAS_NEGOCIO.md | Documento de reglas de negocio |
| REPORTE_CD4.md | Informe técnico del desarrollo |
| README.md | Índice de la documentación |

---

# Estado del proyecto

Estado del microservicio:

- Arquitectura implementada.
- Modelo de Machine Learning integrado.
- Reglas de negocio implementadas.
- Contrato de integración documentado.
- Documentación técnica finalizada.

---

# Responsable

**Científico de Datos 4 (CD4)**

Proyecto:

**EnergiAI – Inteligencia para el Consumo Energético**

Hackathon ONE G9 – Alura + Oracle

---