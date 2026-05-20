# Создать и уничтожить

## Цели

1. Создайте файл с именем `x`
2. Создайте каталог с именем `content`.
3. Переместите файл `x` в каталог `content`.
4. Создайте файл в каталоге `content` с именем `y`.
5. Создайте следующую структуру каталогов в каталоге «content»: «dir1/dir2/dir3».
6. Удалите каталог содержимого.

## Решение

```
touch x
mkdir content
mv x content
touch content/y
mkdir -p content/dir1/dir2/dir3
rm -rf content
```
