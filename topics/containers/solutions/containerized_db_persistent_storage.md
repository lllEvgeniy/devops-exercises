# Контейнерная БД с постоянным хранилищем

1. Запустите контейнер с базой данных любого типа (MySql, PostgreSQL, Mongo и т. д.).
  1. Используйте для базы данных точку монтирования на хосте вместо использования для этого хранилища контейнеров.
  2. Объясните, почему использование хост-хранилища вместо контейнера может быть лучшим выбором.
2. Убедитесь, что контейнер запущен.


## Решение

```
# Каталог для данных БД на хосте
mkdir -pv ~/local/mysql
sudo semanage fcontext -a -t container_file_t '/home/USERNAME/local/mysql(/.*)?'
sudo restorecon -R /home/USERNAME/local/mysql

# Запуск контейнера с volume на хосте
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql -v /home/USERNAME/local/mysql:/var/lib/mysql/db

# Проверка, что контейнер работает
podman ps
```

Лучше использовать хранилище на хосте: при удалении контейнера или сбросе container storage данные БД останутся на диске хоста.