## Контейнеризация приложения

1. Клонируйте проект с открытым исходным кодом, который хотите поместить в контейнер. Несколько предложений:

```
https://github.com/bregman-arie/node-hello-world
https://github.com/bregman-arie/flask-hello-world
```

```bash
git clone https://github.com/bregman-arie/node-hello-world
```

2. Напишите Dockerfile, который вы будете использовать для создания образа приложения (вы можете использовать любой базовый образ).

```dockerfile
FROM alpine
LABEL maintainer="your name/email"
RUN apk add --update nodejs npm
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 3000
ENTRYPOINT ["node", "./app.js"]
```

3. Создайте образ, используя только что написанный Dockerfile.

`docker image build -t web_app:latest .`

4. Убедитесь, что образ существует.

`docker image ls`

5. [Необязательно] Отправьте только что созданный образ в реестр.

```bash
docker login
docker image tag web_app:latest <your username>/web_app:latest
# Проверка: docker image ls
docker image push <your username>/web_app:latest
```

6. Запустите приложение.

```bash
docker container run -d -p 80:3000 web_app:latest
```

7. Убедитесь, что приложение работает.

```bash
docker container ls
docker logs <container ID/name>
# В браузере: http://127.0.0.1:80
```
