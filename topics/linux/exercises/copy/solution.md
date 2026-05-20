# Время копирования

## Цели

1. Создайте пустой файл с именем `x` в `/tmp`.
2. Скопируйте созданный вами файл `x` в свой домашний каталог.
3. Создайте копию файла `x` с именем `y`.
4. Создайте каталог с именем «files» и переместите туда «x» и «y».
5. Скопируйте каталог «files» и назовите копию «copy_of_files».
6. Переименуйте каталог `copy_of_files` в `files2`.
7. Удалите каталоги files и files2.

## Решение

```
touch /tmp/x
cp x ~/
cp x y
mkdir files
mv x files | mv y files
cp -r files copy_of_files
mv copy_of_files files2
rm -rf files files2
```
