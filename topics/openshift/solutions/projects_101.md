## OpenShift — Проекты 101

### Цели

Во вновь развернутом кластере (предпочтительно) выполните следующее:

1. Войдите в кластер OpenShift.
2. Перечислите все проекты
3. Создайте новый проект под названием «Неверленд».
4. Проверьте обзорный статус текущего проекта.

### Решение

```
oc login -u YOUR_USER -p YOUR_PASSWORD_OR_TOKEN
oc get projects # Empty output in new cluster
oc new-project neverland
oc status
```
