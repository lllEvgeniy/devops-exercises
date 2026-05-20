# Упражнения на основе сценариев Docker

Здесь сценарные вопросы по Docker для практики типичных задач DevOps: отладка, сеть нескольких контейнеров и ускорение сборки в CI/CD. У каждого вопроса — пошаговый разбор.

## Вопрос 1. Отладка сбоя контейнера Docker

### Вопрос

Вы — инженер DevOps и разворачиваете приложение на Node.js в Docker. Запускаете `docker run -d -p 3000:3000 my-node-app`, но контейнер сразу завершается. В `docker ps -a` статус — **Exited**. Как диагностировать и исправить?

### Ответ

1. **Логи.** `docker logs <имя_или_ID_контейнера>` — сообщения об ошибках. Часто: не установлены зависимости (падение на этапе `npm install`), неверная команда запуска, отсутствует файл точки входа.
2. **Конфигурация запуска.** `docker inspect <контейнер>` — в JSON смотрите `Config.Cmd` и `Config.Entrypoint`: команда вроде `node app.js` должна существовать в образе и быть корректной.
3. **Dockerfile.** Проверьте `CMD` / `ENTRYPOINT`, например `CMD ["node", "app.js"]`. Исправьте образ и пересоберите: `docker build -t my-node-app .`
4. **Интерактивно.** `docker run -it my-node-app sh` (или `bash`), затем вручную `node app.js` — воспроизведение ошибки в шелле.
5. **Ресурсы хоста.** `docker stats` и метрики ОС — не упираетесь ли в память/OOM.

**Пример:** в логах `node: command not found` — в образе нет Node или не тот `PATH`; задайте базовый образ, например `FROM node:18`, пересоберите и запустите снова.

### Дополнительно

- Сначала почти всегда смотрят `docker logs`.
- `docker ps -a` — статус и идентификатор контейнера (для `logs` / `inspect` нужен именно контейнер, а не только имя образа, если вы его не задавали через `--name`).

---

## Вопрос 2. Связка нескольких контейнеров (Node.js и MySQL)

### Вопрос

Нужно поднять веб-приложение на Node.js и MySQL в Docker. Приложение ожидает БД на `localhost:3306`, но при отдельных `docker run` контейнеры не видят друг друга. Как заставить их работать вместе?

### Ответ

1. **Docker Compose** — опишите оба сервиса и общую сеть в `docker-compose.yml`:

```yaml
version: '3.8'
services:
  node-app:
    image: my-node-app
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - mysql-db
    environment:
      - DB_HOST=mysql-db
      - DB_PORT=3306
  mysql-db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=secret
    ports:
      - "3306:3306"
```

2. **Запуск:** `docker compose up -d` (или `docker-compose up -d`). Из контейнера Node.js хост БД — **имя сервиса** `mysql-db`, а не `localhost` (если только вы не используете `host.docker.internal` / сеть хоста осознанно).
3. **Проверка:** `docker compose logs node-app` — успешное подключение к MySQL; при ошибках смотрите переменные окружения и готовность MySQL (иногда нужен healthcheck и ожидание).
4. **Без Compose** — пользовательская сеть:

   - `docker network create my-app-network`
   - MySQL: `docker run -d --name mysql-db --network my-app-network -e MYSQL_ROOT_PASSWORD=secret mysql:8.0`
   - Node.js: `docker run -d --name node-app --network my-app-network -p 3000:3000 -e DB_HOST=mysql-db my-node-app`

### Дополнительно

- Compose сам создаёт сеть и порядок зависимостей удобнее, чем длинные однострочники.
- Учётные данные БД передавайте через переменные окружения или секреты, не зашивайте в образ.

---

## Вопрос 3. Оптимизация Dockerfile для CI/CD

### Вопрос

В Jenkins собирается Docker-образ Python-приложения; сборка долгая и тормозит pipeline. Как ускорить сборку, не ломая результат?

### Ответ

1. **Меньший базовый образ.** Например `python:3.9-slim` вместо полного `python:3.9` — меньше тянуть по сети и быстрее распаковка.

```dockerfile
FROM python:3.9-slim
```

2. **Порядок слоёв под кэш.** Сначала редко меняющееся, потом код. Типичный приём:

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

```
3. **Меньше слоёв там, где уместно.** Объединение команд через `&&` и очистка кэша pip в том же `RUN`:

```dockerfile
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip
```

4. **Многостадийная сборка** — если нужны компиляторы только на этапе сборки, в финальный образ переносите уже установленные пакеты/артефакты.

```dockerfile
FROM python:3.9 AS builder
COPY requirements.txt .
RUN pip install -r requirements.txt
FROM python:3.9-slim
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .
CMD ["python", "app.py"]
```

5. **Jenkins.** Пересобирать образ только при изменении релевантных файлов; иначе использовать кэш registry или daemon (настройки зависят от вашего pipeline).

```groovy
pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            when { changeset "Dockerfile,**.py" }
            steps { sh 'docker build -t my-python-app .' }
        }
    }
}
```

### Дополнительно

- Добавьте `.dockerignore` (`.git`, `tests/`, артефакты), чтобы не слать лишнее в контекст сборки.
- Замеряйте время стадии сборки в Jenkins до/после изменений.

---

*Материал: Lahiru Galhena*
