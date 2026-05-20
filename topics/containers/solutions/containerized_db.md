# Контейнерная БД

1. Запустите контейнер с базой данных любого типа (MySql, PostgreSQL, Mongo и т. д.).
2. Убедитесь, что контейнер запущен.
3. Получите доступ к контейнеру и создайте новую таблицу (или коллекцию, в зависимости от того, какой тип БД вы выбрали) для учащихся.
4. Вставьте строку (или документ) студента.
5. Убедитесь, что строка/документ добавлена.


## Решение

```
# Запуск контейнера
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql

# Проверка, что контейнер работает
podman ps

# Добавление записи студента
podman exec -it mysql /bin/bash
mysql -u root
use university;
CREATE TABLE Students (id int NOT NULL, name varchar(255) DEFAULT NULL, PRIMARY KEY (id));
insert into Students (id, name) values (1,'Luigi');
select * from Students;
```
