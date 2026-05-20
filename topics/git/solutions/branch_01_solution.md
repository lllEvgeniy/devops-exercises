## Ветка 01 — Решение

```
cd some_repository
echo "master branch" > file1
git add file1
git commit -a -m "added file1"
git checkout -b dev
echo "dev branch" > file2
git add file2
git commit -a -m "added file2"
```

Проверка:

```bash
git log   # в ветке dev — два коммита
git checkout master
git log   # в master — один коммит
```
