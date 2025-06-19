FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependencias del sistema y el driver ODBC 18 desde repositorio Ubuntu 20.04
RUN apt-get update \
   && apt-get install -y --no-install-recommends \
   curl gnupg2 unixodbc unixodbc-dev gcc g++ build-essential \
   && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
   && curl -sSL https://packages.microsoft.com/config/ubuntu/20.04/prod.list \
   > /etc/apt/sources.list.d/mssql-release.list \
   && apt-get update \
   && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
   && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copia el resto de la aplicación
COPY . .

# Expone el puerto usado por Gunicorn
EXPOSE 5000

# Comando por defecto
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]