# Метки и селекторы 101

## Решение

1. Поды с меткой `app=web`:

   `kubectl get pods -l app=web`

2. Все объекты с меткой `env=staging`:

   `kubectl get all -l env=staging`

3. Deployment с метками `env=prod` и `type=web`:

   `kubectl get deploy -l env=prod,type=web`
