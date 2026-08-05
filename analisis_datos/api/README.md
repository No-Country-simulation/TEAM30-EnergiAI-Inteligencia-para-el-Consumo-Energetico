# ⚡ EnergiAI API - Microservicio de Inferencia

> Microservicio desarrollado por el **TEAM30** para el proyecto **EnergiAI – Inteligencia para el Consumo Energético**, como parte del Hackathon ONE G9 – Alura + Oracle.

Este microservicio recibe información sobre el consumo energético de una vivienda, ejecuta un modelo de Machine Learning entrenado y aplica reglas de negocio para generar un análisis energético que posteriormente es consumido por el Backend desarrollado en Spring Boot.

---

# 🎯 Funcionalidades

- ✅ Validación de datos de entrada mediante Pydantic.
- 🤖 Inferencia utilizando un modelo de Machine Learning (Gradient Boosting).
- 📊 Cálculo del costo estimado mensual.
- 💰 Cálculo del ahorro potencial mensual y anual.
- 💡 Generación de recomendaciones mediante reglas de negocio.
- 📝 Logging centralizado.
- 🚀 API REST desarrollada con FastAPI.
- 🔌 Integración con Backend desarrollado en Spring Boot.

---

# 🏗️ Arquitectura

El proyecto fue desarrollado siguiendo una arquitectura por capas con separación de responsabilidades.

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

---

# 📂 Estructura del proyecto

| Carpeta | Descripción |
|----------|-------------|
| `routers/` | Endpoints de la API |
| `services/` | Servicios de predicción y reglas de negocio |
| `schemas/` | Modelos Pydantic |
| `core/` | Configuración de la aplicación |
| `exceptions/` | Manejo centralizado de excepciones |
| `utils/` | Utilidades compartidas |
| `tests/` | Pruebas |

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
```

Ingresar al proyecto

```bash
cd analisis_datos/api
```

---

## 2. Crear el entorno virtual

```bash
python -m venv .venv
```

---

## 3. Activar el entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Git Bash

```bash
source .venv/Scripts/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5. Crear el archivo `.env`

Copiar:

```text
.envexample
```

como

```text
.env
```

y completar las variables necesarias.

Ejemplo:

```text
APP_NAME=EnergiAI API

APP_VERSION=1.0.0

ENERGY_PRICE=0.55

EFFICIENT_SAVINGS=0.05

MODERATE_SAVINGS=0.10

INEFFICIENT_SAVINGS=0.20

MODEL_PATH=models/modelo_iee_gradient_boosting.pkl

LOG_LEVEL=INFO
```

---

# ▶️ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```
http://localhost:8000
```

---

# 📚 Documentación interactiva

La API cuenta con documentación automática generada por FastAPI:

- **Swagger UI**: `http://localhost:8000/docs`

## 🖼️ Vistas previas

### Swagger UI
![Swagger UI](./api/assets/image_1.png)
![Swagger UI](./api/assets/image_2.png)
![Swagger UI](./api/assets/image_3.png)
![Swagger UI](./api/assets/image_4.png)

*Interfaz interactiva para probar los endpoints directamente desde el navegador.*

### Insomnia
![Insomnia](./api/assets/image_6.png)
![Insomnia](./api/assets/image_7.png)

*Colección de requests configurada para pruebas en Insomnia.*

---

# 🌐 Endpoint principal

---

# 🌐 Endpoint principal

## POST /analisis-energetico

Recibe los datos del hogar, ejecuta el modelo de Machine Learning, aplica las reglas de negocio y devuelve un análisis energético.

---

# 📥 Entrada

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

# 📤 Respuesta

```json
{
  "categoria": "Moderado",
  "probabilidad": 0.99,
  "costo_estimado_mensual": 231.00,
  "ahorro_potencial_mensual": 23.10,
  "ahorro_potencial_anual": 277.20,
  "recomendaciones": [
    "Reducir el consumo durante los horarios de mayor demanda.",
    "Optimizar el uso de los sistemas de climatización."
  ]
}
```

---

# 🤖 Modelo de Machine Learning

La API consume un modelo previamente entrenado utilizando **Scikit-Learn** y cargado mediante **Joblib**.

Actualmente se integra el modelo:

```text
modelo_iee_gradient_boosting.pkl
```

La responsabilidad del microservicio consiste en:

- cargar el modelo;
- ejecutar la inferencia;
- obtener la categoría y la probabilidad;
- aplicar reglas de negocio;
- devolver una respuesta estructurada al Backend.

El microservicio **no modifica la predicción del modelo**, preservando la separación entre entrenamiento e inferencia.

---

# 📐 Reglas de negocio

Después de la predicción se calculan automáticamente:

- costo estimado mensual;
- ahorro potencial mensual;
- ahorro potencial anual;
- recomendaciones basadas en las variables de entrada.

Las reglas de negocio complementan la respuesta sin alterar el resultado del modelo.

---

# 🛡️ Validaciones

La API valida automáticamente:

- tipos de datos;
- campos obligatorios;
- formato de la solicitud.

Las validaciones son realizadas mediante **Pydantic**.

---

# ⚠️ Manejo de errores

| Código | Descripción |
|---------|-------------|
| 200 | Solicitud procesada correctamente |
| 422 | Error de validación |
| 500 | Error interno del servidor |

Todos los errores son registrados mediante el sistema de logging.

---

# 📋 Logging

El proyecto utiliza un sistema de logging centralizado para registrar:

- inicio de solicitudes;
- carga del modelo;
- ejecución de inferencias;
- aplicación de reglas de negocio;
- errores y excepciones.

Esto facilita el monitoreo y la trazabilidad del microservicio.

---

# ☁️ Despliegue

El proyecto incluye documentación para el despliegue en Oracle Cloud Infrastructure:

- `DEPLOY_OCI.md`
- `DEPLOY_OBJECT_STORAGE.md`

Estas guías describen el proceso de instalación, configuración y ejecución permanente del microservicio utilizando Oracle Linux, Systemd, Nginx y Oracle Object Storage.

---

# 📄 Documentación del proyecto

La carpeta `reports/cd4` contiene la documentación técnica del microservicio:

- `API_CONTRACT.md`
- `BUSINESS_RULES.md`
- `REPORTE_CD4.md`
- `DEPLOY_OCI.md`
- `DEPLOY_OBJECT_STORAGE.md`

---

# 👥 Equipo

Proyecto desarrollado por el **TEAM30** para el Hackathon ONE G9 – Alura + Oracle.