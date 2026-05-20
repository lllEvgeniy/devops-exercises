## Certified Kubernetes Administrator (CKA)

### Поды (Pods)

<details>
<summary>Разверните под с именем web-1985, используя образ nginx:alpine</summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`

</b></details>

<details>
<summary>Как узнать, на каком узле (node) выполняется под?</summary><br><b>

`kubectl get po -o wide`

</b></details>
