# Развертывание Арго — Канарейки

## Требования

1. Запуск кластера Kubernetes
2. Интерфейс командной строки Argo Rollouts
3. Развернутое приложение в конкретной версии.

## Цели

1. Установите контроллер Argo Rollouts.
2. Напишите манифест развертывания, использующий канареечную стратегию развертывания, и примените его.
   1. Установите 6 реплик.
   2. Отключите автопродвижение
3. Проверьте список развертывания
4. Разверните новую версию своего приложения любым удобным для вас способом.
   1. Проверьте статус внедрения

## Решение

Установка:

1. `kubectl create namespace argo-rollouts`
   1. `kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml`

2. Ресурс развертывания:

```
---
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: some-app
spec:
  replicas: 6
  strategy:
    canary:
      stableService: k8s-service-stable
      canaryService: k8s-service-canary
      trafficRouting:
        ambassador:
          mappings:
            - k8s-mapping
      steps:
      - setWeight: 30
      - pause: {}
      - setWeight: 60
      - pause: {}
      - setWeight: 100
      - pause: {}   
  selector:
    matchLabels:
      app: some-web-app
  template:
    metadata:
      labels:
        app: some-web-app
    spec:
      containers:
      - name: web-app
        image: some/registry/and/image:v1.0
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
```

3. Список rollout: `kubectl argo rollouts list rollouts` (или `kubectl argo rollouts get rollout some-app`)
4. Новый образ: `kubectl argo rollouts set image some-app web-app=some/registry/and/image:v2.0`
   1. Продвижение canary: `kubectl argo rollouts promote some-app --watch`