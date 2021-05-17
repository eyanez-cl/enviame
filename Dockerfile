FROM python:3.9

#creacion y seteado del directorio a ocupar
RUN mkdir /app
WORKDIR /app

#agregamos la carpeta al area de trabajo
ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

ENV PORT=8888

#Instalando  dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Instalando dependencias de entorno
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv
RUN pip3 install psycopg2

#Instalando dependecias de proyecto
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888
CMD gunicorn enviame_io.wsgi:application --bind 0.0.0.0:$PORT