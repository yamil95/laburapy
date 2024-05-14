FROM python:3.12.3-alpine3.19

WORKDIR /app

# Instalación de dependencias y configuración del entorno
RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev && \
    pip install --upgrade pip 

# Copia solo el archivo de requisitos y utiliza Poetry para instalar dependencias
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copia el resto del código
COPY . .



