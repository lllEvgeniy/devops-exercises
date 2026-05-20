# Taints и tolerations — основы

## Цели

1. Проверьте, есть ли на одном из узлов кластера **taints**.
2. Добавьте **taint** с ключом `app`, значением `web` и эффектом `NoSchedule`.
3. Запустите под с **toleration**, чтобы он мог работать на этом узле.

## Решение

1. Проверка taints на узле (пример — minikube):

   `kubectl describe node minikube | grep -i taints`

2. Добавление taint:

   `kubectl taint nodes minikube app=web:NoSchedule`

   - Поды без соответствующего **toleration** не будут планироваться на этот узел.
   - Проверка: `kubectl describe node minikube | grep -i taints`

3. Под с toleration:

```bash
kubectl run some-pod --image=redis
kubectl edit pod some-pod
```

Добавьте в `spec.tolerations`:

```yaml
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохраните изменения. Под должен перейти в состояние `Running`.
