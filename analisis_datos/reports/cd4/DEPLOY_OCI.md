# Guía de Despliegue en Oracle Cloud Infrastructure (OCI)

# EnergiAI – Inteligencia para el Consumo Energético

**Hackathon ONE G9 – Alura + Oracle**

**Autor:** Científico de Datos 4 (CD4)

**Fecha:** Agosto 2026

---

# 1. Objetivo

Este documento describe el procedimiento para desplegar el microservicio de Inteligencia Artificial desarrollado en FastAPI sobre una instancia de Oracle Cloud Infrastructure (OCI).

La guía contempla desde la preparación de la máquina virtual hasta la ejecución permanente del servicio utilizando **Systemd**, permitiendo que el microservicio se reinicie automáticamente ante cualquier reinicio del servidor.

---

# 2. Arquitectura del despliegue

```text
Internet
        │
        ▼
Oracle Cloud Infrastructure
        │
        ▼
Compute Instance (Oracle Linux 9)
        │
        ▼
Nginx
        │
        ▼
Uvicorn
        │
        ▼
FastAPI
        │
        ▼
Prediction Service
        │
        ▼
Business Service
        │
        ▼
Modelo Machine Learning (.pkl)
        │
        ▼
OCI Object Storage
```

---

# 3. Requisitos

Antes de iniciar el despliegue se requiere:

- Cuenta de Oracle Cloud Infrastructure.
- Compute Instance con Oracle Linux 9.
- Acceso SSH.
- Git.
- Python 3.
- Pip.
- Virtual Environment.
- Acceso al repositorio GitHub.
- Modelo entrenado (.pkl).

---

# 4. Conectarse por SSH

Desde la terminal:

```bash
ssh opc@IP_PUBLICA
```

Ejemplo:

```bash
ssh opc@150.xxx.xxx.xxx
```

---

# 5. Actualizar el sistema

```bash
sudo dnf update -y
```

---

# 6. Instalar Git

```bash
sudo dnf install git -y
```

Verificar:

```bash
git --version
```

---

# 7. Instalar Python

```bash
sudo dnf install python3 python3-pip -y
```

Verificar:

```bash
python3 --version
```

---

# 8. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
```

Ingresar:

```bash
cd REPOSITORIO/analisis_datos/api
```

---

# 9. Crear entorno virtual

```bash
python3 -m venv .venv
```

Activar:

```bash
source .venv/bin/activate
```

---

# 10. Actualizar pip

```bash
pip install --upgrade pip
```

---

# 11. Instalar dependencias

```bash
pip install -r requirements.txt
```

Verificar:

```bash
pip list
```

---

# 12. Variables de entorno

Crear el archivo:

```bash
nano .env
```

Contenido:

```text
APP_NAME=EnergiAI API
APP_VERSION=1.0.0

ENERGY_PRICE=0.55

EFFICIENT_SAVINGS=0.05
MODERATE_SAVINGS=0.10
INEFFICIENT_SAVINGS=0.20

MODEL_PATH=/opt/energiai/models/modelo_iee_gradient_boosting.pkl

LOG_LEVEL=INFO
```

Guardar.

---

# 13. Modelo de Machine Learning

## Desarrollo

Durante el desarrollo el modelo se encuentra en:

```text
models/
    modelo_iee_gradient_boosting.pkl
```

---

## Producción

En producción el modelo debe almacenarse en **Oracle Cloud Object Storage**.

Se recomienda descargarlo durante el despliegue hacia:

```text
/opt/energiai/models/
```

quedando:

```text
/opt/energiai/models/modelo_iee_gradient_boosting.pkl
```

De esta manera será posible reemplazar únicamente el modelo sin modificar el código del microservicio.

---

# 14. Probar la API

Ejecutar:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Abrir:

```
http://IP_PUBLICA:8000/docs
```

Verificar que Swagger se encuentre disponible.

---

# 15. Instalar Nginx

```bash
sudo dnf install nginx -y
```

Iniciar:

```bash
sudo systemctl enable nginx
```

```bash
sudo systemctl start nginx
```

Verificar:

```bash
sudo systemctl status nginx
```

---

# 16. Configurar Proxy Reverso

Editar:

```bash
sudo nano /etc/nginx/nginx.conf
```

Agregar:

```nginx
server {

    listen 80;

    server_name _;

    location / {

        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_set_header X-Forwarded-Proto $scheme;

    }

}
```

Guardar.

Verificar:

```bash
sudo nginx -t
```

Reiniciar:

```bash
sudo systemctl restart nginx
```

---

# 17. Crear servicio Systemd

Crear:

```bash
sudo nano /etc/systemd/system/energiai.service
```

Contenido:

```ini
[Unit]
Description=EnergiAI FastAPI Service
After=network.target

[Service]

User=opc

WorkingDirectory=/home/opc/REPOSITORIO/analisis_datos/api

ExecStart=/home/opc/REPOSITORIO/analisis_datos/api/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

Restart=always

RestartSec=5

Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```

Guardar.

---

# 18. Registrar el servicio

```bash
sudo systemctl daemon-reload
```

---

# 19. Habilitar inicio automático

```bash
sudo systemctl enable energiai
```

---

# 20. Iniciar el servicio

```bash
sudo systemctl start energiai
```

---

# 21. Verificar el estado

```bash
sudo systemctl status energiai
```

Debe aparecer:

```text
active (running)
```

---

# 22. Reiniciar el servicio

Cuando exista una nueva versión del código:

```bash
sudo systemctl restart energiai
```

---

# 23. Detener el servicio

```bash
sudo systemctl stop energiai
```

---

# 24. Visualizar los logs

```bash
journalctl -u energiai -f
```

Los registros del microservicio aparecerán en tiempo real.

---

# 25. Actualizar el proyecto

```bash
cd REPOSITORIO
```

```bash
git pull
```

Activar el entorno virtual:

```bash
source analisis_datos/api/.venv/bin/activate
```

Actualizar dependencias si es necesario:

```bash
pip install -r analisis_datos/api/requirements.txt
```

Reiniciar el servicio:

```bash
sudo systemctl restart energiai
```

---

# 26. Actualizar únicamente el modelo

Si se genera una nueva versión del modelo:

1. Reemplazar el archivo:

```text
modelo_iee_gradient_boosting.pkl
```

2. Reiniciar:

```bash
sudo systemctl restart energiai
```

No será necesario modificar el código fuente del microservicio.

---

# 27. Buenas prácticas implementadas

Durante el despliegue se recomienda:

- Utilizar entornos virtuales.
- No ejecutar la aplicación como usuario root.
- Mantener el modelo separado del código fuente.
- Utilizar Object Storage para almacenar modelos.
- Ejecutar la API mediante Systemd.
- Exponer únicamente Nginx hacia Internet.
- Mantener actualizado el sistema operativo.
- Versionar el código mediante Git.

---

# 28. Resultado esperado

Al finalizar el procedimiento el microservicio quedará ejecutándose de forma permanente dentro de Oracle Cloud Infrastructure.

La arquitectura permitirá:

- Reinicio automático del servicio.
- Actualización del modelo sin modificar la API.
- Integración con Backend mediante HTTP.
- Escalabilidad para futuras versiones del modelo.
- Despliegue seguro y mantenible siguiendo buenas prácticas de ingeniería.