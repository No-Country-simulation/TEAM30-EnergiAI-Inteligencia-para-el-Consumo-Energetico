# Contrato de Integración API
# EnergiAI – Inteligencia para el Consumo Energético

**Versión:** 2.0  
**Estado:** Aprobado para integración Backend – IA  
**Responsable:** Científico de Datos 4 (CD4)  
**Microservicio:** FastAPI + Machine Learning  
**Fecha:** Agosto 2026

---

# 1. Objetivo

Este documento define el contrato oficial de integración entre el Backend desarrollado en **Java Spring Boot** y el microservicio de Inteligencia Artificial desarrollado en **FastAPI**.

El objetivo es establecer una interfaz estable, desacoplada y mantenible para la comunicación entre ambos componentes.

---

# 2. Arquitectura de integración

```text
Cliente

        │
        ▼

Spring Boot

        │
POST /analisis-energetico

        ▼

Microservicio FastAPI

        │
        ├── Validación
        ├── Predicción del modelo
        ├── Reglas de negocio
        └── Respuesta JSON

        │
        ▼

Spring Boot

        │
Persistencia

        │
        ▼

Cliente
```

---

# 3. Endpoint

## Método

```http
POST
```

## Ruta

```http
/analisis-energetico
```

## Content-Type

```http
application/json
```

---

# 4. JSON de Entrada

```json
{
    "consumo_kwh": 420,
    "cantidad_personas": 4,
    "cantidad_equipos": 10,
    "temperatura_exterior": 28,
    "uso_horario_pico": true
}
```

---

# 5. Descripción de los parámetros

| Campo | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| consumo_kwh | float | Sí | Consumo mensual de energía en kWh |
| cantidad_personas | integer | Sí | Número de habitantes del hogar |
| cantidad_equipos | integer | Sí | Número de equipos eléctricos |
| temperatura_exterior | float | Sí | Temperatura exterior promedio |
| uso_horario_pico | boolean | Sí | Indica si existe consumo en horario pico |

---

# 6. Validaciones

El microservicio validará:

- Todos los campos son obligatorios.
- consumo_kwh > 0
- cantidad_personas > 0
- cantidad_equipos > 0
- temperatura_exterior debe encontrarse dentro del rango permitido.
- uso_horario_pico debe ser booleano.

Si alguna validación falla se devolverá:

```http
HTTP 422
```

---

# 7. Flujo interno

1. Recepción de la solicitud.
2. Validación de datos.
3. Preparación de la información.
4. Carga del modelo entrenado.
5. Predicción.
6. Obtención de la categoría.
7. Obtención de la probabilidad.
8. Aplicación de reglas de negocio.
9. Construcción de la respuesta.
10. Retorno al Backend.

---

# 8. Respuesta Exitosa

```json
{
    "categoria": "Moderado",
    "probabilidad": 0.99,
    "costo_estimado_mensual": 315.00,
    "ahorro_potencial_mensual": 31.50,
    "ahorro_potencial_anual": 378.00,
    "recomendaciones": [
        "Reducir el consumo durante los horarios pico.",
        "Revisar los equipos con mayor consumo energético.",
        "Optimizar el uso de electrodomésticos."
    ],
}
```

---

# 9. Descripción de la respuesta

| Campo | Tipo | Descripción |
|--------|------|-------------|
| categoria | string | Categoría predicha por el modelo (Eficiente, Moderado o Ineficiente) |
| probabilidad | float | Nivel de confianza de la predicción |
| costo_estimado_mensual | float | Consumo mensual × tarifa configurada |
| ahorro_potencial_mensual | float | Estimación del ahorro mensual |
| ahorro_potencial_anual | float | Estimación del ahorro anual |
| recomendaciones | array[string] | Recomendaciones generadas mediante reglas de negocio |

---

# 10. Respuestas de Error

## Error de validación

```http
HTTP 422
```

```json
{
    "detail": [
        {
            "loc": [
                "body",
                "consumo_kwh"
            ],
            "msg": "El consumo debe ser mayor que cero.",
            "type": "value_error"
        }
    ]
}
```

---

## Error interno

```http
HTTP 500
```

```json
{
    "detail": "Error interno del servidor."
}
```

---

# 11. Reglas de negocio implementadas por CD4

El microservicio aplica las siguientes reglas de negocio posteriores a la predicción del modelo:

- Cálculo del costo estimado mensual.
- Cálculo del ahorro potencial mensual.
- Cálculo del ahorro potencial anual.
- Generación de recomendaciones.
- Generación de una explicación del resultado.

Estas reglas son independientes del modelo de Machine Learning y pueden evolucionar sin necesidad de reentrenar el modelo.

---

# 12. Decisión Arquitectónica

Durante la integración del modelo **modelo_iee_gradient_boosting.pkl** se verificó que el modelo únicamente genera:

- Categoría predicha (`predict()`).
- Probabilidad asociada (`predict_proba()`).

El **Índice de Eficiencia Energética (IEE)** fue utilizado exclusivamente durante el proceso de entrenamiento para construir la variable objetivo del clasificador.

Debido a que el modelo no devuelve dicho índice durante la inferencia, se decidió eliminar el campo **IEE** del contrato de integración.

Esta decisión permite:

- Mantener desacoplados el entrenamiento y la inferencia.
- Evitar duplicar lógica del proceso de entrenamiento.
- Facilitar futuras actualizaciones del modelo sin modificar el contrato de negocio.
- Exponer únicamente información realmente generada por el modelo.

---

# 13. Compatibilidad

**Versión del contrato:** 2.0

Este documento reemplaza cualquier versión anterior que incluya el campo **IEE** dentro de la respuesta del microservicio.

---

# 14. Historial de cambios

| Versión | Fecha | Descripción |
|----------|--------|-------------|
| 1.0 | Julio 2026 | Primera propuesta de integración. |
| 2.0 | Agosto 2026 | Eliminación del campo IEE del contrato tras la integración del modelo real y actualización de la respuesta del microservicio. |

---

# 15. Responsabilidades

## Backend (Spring Boot)

- Consumir el endpoint.
- Validar la comunicación.
- Persistir los resultados.
- Exponer la información al cliente final.

## Microservicio FastAPI (CD4)

- Validar la solicitud.
- Ejecutar el modelo de Machine Learning.
- Aplicar las reglas de negocio.
- Devolver la respuesta estructurada.

---