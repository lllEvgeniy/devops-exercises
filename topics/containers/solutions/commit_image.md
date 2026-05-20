# Создание изображений на лету

## Требования

Имейте хотя бы одно изображение локально (для подтверждения запустите `podman image ls`).<br>
Если у вас нет локальных изображений, просто запустите `podman pull nginx:alpine`.

## Цели

1. Запустите контейнер, используя образ веб-сервера (например, httpd, nginx,...).
  - Привязать порт контейнера 80 к локальному порту 80.
  - Запустите его в автономном режиме
  — Имя должно быть nginx_container.
2. Убедитесь, что веб-сервер работает и доступен.
3. Создайте HTML-файл со следующим содержимым и скопируйте его в контейнер в контейнер по пути, по которому он будет доступен в качестве индексного файла.

```
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
</html>
```

4. Создайте образ из работающего контейнера и назовите его «nginx_mario».
5. Пометьте контейнер тегом «Марио».
6. Удалите исходный контейнер (container_nginx) и убедитесь, что он удален.
7. Создайте новый контейнер из созданного вами образа (так же, как исходный контейнер).
8. Запустите «curl 127.0.0.1:80». Что ты видишь?
9. Запустите podman diff на новом образе. Объясните вывод

## Решение

```
# Запуск контейнера
podman run --name nginx_container -d -p 80:80 nginx:alpine

# Проверка, что веб-сервер отвечает
curl 127.0.0.1:80
    #  <!DOCTYPE html>
    #  <html>
    #  <head>
    #  <title>Welcome to nginx!</title>

# Создание index.html
cat <<EOT >>index.html
<html>
<head>
<title>It's a me</title>
</head>
<body>
<h1>Mario</h1>
</body>
EOT

# Копирование index.html в контейнер
podman cp index.html nginx_container:/usr/share/nginx/html/index.html

# Создание образа из работающего контейнера
podman commit nginx_container nginx_mario

# Тегирование образа
podman image ls
# localhost/nginx_mario     latest   dc7ed2343521   52 seconds ago   25 MB
podman tag dc7ed2343521 mario

# Удаление контейнера
podman stop nginx_container
podman rm nginx_container
podman ps -a # no container 'nginx_container'

# Новый контейнер из образа
podman run -d -p 80:80 nginx_mario

# Проверка контейнера из нового образа
curl 127.0.0.1:80
#<html>
#<head>
#<title>It's a me</title>
#</head>
#<body>
#<h1>Mario</h1>
#</body>

# Сравнение слоёв
podman diff nginx_mario

C /etc
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
A /run/nginx.pid
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /var/cache/nginx
C /var
C /var/cache
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp

# Новый index.html — поэтому изменён (C) /usr/share/nginx/html/index.html
# Образ создан при работающем nginx — поэтому появились файлы под /var (кэш, pid и т.д.)
```
