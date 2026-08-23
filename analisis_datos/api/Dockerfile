FROM python:3.10-slim

WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements.txt desde api/
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la API (todo lo que está en api/)
COPY api/ .

COPY models/ /app/models/

# Verificación en tiempo de construcción
RUN echo "Verificando estructura:" && \
    ls -la /app/ && \
    echo "Modelos:" && \
    ls -la /app/models/ && \
    echo "Código de la API:" && \
    ls -la /app/app/

EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]