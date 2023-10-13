# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.8-alpine AS build
EXPOSE 8000
# Copiamos el directorio con los dos proyectos al contenedor
COPY . /app
# Instalamos paquetes necesarios
RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       pkgconfig \
                       git \
                       gcc \
                       libcurl \
                       libc-dev \
    && rm -rf /var/cache/apk/*
# Instalamos las dependencias del proyecto de python
WORKDIR /app
RUN pip3 install -r requirements.txt --no-cache-dir

# Instalamos npm junto con las dependencais del 
# proyecto de Vue.js 
RUN apk add --no-cache npm
WORKDIR /app/frontend
RUN npm install

# Generamos el contenido estatico del frontend y del 
# backend, borramos el directorio frontend para liberar
# espacio.
RUN npm run build
WORKDIR /app
RUN rm -rf /app/frontend
RUN python manage.py collectstatic --noinput

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

# Iniciamos el servicio de gunicorn. 
CMD gunicorn --bind 0.0.0.0:8000 backend.wsgi 

