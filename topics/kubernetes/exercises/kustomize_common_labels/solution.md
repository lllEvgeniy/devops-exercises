# Настройка — общие метки

## Требования

1. Запуск кластера Kubernetes
2. Kubctl версии 1.14 или выше.

## Цели

В текущем каталоге находится приложение, состоящее из развертывания и службы.

1. Напишите файл kustomization.yml, который добавит к Сервису и Развертыванию метку «имя команды: ace».
2. Выполните команду настройки, которая создаст настроенные файлы k8s с добавленной меткой.

## Решение

1. Добавьте следующее в kustomization.yml в каталоге someApp:

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

commonLabels:
  team-name: aces

resources:
  - service.yml
  - deployment.yml

```

2. Запустите `kubectl apply -k someApp`