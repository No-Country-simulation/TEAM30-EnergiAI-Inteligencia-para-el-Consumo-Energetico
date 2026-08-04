# ⚡ EnergiAI API - Microservicio de Inferencia

> Microservicio desarrollado por el **TEAM30** para el proyecto EnergiAI como parte del hackathon.

Este microservicio es el **cerebro inteligente** de la aplicación: recibe datos del hogar, ejecuta predicciones de consumo energético y genera recomendaciones personalizadas para optimizar el uso de electricidad.

---

## 🎯 Funcionalidades principales

- ✅ Validación de datos de entrada
- 🧠 Predicción de categorías de consumo energético
- 📊 Cálculo de métricas de impacto (IEE, costos, ahorros)
- 💡 Generación de recomendaciones personalizadas
- 🔌 Endpoint REST listo para integrarse con el Backend Spring Boot

---

## 🏗️ Arquitectura del Microservicio

El proyecto sigue una arquitectura limpia y modular:

| Carpeta | Propósito |
|---------|-----------|
| `routers/` | Definición de los endpoints HTTP |
| `services/` | Lógica de negocio y predicción |
| `schemas/` | Modelos de datos con Pydantic |
| `core/` | Configuración y componentes transversales |
| `utils/` | Funciones auxiliares reutilizables |
| `tests/` | Pruebas unitarias y de integración |

---

## 🚀 ¿Cómo levantar la API?

### 1. Clonar el repositorio y ubicarse en la carpeta correcta

```bash
 cd analisis_datos/api
```

### 2. Crear el entorno virtual

```bash
 python -m venv .venv
```

### 3. Activar el entorno virtual
**En Git Bash:**
```bash
 source .venv/Scripts/activate
```

**En Windows:**
```bash
 .venv/Scripts/activate
```

### 4. Crear el archivo .env desde .envexample
```text
 cp .envexample .env
```

### 5. Instalar dependencias
```bash
 pip install -r requirements.txt
```

## Ejecución y Documentación de la API

### Ejecutar el servidor
```bash
 uvicorn app.main:app --reload
```
La API estará disponible en: `http://localhost:8000`

## Explorar la documentación interactiva

Una vez levantado el servidor, puedes probar el endpoint desde:

- **Swagger UI:** `http://localhost:8000/docs`


---

## 📦 Contrato de Datos
### Entrada (lo que envías)
```json
{
  "consumo_kwh": 350,
  "cantidad_personas": 4,
  "cantidad_equipos": 8,
  "temperatura_exterior": 28,
  "uso_horario_pico": true
}
```
### Salida (lo que recibes)
```json
{
  "categoria": "Moderado-Eficiente o Ineficiente",
  "iee": 85.3,
  "probabilidad": 0.92,
  "costo_estimado_mensual": 4520.50,
  "ahorro_potencial_mensual": 1200.00,
  "ahorro_potencial_anual": 14400.00,
  "recomendaciones": ["Usar electrodomésticos eficientes", "Aprovechar luz natural"]
}
```
---

## 🤖 Estado del Predictor
Actualmente, el servicio utiliza un predictor simulado (`PredictionService`)
que devuelve respuestas fijas. Esto permite:

- ✅ **Desarrollo paralelo** con el Backend Spring Boot
- ✅ **Pruebas de integración** tempranas
- ✅ **Validación del flujo completo** de la API
**Futuro:** Cuando se entregue el modelo final (`modelo.pkl`), solo se
reemplazará la implementación interna del `PredictionService`. El contrato de
entrada/salida NO cambiará, garantizando cero impacto en el Backend.

---

## 📐 Business Service - Reglas de Negocio
El `BusinessService` complementa la predicción del modelo agregando lógica
de negocio:
| Métrica | Descripción |
|---------|-------------|
| **Costo estimado mensual** | Calculado según el consumo y la tarifa
vigente |
| **Ahorro potencial mensual** | Basado en las recomendaciones aplicadas |
| **Ahorro potencial anual** | Proyección a 12 meses |
| **Recomendaciones** | Lista de acciones personalizadas |
⚠️ *Este servicio no modifica la salida del modelo, solo la enriquece.*

---

## 🌐 Endpoint Principal
### `POST /analisis-energetico`
**Descripción:** Recibe datos del hogar, ejecuta la predicción y devuelve un
análisis energético completo.
**Ejemplo de uso (con cURL):**

```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/analisis-energetico' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "cantidad_equipos": 10,
    "cantidad_personas": 4,
    "consumo_kwh": 420,
    "temperatura_exterior": 28,
    "uso_horario_pico": true
    }'
```

---

## 🛡️ Manejo de Errores
La API implementa un sistema robusto de manejo de excepciones:
| Código | Descripción |
|--------|-------------|
| `422` | Error de validación (datos incorrectos o faltantes) |
| `400` | Solicitud mal formada |
| `500` | Error interno del servidor |
Todos los errores son registrados automáticamente mediante el sistema de
logging.

---

## 📋 Logging
La aplicación utiliza el módulo `logging` de Python con configuración
centralizada. Esto permite:
- 🔍 Monitoreo en tiempo real
- 🐛 Depuración eficiente
- 📊 Trazabilidad de eventos y errores
