FROM python:3.12.3-alpine3.19

WORKDIR /app
# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1  
# Instalación de dependencias y configuración del entorno
RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev && \
    pip install --upgrade pip 

# Copia solo el archivo de requisitos y utiliza Poetry para instalar dependencias
# Copia el archivo de requisitos desde el directorio raíz
COPY ./requirements.txt ./app/

# Instalación de dependencias
RUN pip install -r ./app/requirements.txt

# Copia el resto del código
COPY . .



