FROM python:3.7.0

ADD clear_jobs.py /app/clear_jobs.py

# Asignamos el directorio de trabajo
WORKDIR /app/

# Instalar dependencias de python
RUN pip install --upgrade pip; \
    pip install kubernetes==7.0

# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
