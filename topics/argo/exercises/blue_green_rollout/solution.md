# Арго-роллеты — синий/зеленый

## Требования

1. Запуск кластера Kubernetes
2. Интерфейс командной строки Argo Rollouts
3. Развернутое приложение в конкретной версии.

## Цели

1. Установите контроллер Argo Rollouts.
2. Напишите манифест развертывания, использующий синее/зеленое развертывание, и примените его.
   1. Установите 3 реплики.
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
  replicas: 3
  strategy:
    blueGreen:     
      autoPromotionEnabled: false
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
   1. Продвижение blue/green: `kubectl argo rollouts promote some-app --watch`