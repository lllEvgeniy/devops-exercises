# Приложение ArgoCD Helm

## Требования

1. Запуск кластера Kubernetes
2. ArgoCD установлен на кластере k8s
3. Репозиторий диаграммы Хелма

## Цели

1. Создайте новое приложение в ArgoCD, которое указывает на репозиторий вашей диаграммы Helm.

## Решение

```
argocd app create some-app \
--project default \
--repo https://repo-with-helm-chart
--path "./helm" \
--sync-policy auto \
--dest-namespace default \
--dest-server https://kubernetes.cluster
```