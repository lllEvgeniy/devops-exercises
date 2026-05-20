## ReplicaSet 02 — решение

1. Создайте ReplicaSet с двумя репликами:

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

2. Проверьте ReplicaSet и две реплики:

```bash
kubectl get rs
```

3. Удалите ReplicaSet, **не** удаляя поды:

```bash
kubectl delete -f rs.yaml --cascade=orphan
```

4. ReplicaSet удалён, поды продолжают работать:

```bash
kubectl get rs   # пусто
kubectl get po   # поды на месте
```

5. Снова примените тот же манифест:

```bash
kubectl apply -f rs.yaml
```

6. ReplicaSet должен подхватить существующие поды, а не создавать новые:

```bash
kubectl describe rs web
kubectl get po -l type=web
```

Имена подов не должны измениться; в событиях ReplicaSet не должно быть массового создания новых подов.
