# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.8-alpine AS build
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app

RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       pkgconfig \
                       git \
                       gcc \
                       libcurl \
                       libc-dev \
    && rm -rf /var/cache/apk/*
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

RUN apk add --no-cache npm
WORKDIR /app/frontend
RUN npm install
# RUN npm run build


RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
WORKDIR /app 
CMD cd frontend && npm run build && cd /app && rm -rf /app/frontend && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 backend.wsgi

# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
