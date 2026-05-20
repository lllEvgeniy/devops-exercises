## ReplicaSet 01 — решение

1. Создайте ReplicaSet с двумя репликами (приложение на ваш выбор):

```bash
cat >> rs.yaml <<'EOL'
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: web
  labels:
    app: somewebapp
    type: web
spec:
  replicas: 2
  selector:
    matchLabels:
      type: web
  template:
    metadata:
      labels:
        type: web
    spec:
      containers:
      - name: httpd
        image: registry.redhat.io/rhscl/httpd-24-rhel7
EOL

kubectl apply -f rs.yaml
```

2. Убедитесь, что ReplicaSet создан и есть 2 пода:

```bash
kubectl get rs
# или: kubectl get -f rs.yaml
```

3. Удалите один из подов:

```bash
kubectl delete pod <POD_NAME>
```

4. Убедитесь, что ReplicaSet создал новый под вместо удалённого:

```bash
kubectl get rs
kubectl get po
```
