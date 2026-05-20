## Многоэтапные сборки

### Цель

Узнайте о многоэтапных сборках

### Инструкции

1. Не создавая образ и не запуская какой-либо контейнер, используйте следующий файл Dockerfile и преобразуйте его для многоэтапного использования:

```
FROM nginx
RUN apt-get update \
 && apt-get install -y curl python build-essential \
 && apt-get install -y nodejs \
 && apt-get clean -y
RUN mkdir -p /my_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
ADD app/ /my_cool_app
WORKDIR /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
RUN apt-get update && apt-get install -y git \
 && npm install \
 && bower install \
RUN ember build — environment=prod
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]

```

2. Каковы преимущества использования многоэтапных сборок?

### Решение

1. Одно из возможных решений (акцент делается на прохождение приложения с первого этапа):

```
FROM node:6
RUN mkdir -p /my_cool_app
RUN npm install -g ember-cli
RUN npm install -g bower
WORKDIR /my_cool_app
RUN npm install
ADD app/ /my_cool_app
RUN bower install
RUN ember build — environment=prod

FROM nginx
RUN mkdir -p /my_cool_app
ADD ./config/nginx/docker.conf /etc/nginx/nginx.conf
ADD ./config/nginx/k8s.conf /etc/nginx/nginx.conf.k8s
# Копирование артефактов сборки из первого stage
COPY — from=0 /my_cool_app/dist /my_cool_app/dist
WORKDIR /my_cool_app
CMD [ “/root/nginx-app.sh”, “nginx”, “-g”, “daemon off;” ]

```

2. Многоэтапные сборки позволяют создавать образы контейнеров меньшего размера, разделив процесс сборки на несколько этапов, как мы это делали выше. Образ приложения не содержит ничего, связанного с процессом сборки, кроме самого приложения.