# Контейнерный веб-сервер

1. Запустите контейнерный веб-сервер в фоновом режиме и привяжите его порт (8080) к локальному порту.
2. Убедитесь, что порт (8080) привязан.
3. Подключитесь к веб-серверу с вашего локального хоста.
4. Теперь запустите то же веб-приложение, но привяжите его к локальному порту 8080.

## Решение

```
$ podman run -d -p 8080 httpd # run the container and bind the port 8080 to a local port
$ podman port -l 8080 # show to which local port the port 8080 on the container, binds to
0.0.0.0:41203
$ curl http://0.0.0.0:41203 # use the port from the output of the previous command

!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<title>Test Page for the HTTP Server on Red Hat Enterprise Linux</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

$ podman run -d -p 8080:8080 httpd
```
