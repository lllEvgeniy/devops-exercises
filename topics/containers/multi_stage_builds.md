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