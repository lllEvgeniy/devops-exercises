## ReplicaSet 03 — решение

1. Создайте ReplicaSet с двумя репликами; метка селектора и в шаблоне пода — `type=web`:

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

2. Проверьте две реплики:

```bash
kubectl get rs
```

3. Сохраните список подов:

```bash
kubectl get po > running_pods.txt
```

4. Удалите метку `type=web` у одного из подов:

```bash
kubectl label pod <POD_NAME> type-
```

5. Снова перечислите поды. Будет ли ещё один под?

Да. После снятия метки под перестаёт соответствовать селектору ReplicaSet и больше им не управляется. ReplicaSet видит недостачу реплик и создаёт новый под.

6. Убедитесь, что ReplicaSet создал новый под:

```bash
kubectl describe rs web
kubectl get po
```
