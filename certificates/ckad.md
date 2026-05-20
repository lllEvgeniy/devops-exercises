## Certified Kubernetes Application Developer (CKAD)

### Основные концепции

### Поды (Pods)

<details>
<summary>Разверните под с именем web-1985, используя образ nginx:alpine</summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`

</b></details>

<details>
<summary>Как узнать, на каком узле (node) выполняется под?</summary><br><b>

`kubectl get po -o wide`

</b></details>

### Пространства имён (Namespaces)

<details>
<summary>Перечислите все пространства имён</summary><br><b>

`kubectl get ns`

</b></details>

<details>
<summary>Перечислите все поды в пространстве имён neverland</summary><br><b>

`kubectl get po -n neverland`

</b></details>

<details>
<summary>Перечислите все поды во всех пространствах имён</summary><br><b>

`kubectl get po --all-namespaces`

</b></details>
