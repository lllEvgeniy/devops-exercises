# CKA (сертифицированный администратор Kubernetes)

- [CKA (сертифицированный администратор Kubernetes)](#cka-certified-kubernetes-administrator)
  - [Настройка](#настройка)
  - [Поды (Pods)](#pods)
    - [Устранение неполадок подов](#troubleshooting-pods)
  - [Пространства имен](#пространства имен)
  - [Узлы](#узлы)
  - [Сервисы (Services)](#services)
  - [Наборы реплик](#репликасеты)
    - [Устранение неполадок с наборами реплик](#troubleshooting-replicasets)
  - [Развертывания](#развертываний)
    - [Устранение неполадок при развертывании](#troubleshooting-deployments)
  - [Планировщик](#планировщик)
    - [Affinity узлов](#node-affinity)
  - [Метки и селекторы](#labels-and-selectors)
    - [Селектор узла](#node-selector)
  - [Taints и tolerations](#taints)
  - [Лимиты ресурсов](#resource-limits)
  - [Мониторинг](#мониторинг)
  - [Планировщик (дополнительно)](#scheduler-1)

## Настройка

* Настройте кластер Kubernetes. Используйте один из следующих
   1. Minikube для локального бесплатного и простого кластера
   2. Управляемый кластер (ЭКС, ГКЕ, АКС)

* Установите псевдонимы:

```bash
alias k=kubectl
alias kd=kubectl delete
alias kds=kubectl describe
alias ke=kubectl edit
alias kr=kubectl run
alias kg=kubectl get
```

## Поды (Pods) {#pods}

<details>
<summary>Запустите команду, чтобы просмотреть все поды в текущем пространстве имен.</summary><br><b>

`kubectl get pods`

Примечание: создайте псевдоним («alias k=kubectl») и привыкните к «k get po».

</b></details>

<details>
<summary>Запустите под под названием «nginx-test», используя образ «nginx».</summary><br><b>

`kubectl run nginx-test --image=nginx`

</b></details>

<details>
<summary>Предположим, у вас есть под с именем «nginx-test», как его удалить?</summary><br><b>

`kubectl delete pod nginx-test`

</b></details>

<details>
<summary>В каком пространстве имен работает под <code>etcd</code>? перечислить поды в этом пространстве имен</summary><br><b>

`k get po -n kube-system`

Допустим, вы не знали, в каком именно пространстве имен он находится. Затем можно выполнить `kubectl get pods -A | grep etcd`, чтобы найти под и увидеть его namespace.

</b></details>

<details>
<summary>Получение списка подов из всех пространств имен</summary><br><b>

`kubectl get pods -A`

Длинная версия будет выглядеть так: «kubectl get pods --all-namespaces».

</b></details>

<details>
<summary>Напишите YAML-манифест пода с двумя контейнерами и используйте файл YAML для создания пода (используйте любые изображения, которые вы предпочитаете).</summary><br><b>

```
cat > pod.yaml <<EOL
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
  - image: alpine
    name: alpine
  - image: nginx-unprivileged
    name: nginx-unprivileged
EOL

kubectl create -f pod.yaml
```

Если вы спросите себя, как запомнить весь манифест — можно сгенерировать заготовку: `kubectl run some-pod --image=redis -o yaml --dry-run=client > pod.yaml`. На экзамене важнее понимать структуру, а не заучивать команды наизусть.

</b></details>

<details>
<summary>Создайте YAML-манифест пода без его фактического запуска с помощью команды kubectl (используйте любое изображение, которое вы предпочитаете)</summary><br><b>

`k run some-pod -o yaml --image nginx-unprivileged --dry-run=client > pod.yaml`

</b></details>

<details>
<summary>Как проверить правильность манифеста?</summary><br><b>

с флагом `--dry-run`, который на самом деле не создаст его, но проверит, и таким образом вы сможете обнаружить любые проблемы с синтаксисом.

`kubectl create -f YAML_FILE --dry-run=client`

</b></details>

<details>
<summary>Как проверить, какое изображение использует определённый под?</summary><br><b>

`kubectl describe pod <POD_NAME> | grep -i image`

</b></details>

<details>
<summary>Как проверить, сколько контейнеров работает в одном поде?</summary><br><b>

`k get po POD_NAME` и увидите номер в столбце READY.

Вы также можете запустить `kubectl describe pod POD_NAME`

</b></details>

<details>
<summary>Запустите под под названием «remo» с последним изображением Redis и меткой «год = 2017».</summary><br><b>

`kubectl run remo --image=redis:latest -l year=2017`

</b></details>

<details>
<summary>Получение списка подов и их меток</summary><br><b>

`k get po --show-labels`

</b></details>

<details>
<summary>Удалить под с именем «nm»</summary><br><b>

`kubectl delete pod nm`

</b></details>

<details>
<summary>Перечислите все поды с меткой «env=prod».</summary><br><b>

`k get po -l env=prod`

Чтобы их подсчитать: `k get po -l env=prod --no-headers | wc -l`

</b></details>

<details>
<summary>Создайте статический под с изображением <code>python</code>, который запускает команду <code>sleep 2017</code></summary><br><b>

Сначала перейдите в каталог, отслеживаемый kubelet для создания статического пода: `cd /etc/kubernetes/manifests` (вы можете проверить путь, прочитав файл конфигурации kubelet)

Теперь создайте определение/манифест в этом каталоге.

`kubectl run some-pod --image=python --command sleep 2017 --restart=Never --dry-run=client -o yaml > static-pod.yaml`

</b></details>

<details>
<summary>Опишите, как бы вы удалили статический под</summary><br><b>

Найдите каталог статических подов (посмотрите staticPodPath в файле конфигурации kubelet).

Перейдите в этот каталог и удалите манифест/определение статического пода (`rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`)

</b></details>

### Устранение неполадок подов {#troubleshooting-pods}

<details>
<summary>Вы пытаетесь запустить под, но видите статус CrashLoopBackOff. Что это значит? Как определить проблему?</summary><br><b>

Контейнер не удалось запустить (по разным причинам), и Kubernetes пытается снова запустить под через некоторую задержку (= время ожидания).

Некоторые причины неудачи:
  - Неправильная конфигурация: опечатка, неподдерживаемое значение и т. д.
  - Ресурс недоступен - узлы не работают, PersistentVolume не установлена и т. д.

Некоторые способы отладки:

1. `kubectl describe pod POD_NAME`
   1. Сосредоточьтесь на **State** (часто `Waiting` / `CrashLoopBackOff`) и **Last State** — там причина последнего сбоя.
2. `kubectl logs POD_NAME`
   1. Это должно обеспечить точный вывод 
   2. Для конкретного контейнера вы можете добавить `-c CONTAINER_NAME`
3. Если причина всё ещё неясна: `kubectl get events --sort-by='.lastTimestamp'`

</b></details>

<details>
<summary>Что означает ошибка <code>ImagePullBackOff</code>?</summary><br><b>

Скорее всего вы не правильно написали название образа, который пытаетесь вытащить и запустить. Или, возможно, его нет в реестре.

Вы можете подтвердить это с помощью `kubectl describe pod POD_NAME`.

</b></details>

<details>
<summary>Как проверить, на каком узле работает определенный Pod?</summary><br><b>

`kubectl get pod POD_NAME -o wide`

</b></details>

<details>
<summary>Выполните следующую команду: <code>kubectl run ohno --image=sheris</code>. Это сработало? почему нет? исправьте это, не удаляя под и используя любое изображение, которое захотите.</summary><br><b>

Потому что нет такого образа `sheris` (опечатка в `--image=sheris`). По крайней мере на данный момент :)

Чтобы это исправить, выполните `kubectl edit pod ohno` и измените `- image: sheris` на `- image: redis` (или другой существующий образ).

</b></details>

<details>
<summary>Вы пытаетесь запустить под, но он находится в состоянии Pending. В чем может быть причина?</summary><br><b>

Одна из возможных причин заключается в том, что планировщик, который должен планировать поды на узлах, не работает. Чтобы проверить это, вы можете запустить `kubectl get po -A | grep scheduler` или проверьте непосредственно в пространстве имен `kube-system`.

</b></details>

<details>
<summary>Как просмотреть журналы контейнера, работающего в поде?</summary><br><b>

`kubectl logs POD_NAME`

</b></details>

<details>
<summary>В поде есть два контейнера, которые называются «some-pod». Что произойдет, если вы запустите <code>kubectl logs some-pod</code></summary><br><b>

Это не сработает, потому что внутри пода есть два контейнера, и вам нужно указать один из них с помощью `kubectl logs POD_NAME -c CONTAINER_NAME`

</b></details>

## Пространства имен

<details>
<summary>Перечислить все пространства имен</summary><br><b>

`kubectl get ns`

</b></details>

<details>
<summary>Создайте пространство имен под названием «alle».</summary><br><b>

`kubectl create namespace alle`

</b></details>

<details>
<summary>Проверьте, сколько существует пространств имен</summary><br><b>

`kubectl get ns --no-headers | wc -l`

</b></details>

<details>
<summary>Проверьте, сколько подов существует в пространстве имен «dev».</summary><br><b>

`k get po -n dev`

</b></details>

<details>
<summary>Создайте под с именем «kratos» в пространстве имен dev. Под должен использовать образ «redis».</summary><br><b>

Если пространство имен еще не существует: `k create ns dev`

`kubectl run kratos --image=redis -n dev`

</b></details>

<details>
<summary>Вы ищете под с именем «Atreus». Как проверить, в каком пространстве имен он работает?</summary><br><b>

`kubectl get pods -A | grep Atreus`

</b></details>

## Узлы

<details>
<summary>Запустите команду для просмотра всех узлов кластера</summary><br><b>

`kubectl get nodes`

Примечание: создайте псевдоним («alias k=kubectl») и привыкните к «k get no».

</b></details>

<details>
<summary>Создайте список всех узлов в формате JSON и сохраните его в файле с именем «some_nodes.json».</summary><br><b>

`k get nodes -o json > some_nodes.json`

</b></details>

<details>
<summary>Проверьте, какие метки имеет один из ваших узлов в кластере.</summary><br><b>

`kubectl get nodes --show-labels`

</b></details>

## Сервисы (Services) {#services}

<details>
<summary>Проверьте, сколько служб запущено в текущем пространстве имен.</summary><br><b>

`kubectl get svc`

</b></details>

<details>
<summary>Создайте внутреннюю службу под названием «sevi», чтобы открыть доступ к веб-приложению через порт 1991.</summary><br><b>

`kubectl expose pod web --port=1991 --name=sevi`

</b></details>

<details>
<summary>Как ссылаться по имени на службу под названием «app-service» в том же пространстве имен?</summary><br><b>

сервис приложений

</b></details>

<details>
<summary>Как проверить TargetPort службы?</summary><br><b>

`kubectl describe svc <SERVICE_NAME>`

</b></details>

<details>
<summary>Как проверить, какие конечные точки имеет svc?</summary><br><b>

`kubectl describe svc <SERVICE_NAME>`

</b></details>

<details>
<summary>Как ссылаться по имени на службу под названием «app-service» в другом пространстве имен, называемом «dev»?</summary><br><b>

приложение-service.dev.svc.cluster.local

</b></details>

<details>
<summary>Предположим, у вас запущено развертывание, и вам нужно создать службу для предоставления доступа к подам. Это то, что требуется/известно:

* Имя развертывания: jabulik
* Целевой порт: 8080.
* Тип службы: NodePort.
* Селектор: приложение Jabulik.
* Порт: 8080</summary><br><b>

`kubectl expose deployment jabulik --name=jabulik-service --target-port=8080 --type=NodePort --port=8080 --dry-run=client -o yaml > svc.yaml`

`vi svc.yaml` (убедитесь, что селектор установлен на `jabulik-app`)

`kubectl apply -f svc.yaml`

</b></details>

## Наборы реплик

<details>
<summary>Как проверить, сколько наборов реплик определено в текущем пространстве имен?</summary><br><b>

`kubectl get rs`

</b></details>

<details>
<summary>У вас есть набор реплик, определенный для запуска 3 подов. Вы удалили один из этих трёх подов. Что будет дальше? сколько будет подов?</summary><br><b>

Теоретически по-прежнему будут работать 3 пода, потому что цель набора реплик — обеспечить это. поэтому, если вы удалите один или несколько подов, контроллер создаст новые — снова будет 3 пода.

</b></details>

<details>
<summary>Как проверить, какой образ контейнера использовался как часть набора реплик под названием «repli»?</summary><br><b>

`kubectl describe rs repli | grep -i image`

</b></details>

<details>
<summary>Как проверить, сколько подов Pods готово в составе набора реплик под названием «repli»?</summary><br><b>

`kubectl describe rs repli | grep -i "Pods Status"`

</b></details>

<details>
<summary>Как удалить набор реплик под названием «рори»?</summary><br><b>

`kubectl delete rs rori`

</b></details>

<details>
<summary>Как изменить набор реплик под названием «рори», чтобы использовать другое изображение?</summary><br><b>

`kubectl edit rs rori`

</b></details>

<details>
<summary>Увеличьте масштаб набора реплик под названием «rori», чтобы запускать 5 подов вместо 2.</summary><br><b>

`kubectl scale rs rori --replicas=5`

</b></details>

<details>
<summary>Уменьшите масштаб набора реплик под названием «rori», чтобы запустить 1 под вместо 5.</summary><br><b>

`kubectl scale rs rori --replicas=1`

</b></details>

### Устранение неполадок с наборами реплик {#troubleshooting-replicasets}

<details>
<summary>Исправьте следующее определение ReplicaSet.

```yaml
apiVersion: apps/v1
kind: ReplicaCet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: taink
    spec:
      containers:
      - name: redis
        image: redis
```

</summary><br><b>

Поле `kind` должно быть `ReplicaSet`, а не `ReplicaCet`.

</b></details>

<details>
<summary>Исправьте следующее определение ReplicaSet.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  selector:
    matchLabels:
      tier: cache
  template:
    metadata:
      labels:
        tier: taink
    spec:
      containers:
      - name: redis
        image: redis
```

</summary><br><b>

Селектор `matchLabels` не совпадает с метками в `template.metadata.labels` (`cache` vs `taink`). Исправьте метку в шаблоне на `tier: cache`.

</b></details>

## Развертывания

<details>
<summary>Как составить список всех развертываний в текущем пространстве имен?</summary><br><b>

`kubectl get deployments`

</b></details>

<details>
<summary>Как проверить, какой образ использует определенное развертывание?</summary><br><b>

`kubectl describe deployment <DEPLOYMENT_NAME> | grep -i image`

</b></details>

<details>
<summary>Создайте определение файла/манифест развертывания под названием «dep» с тремя репликами, использующими образ «redis».</summary><br><b>

`kubectl create deployment dep --image=redis --replicas=3 --dry-run=client -o yaml > deployment.yaml`

</b></details>

<details>
<summary>Удалите развертывание `depdep`</summary><br><b>

`kubectl delete deployment depdep`

</b></details>

<details>
<summary>Создайте развертывание под названием «pluck», используя образ «redis», и убедитесь, что оно запускает 5 реплик.</summary><br><b>

`kubectl create deployment pluck --image=redis --replicas=5`

</b></details>

<details>
<summary>Создайте развертывание со следующими свойствами:

* называется «blufer»
* использует образ «python»
* запускает 3 реплики
* все поды будут размещены на узле с меткой «blufer».</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > Deployment.yaml`

Добавьте следующий раздел (`vi Deployment.yaml`):

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: blufer
            operator: Exists
```

`kubectl apply -f Deployment.yaml`

</b></details>

### Устранение неполадок при развертывании {#troubleshooting-deployments}

<details>
<summary>Исправьте следующий манифест развертывания.

```yaml
apiVersion: apps/v1
kind: Deploy
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: dep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```

</summary><br><b>

Измените `kind: Deploy` на `kind: Deployment`.

</b></details>

<details>
<summary>Исправьте следующий манифест развертывания.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: dep
  name: dep
spec:
  replicas: 3
  selector:
    matchLabels:
      app: depdep
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: dep
    spec:
      containers:
      - image: redis
        name: redis
        resources: {}
status: {}
```

</summary><br><b>

Селектор `matchLabels.app: depdep` не совпадает с меткой пода `app: dep`. Исправьте селектор на `app: dep`.

</b></details>

## Планировщик

<details>
<summary>Как запланировать под на узле с именем «node1»?</summary><br><b>

`kubectl run some-pod --image=redis -o yaml --dry-run=client > pod.yaml`

`vi pod.yaml` и добавьте:

```yaml
spec:
  nodeName: node1
```

`kubectl apply -f pod.yaml`

Примечание: если в кластере нет узла `node1`, под останется в состоянии `Pending`.

</b></details>

### Affinity узлов (node affinity) {#node-affinity}

<details>
<summary>Используя node affinity, настройте Pod для планирования на узлах, где ключ <code>region</code> равен <code>asia</code> или <code>emea</code>.</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: In
          values:
          - asia
          - emea
```

</b></details>

<details>
<summary>Используя node affinity, настройте под так, чтобы он не планировался на узлах с <code>region=neverland</code>.</summary><br><b>

`vi pod.yaml`

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: region
          operator: NotIn
          values:
          - neverland
```

</b></details>

## Метки и селекторы {#labels-and-selectors}

<details>
<summary>Как перечислить все поды с меткой «app=web»?</summary><br><b>

`k get po -l app=web`

</b></details>

<details>
<summary>Как составить список всех объектов, помеченных как «env=staging»?</summary><br><b>

`kubectl get all -l env=staging`

</b></details>

<details>
<summary>Как составить список всех развертываний из «env=prod» и «type=web»?</summary><br><b>

`kubectl get deploy -l env=prod,type=web`

</b></details>

### Селектор узла (node selector) {#node-selector}

<details>
<summary>Примените метку «hw=max» к одному из узлов вашего кластера.</summary><br><b>

`kubectl label nodes <NODE_NAME> hw=max`

</b></details>

<details>
<summary>Создайте и запустите под под названием some-pod с образом redis и настройте его на использование селектора hw=max.</summary><br><b>

```
kubectl run some-pod --image=redis --dry-run=client -o yaml > pod.yaml

vi pod.yaml

spec:
  nodeSelector:
    hw: max

kubectl apply -f pod.yaml
```

</b></details>

<details>
<summary>Объясните, почему селекторы узлов могут быть ограничены.</summary><br><b>

Предположим, вы хотите запустить свой под на всех узлах с параметром hw, установленным на max или min, а не только на max. Это невозможно с помощью nodeSelectors, которые довольно упрощены, и здесь вы можете рассмотреть возможность «node affinity».

</b></details>

## Taints и tolerations {#taints}

<details>
<summary>Проверьте, есть ли на узле <code>master</code> taints.</summary><br><b>

`kubectl describe node master | grep -i taints`

</b></details>

<details>
<summary>Добавьте на один из узлов кластера taint с ключом <code>app</code>, значением <code>web</code> и эффектом <code>NoSchedule</code>. Убедитесь, что он применился.</summary><br><b>

`kubectl taint nodes minikube app=web:NoSchedule`

`kubectl describe node minikube | grep -i taints`

</b></details>

<details>
<summary>Вы добавили <code>kubectl taint nodes minikube app=web:NoSchedule</code> на единственном узле кластера, затем выполнили <code>kubectl run some-pod --image=redis</code>. Что произойдёт?</summary><br><b>

Под останется в состоянии <code>Pending</code>, потому что на единственном узле есть taint <code>app=web:NoSchedule</code>, а у пода нет соответствующего toleration.

</b></details>

<details>
<summary>Вы добавили <code>kubectl taint nodes minikube app=web:NoSchedule</code> на единственном узле кластера, затем выполнили <code>kubectl run some-pod --image=redis</code>, но под остаётся в <code>Pending</code>. Как это исправить?</summary><br><b>

`kubectl edit pod some-pod` и добавьте в `spec.tolerations`:

```yaml
  - effect: NoSchedule
    key: app
    operator: Equal
    value: web
```

Сохраните изменения. Под должен перейти в состояние `Running`.

</b></details>

<details>
<summary>Удалите существующий taint с одного из узлов вашего кластера.</summary><br><b>

`kubectl taint nodes minikube app=web:NoSchedule-`

</b></details>

## Лимиты и requests ресурсов {#resource-limits}

<details>
<summary>Проверьте, есть ли какие-либо ограничения на один из подов вашего кластера.</summary><br><b>

`kubectl describe pod <POD_NAME> | grep -i limits`

</b></details>

<details>
<summary>Запустите под под названием «yay» с изображением «python» и запросом ресурсов в размере 64 МБ памяти и 250 МБ процессора.</summary><br><b>

`kubectl run yay --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```yaml
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay
    resources:
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`

</b></details>

<details>
<summary>Запустите под под названием «yay2» с изображением «python». Убедитесь, что у него есть запрос на ресурсы: 64 МБ памяти и 250 МБ ЦП, а ограничения составляют 128 МБ памяти и 500 МБ ЦП.</summary><br><b>

`kubectl run yay2 --image=python --dry-run=client -o yaml > pod.yaml`

`vi pod.yaml`

```yaml
spec:
  containers:
  - image: python
    imagePullPolicy: Always
    name: yay2
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 250m
        memory: 64Mi
```

`kubectl apply -f pod.yaml`

</b></details>

## Мониторинг

<details>
<summary>Развертывание сервера метрик</summary><br><b>

`kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`

</b></details>

<details>
<summary>Используя метрики-сервер, просмотрите следующее:

* самые производительные узлы в кластере
* поды с наибольшим потреблением ресурсов</summary><br><b>

* узлы: `kubectl top nodes`
* поды: `kubectl top pods`

</b></details>

## Планировщик (дополнительно) {#scheduler-1}

<details>
<summary>Можете ли вы развернуть несколько планировщиков?</summary><br><b>

Да, это возможно. Можно запустить отдельный Pod с kube-scheduler и своим именем, например:

```yaml
spec:
  containers:
  - command:
    - kube-scheduler
    - --address=127.0.0.1
    - --leader-elect=true
    - --scheduler-name=some-custom-scheduler
...

```
</b></details>

<details>
<summary>Предположим, у вас есть несколько планировщиков. Как узнать, какой планировщик использовался для данного пода?</summary><br><b>

По событиям (`kubectl get events`) видно, какой scheduler обработал под.

</b></details>

<details>
<summary>Вы хотите запустить новый под и запланировать его с помощью специального планировщика. Как этого добиться?</summary><br><b>

Добавьте в манифест пода:

```yaml
spec:
  schedulerName: some-custom-scheduler
```

</b></details>
