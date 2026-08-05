# Guía de Integración del Modelo con Oracle Cloud Object Storage

# EnergiAI – Inteligencia para el Consumo Energético

**Hackathon ONE G9 – Alura + Oracle**

**Autor:** Científico de Datos 4 (CD4)

**Fecha:** Agosto 2026

---

# 1. Objetivo

Este documento describe el procedimiento para almacenar el modelo de Machine Learning en Oracle Cloud Object Storage y utilizarlo desde el microservicio desarrollado en FastAPI.

La estrategia permite desacoplar completamente el código fuente del modelo entrenado, facilitando futuras actualizaciones sin necesidad de modificar la aplicación.

---

# 2. Arquitectura

```text
Científico de Datos

        │

        ▼

Nuevo modelo

modelo_iee_gradient_boosting.pkl

        │

        ▼

Oracle Object Storage

        │

        ▼

Compute Instance OCI

        │

Descarga del modelo

        ▼

/opt/energiai/models/

        │

        ▼

Prediction Service

        │

        ▼

FastAPI
```

---

# 3. Ventajas

Esta estrategia presenta las siguientes ventajas:

- Separación entre código y modelo.
- Actualización del modelo sin modificar la API.
- Versionamiento independiente.
- Despliegue más sencillo.
- Mayor mantenibilidad.
- Escalabilidad.

---

# 4. Crear un Bucket

Ingresar a Oracle Cloud.

Seleccionar:

```text
Storage

↓

Buckets

↓

Create Bucket
```

Ejemplo:

```text
energiai-models
```

---

# 5. Subir el modelo

Subir:

```text
modelo_iee_gradient_boosting.pkl
```

El Bucket quedará similar a:

```text
energiai-models

│

└── modelo_iee_gradient_boosting.pkl
```

---

# 6. Crear un Pre-Authenticated Request (PAR)

Seleccionar el archivo.

Crear un:

```text
Pre-Authenticated Request
```

Con permisos:

- Read

Obtener una URL similar a:

```text
https://objectstorage.sa-santiago-1.oraclecloud.com/p/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Esta URL permitirá descargar el modelo sin exponer credenciales dentro del microservicio.

---

# 7. Preparar el servidor

Crear la carpeta donde se almacenará el modelo:

```bash
sudo mkdir -p /opt/energiai/models
```

Asignar permisos:

```bash
sudo chown opc:opc /opt/energiai/models
```

---

# 8. Descargar el modelo

Desde la instancia ejecutar:

```bash
wget "URL_DEL_PAR" \
-O /opt/energiai/models/modelo_iee_gradient_boosting.pkl
```

Verificar:

```bash
ls /opt/energiai/models
```

Debe aparecer:

```text
modelo_iee_gradient_boosting.pkl
```

---

# 9. Configurar la API

Modificar el archivo `.env`:

```text
MODEL_PATH=/opt/energiai/models/modelo_iee_gradient_boosting.pkl
```

No será necesario modificar el código fuente.

---

# 10. Reiniciar el servicio

```bash
sudo systemctl restart energiai
```

---

# 11. Actualizar el modelo

Cuando exista una nueva versión del modelo:

1. Subir el nuevo archivo al Bucket.
2. Reemplazar el archivo existente.
3. Descargar nuevamente en la instancia.

```bash
wget "URL_DEL_PAR" \
-O /opt/energiai/models/modelo_iee_gradient_boosting.pkl
```

4. Reiniciar el servicio.

```bash
sudo systemctl restart energiai
```

La API utilizará automáticamente el nuevo modelo.

---

# 12. Flujo de actualización

```text
Nuevo entrenamiento

        │

        ▼

Nuevo modelo .pkl

        │

        ▼

Object Storage

        │

        ▼

Descarga en OCI

        │

        ▼

Reinicio del servicio

        │

        ▼

Nueva versión disponible
```

---

# 13. Buenas prácticas

Durante la administración del modelo se recomienda:

- No almacenar el modelo dentro del repositorio Git.
- Mantener un único archivo activo por versión.
- Conservar versiones anteriores para recuperación.
- Utilizar Object Storage como repositorio central de modelos.
- Reiniciar el servicio únicamente después de reemplazar el modelo.
- Mantener el código fuente independiente del archivo `.pkl`.

---

# 14. Consideraciones para producción

Para un entorno de producción se recomienda:

- Utilizar OCI CLI en lugar de descargas manuales.
- Automatizar la actualización del modelo mediante scripts.
- Versionar los modelos utilizando nombres como:

```text
modelo_v1.pkl
modelo_v2.pkl
modelo_v3.pkl
```

- Registrar la fecha y versión del modelo desplegado.
- Implementar monitoreo del microservicio y de las inferencias.

---

# 15. Resultado esperado

Con esta arquitectura el microservicio queda desacoplado del modelo entrenado.

La actualización del modelo se limita a reemplazar un único archivo dentro de Oracle Cloud Object Storage y reiniciar el servicio, sin necesidad de recompilar ni modificar el código fuente del proyecto.