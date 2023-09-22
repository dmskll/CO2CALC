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
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


EXPOSE 8080
RUN apk add --no-cache npm
WORKDIR /app/frontend
#COPY package*.json .
RUN npm install
#COPY . .
RUN npm run build
#CMD ["npm", "run", "serve"]

#ENTRYPOINT ["python3"] 
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]


RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
WORKDIR /app 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
