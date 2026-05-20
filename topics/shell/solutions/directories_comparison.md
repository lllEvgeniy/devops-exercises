## Сравнение каталогов

### Цели

1. На вход передаются **два каталога**; на выходе должна отображаться **любая разница** между ними.

### Решение 1 (контрольная сумма списка имён)

Скрипт `dirdiff.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Использование: $0 <каталог1> <каталог2>" >&2
  exit 1
fi

d1="$1"
d2="$2"

sum1=$(find "$d1" -mindepth 1 -maxdepth 1 -printf '%f\n' 2>/dev/null | sort | md5sum | awk '{print $1}')
sum2=$(find "$d2" -mindepth 1 -maxdepth 1 -printf '%f\n' 2>/dev/null | sort | md5sum | awk '{print $1}')

if [ "$sum1" = "$sum2" ]; then
  echo "Состав верхнего уровня (имена) совпадает по хэшу."
  exit 0
fi

diff -qr "$d1" "$d2"
```

> Примечание: сравнение только **имён** на верхнем уровне не гарантирует идентичность содержимого файлов; для полного сравнения используйте `diff -r`.

### Решение 2 (`diff --recursive`)

```bash
diff --recursive directory1 directory2
```

Краткий режим только «что отличается»:

```bash
diff -qr directory1 directory2
```
