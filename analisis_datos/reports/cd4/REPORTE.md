# Reporte Técnico CD4
# EnergiAI – Inteligencia para el Consumo Energético

**Hackathon ONE G9 – Alura + Oracle**

**Responsable:** Científico de Datos 4 (CD4)

**Fecha:** Agosto 2026

---

# 1. Introducción

Como parte del proyecto **EnergiAI – Inteligencia para el Consumo Energético**, el rol de CD4 consistió en desarrollar el microservicio de Inteligencia Artificial encargado de integrar el modelo de Machine Learning con el Backend del sistema.

El microservicio fue implementado utilizando **FastAPI**, siguiendo una arquitectura en capas que facilita el mantenimiento, la escalabilidad y la integración con otros componentes del proyecto.

A diferencia de las etapas anteriores del proyecto, el objetivo de esta fase no fue entrenar un modelo de Machine Learning, sino consumir el modelo generado por CD3, aplicar reglas de negocio y devolver una respuesta enriquecida al Backend.

---

# 2. Objetivos

## Objetivo general

Desarrollar un microservicio de Inteligencia Artificial preparado para producción que permita consumir un modelo de Machine Learning desde un Backend desarrollado en Java Spring Boot.

## Objetivos específicos

- Integrar el modelo entrenado.
- Validar las solicitudes recibidas.
- Ejecutar la predicción.
- Aplicar reglas de negocio.
- Calcular métricas económicas.
- Generar recomendaciones.
- Documentar la API.
- Preparar el microservicio para futuras versiones del modelo.

---

# 3. Responsabilidades de CD4

Las responsabilidades asignadas fueron:

- Desarrollo del microservicio utilizando FastAPI.
- Integración del modelo entrenado.
- Implementación de reglas de negocio.
- Cálculo del costo energético.
- Estimación del ahorro potencial.
- Generación de recomendaciones.
- Documentación técnica.
- Definición del contrato de integración con Backend.

---

# 4. Arquitectura implementada

El microservicio fue diseñado utilizando una arquitectura por capas con separación de responsabilidades.

```text
Cliente

        │

        ▼

Spring Boot

        │

POST /analisis-energetico

        ▼

Router

        │

        ▼

Prediction Service

        │

        ▼

Business Service

        │

        ▼

Respuesta JSON
```

Esta arquitectura permite reemplazar el modelo de Machine Learning sin modificar la lógica de negocio ni el contrato de integración.

---

# 5. Integración del modelo

Durante el desarrollo inicial del microservicio aún no se disponía del modelo entrenado.

Por esta razón se implementó un **predictor simulado (Mock Predictor)** que permitió construir y probar toda la arquitectura antes de recibir el archivo definitivo.

Posteriormente se integró el modelo:

```
modelo_iee_gradient_boosting.pkl
```

utilizando la biblioteca **Joblib**.

---

# 6. Decisión arquitectónica

Durante la integración del modelo se verificó que la inferencia únicamente devuelve:

- Categoría.
- Probabilidad.

Inicialmente se contempló incluir el **Índice de Eficiencia Energética (IEE)** dentro de la respuesta de la API.

Sin embargo, tras analizar el notebook de entrenamiento se comprobó que el IEE fue utilizado únicamente para construir la variable objetivo del modelo y no forma parte de la salida generada durante la inferencia.

Con el propósito de evitar duplicar la lógica del entrenamiento dentro del microservicio y reducir el acoplamiento entre entrenamiento e inferencia, se decidió eliminar dicho campo del contrato de integración.

Esta decisión fue comunicada al equipo Backend mediante la actualización del documento **API_CONTRACT.md**.

---

# 7. Reglas de negocio implementadas

Después de obtener la predicción del modelo, el microservicio ejecuta las siguientes reglas de negocio:

- Cálculo del costo estimado mensual.
- Cálculo del ahorro potencial mensual.
- Cálculo del ahorro potencial anual.
- Generación de recomendaciones.
- Generación de una explicación del resultado.

Estas reglas permanecen completamente desacopladas del modelo de Machine Learning.

---

# 8. Documentación generada

Como parte del trabajo realizado se elaboraron los siguientes documentos:

- API_CONTRACT.md
- BUSINESS_RULES.md
- REPORTE_CD4.md

Estos documentos permiten facilitar la integración con Backend y el mantenimiento futuro del microservicio.

---

# 9. Buenas prácticas implementadas

Durante el desarrollo del microservicio se aplicaron las siguientes prácticas:

- Arquitectura por capas.
- Separación de responsabilidades.
- Validación mediante Pydantic.
- Tipado estático.
- Docstrings en español.
- Logging centralizado.
- Manejo de excepciones.
- Configuración desacoplada.
- Código reutilizable.
- Cumplimiento de PEP 8.

---

# 10. Pruebas realizadas

Las pruebas funcionales incluyeron:

- Validación de solicitudes.
- Integración del modelo.
- Predicciones utilizando datos de prueba.
- Verificación del contrato JSON.
- Pruebas mediante Insomnia.
- Validación de las reglas de negocio.

Todas las pruebas realizadas fueron satisfactorias.

---

# 11. Resultados

El microservicio desarrollado permite:

- Recibir solicitudes desde el Backend.
- Ejecutar inferencias utilizando el modelo entrenado.
- Aplicar reglas de negocio.
- Generar recomendaciones.
- Calcular métricas económicas.
- Devolver respuestas estructuradas en formato JSON.

La arquitectura implementada facilita futuras actualizaciones del modelo sin modificar el resto del sistema.

---

# 12. Trabajo futuro

Las siguientes mejoras podrán incorporarse en futuras versiones del proyecto:

- Versionado del modelo.
- Registro de inferencias.
- Explainable AI (XAI).
- Monitoreo del modelo.
- Contenerización mediante Docker.
- Despliegue en Oracle Cloud Infrastructure (OCI).
- Integración continua y despliegue continuo (CI/CD).

---

# 13. Conclusiones

El microservicio desarrollado cumple con los objetivos definidos para el rol de CD4.

La arquitectura implementada permite desacoplar el entrenamiento del proceso de inferencia, facilita la integración con el Backend y proporciona una base sólida para la evolución futura del sistema.

La documentación generada asegura una comunicación clara entre los equipos de Ciencia de Datos y Backend, favoreciendo la mantenibilidad y escalabilidad de la solución.

---