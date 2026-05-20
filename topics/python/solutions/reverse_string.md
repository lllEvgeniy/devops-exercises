## Перевернуть строку — Решение

Срез в Python:

```python
my_string[::-1]
```

Более наглядный способ (осторожно: для очень длинных строк может быть медленно):

```python
def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp
```
