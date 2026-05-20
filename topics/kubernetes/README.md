<a id="kubernetes"></a>
# Kubernetes

Какова ваша цель?

* Подготовиться к сертификации **CKA** — см. [CKA](CKA.md).
* Изучить Kubernetes по теории и практике — разделы [упражнений](#kubernetes-exercises) и [вопросов](#kubernetes-questions).
* Сфокусироваться на практике — начните с [упражнений](#kubernetes-exercises).

- [Kubernetes](#kubernetes)
  - [Упражнения Kubernetes](#kubernetes-exercises)
    - [Поды](#exercises-pods)
    - [Сервисы (Service)](#exercises-services)
    - [ReplicaSet](#exercises-replicaset)
    - [Метки и селекторы](#exercises-labels-selectors)
    - [Планировщик и taints](#exercises-scheduler-taints)
    - [Kustomize](#exercises-kustomize)
  - [Вопросы по Kubernetes](#kubernetes-questions)
    - [Kubernetes 101](#kubernetes-101)
    - [Кластер и архитектура](#cluster-and-architecture)
      - [Kubelet](#kubelet)
      - [Команды для узлов](#nodes-commands)
    - [Поды](#pods-questions)
      - [Статические поды](#static-pods)
      - [Команды подов](#pods-commands)
      - [Отладка подов](#pods-troubleshooting)
    - [Метки и селекторы](#labels-and-selectors-questions)
    - [Развёртывания (Deployments)](#deployments-questions)
      - [Команды deployments](#deployments-commands)
    - [Сервисы (Service)](#services-questions)
    - [Ingress](#ingress-questions)
    - [ReplicaSet](#replicasets-questions)
    - [DaemonSet](#daemonset)
      - [Команды DaemonSet](#daemonset-commands)
    - [StatefulSet](#statefulset)
    - [Хранилище](#storage-questions)
      - [Тома (volumes)](#volumes-under-storage)
    - [Сеть](#network-questions)
    - [Сетевые политики](#network-policies)
    - [etcd](#etcd)
    - [Пространства имён](#namespaces-questions)
      - [Команды пространств имён](#namespaces-commands)
      - [Квоты ресурсов](#resource-quota)
    - [Операторы](#operators-questions)
    - [Секреты](#secrets-questions)
    - [Тома и монтирование](#volume-mounts)
    - [RBAC](#rbac-questions)
    - [Шаблоны](#templates-questions)
    - [CronJob](#cronjob-questions)
    - [Разное](#kubernetes-misc)
    - [Gatekeeper](#gatekeeper)
    - [Политики и Conftest](#policy-testing)
    - [Helm](#helm-questions)
      - [Команды Helm](#helm-commands)
    - [Безопасность](#pod-security)
    - [Сценарии устранения неполадок](#troubleshooting-scenarios)
    - [Istio](#istio)
    - [Контроллеры](#controllers)
    - [Планировщик (Scheduler)](#scheduler)
      - [Node affinity](#node-affinity)
    - [Taints и tolerations](#taints)
    - [Requests и limits](#resource-limits)
      - [Команды (ресурсы)](#resource-limits-commands)
    - [Мониторинг](#monitoring)
    - [Kustomize](#kustomize-overlays)
    - [Стратегии развёртывания](#deployment-strategies)
    - [Сценарии](#scenarios)

<a id="kubernetes-exercises"></a>
## Упражнения Kubernetes

<a id="exercises-pods"></a>
### Поды

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Мой первый Pod | Поды | [Упражнение](pods_01.md) | [Решение](solutions/pods_01_solution.md) |
| «Убивающие» контейнеры | Поды | [Упражнение](killing_containers.md) | [Решение](solutions/killing_containers.md) |

<a id="exercises-services"></a>
### Сервисы (Service)

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Создание сервиса | Service | [Упражнение](services_01.md) | [Решение](solutions/services_01_solution.md) |

<a id="exercises-replicaset"></a>
### ReplicaSet

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Создание ReplicaSet | ReplicaSet | [Упражнение](replicaset_01.md) | [Решение](solutions/replicaset_01_solution.md) |
| Работа с ReplicaSet | ReplicaSet | [Упражнение](replicaset_02.md) | [Решение](solutions/replicaset_02_solution.md) |
| Селекторы ReplicaSet | ReplicaSet | [Упражнение](replicaset_03.md) | [Решение](solutions/replicaset_03_solution.md) |

<a id="exercises-labels-selectors"></a>
### Метки и селекторы

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Метки и селекторы 101 | Labels, selectors | [Упражнение](exercises/labels_and_selectors/exercise.md) | [Решение](exercises/labels_and_selectors/solution.md) |
| Селекторы узлов | nodeSelector | [Упражнение](exercises/node_selectors/exercise.md) | [Решение](exercises/node_selectors/solution.md) |

<a id="exercises-scheduler-taints"></a>
### Планировщик и taints

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Taints 101 | taints / tolerations | [Упражнение](exercises/taints_101/exercise.md) | [Решение](exercises/taints_101/solution.md) |

<a id="exercises-kustomize"></a>
### Kustomize

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Общие метки (commonLabels) | Kustomize | [Упражнение](exercises/kustomize_common_labels/exercise.md) | [Решение](exercises/kustomize_common_labels/solution.md) |

<a id="kubernetes-questions"></a>
## Вопросы по Kubernetes

<a id="kubernetes-101"></a>
### Kubernetes 101

<details>
<summary>Что такое Kubernetes? Зачем он организациям?</summary><br><b>

Kubernetes — это система с открытым исходным кодом, которая предоставляет пользователям возможность управлять, масштабировать и развертывать контейнерные приложения.

Чтобы понять, чем хорош Kubernetes, давайте рассмотрим несколько примеров:

* Вы хотите запустить определенное приложение в контейнере в нескольких разных местах и синхронизировать изменения во всех них, независимо от того, где они запускаются.
* Выполнение обновлений и изменений в сотнях контейнеров.
* Обработка случаев, когда текущая нагрузка требует увеличения (или уменьшения)

</b></details>

<details>
<summary>Когда и почему НЕ использовать Kubernetes?</summary><br><b>

- Если вы управляете инфраструктурой низкого уровня или «голым железом», Kubernetes, вероятно, не то, что вам нужно или что вам нужно.
  — Если у вас небольшая команда (менее 20 инженеров), использующая менее дюжины контейнеров, Kubernetes может оказаться излишним (даже если вам нужно масштабирование, развертывание обновлений и т. д.). Возможно, вы по-прежнему пользуетесь преимуществами использования управляемого Kubernetes, но вам определенно стоит тщательно об этом подумать, прежде чем принимать решение о его использовании.

</b></details>

<details>
<summary>Каковы некоторые возможности Kubernetes?</summary><br><b>

- Самовосстановление: Kubernetes использует проверки работоспособности для мониторинга контейнеров и выполнения определенных действий в случае сбоя или других типов событий, например перезапуска контейнера.
  - Балансировка нагрузки: Kubernetes может разделять и/или балансировать запросы к приложениям, работающим в кластере, в зависимости от состояния подов, на которых выполняется приложение.
  - Операторы: упакованные приложения Kubernetes, которые могут использовать API кластера для обновления его состояния и запуска действий на основе событий и изменений состояния приложения.
  - Автоматическое развертывание: постепенное обновление приложений и поддержка отката в случае, если что-то пойдет не так.
  - Масштабирование: масштабирование по горизонтали (вниз и вверх) на основе различных параметров состояния и пользовательских критериев.
  - Секреты: у вас есть механизм хранения имен пользователей, паролей и конечных точек служб конфиденциальным способом, который не каждый, кто использует кластер, может просмотреть его.

</b></details>

<details>
<summary>Какие объекты Kubernetes существуют?</summary><br><b>

* Под
  * Сервис
  * Контроллер репликации
  * Набор реплик
  * DaemonSet
  * Namespace
  * ConfigMap
  ...

</b></details>

<details>
<summary>Какие поля являются обязательными для любого объекта Kubernetes?</summary><br><b>

`metadata`, `kind` и `apiVersion`

</b></details>

<details>
<summary>Что такое kubectl?</summary><br><b>

Kubectl — это инструмент командной строки Kubernetes, который позволяет запускать команды в кластерах Kubernetes. Например, вы можете использовать kubectl для развертывания приложений, проверки ресурсов кластера и управления ими, а также просмотра журналов.

</b></details>

<details>
<summary>Какие объекты Kubernetes вы обычно используете при развертывании приложений в Kubernetes?</summary><br><b>

* Deployment — создает Pods() и наблюдает за ними
* Сервис: внутренняя маршрутизация трафика к подам.
* Ingress: маршрутизация трафика из-за пределов кластера.

</b></details>

<details>
<summary>Почему в Kubernetes нет такой команды? <code>kubectl get containers</code></summary><br><b>

Потому что контейнер не является объектом Kubernetes. Самая маленькая объектная единица в Kubernetes — это Pod. В одном поде вы можете найти один или несколько контейнеров.

</b></details>

<details>
<summary>Какие действия или операции вы считаете лучшими практиками, когда дело касается Kubernetes?</summary><br><b>

- Всегда проверяйте, что файлы YAML Kubernetes действительны. Рекомендуется применять автоматические проверки и конвейеры.
  - Всегда указывайте запросы и ограничения, чтобы предотвратить ситуацию, когда контейнеры используют всю память кластера, что может привести к проблеме OOM.
  - Укажите метки для логической группировки подов, развертываний и т. д. Используйте метки, например, для определения типа приложения, среди прочего.

</b></details>

<a id="cluster-and-architecture"></a>
### Кластер и архитектура

<details>
<summary>Что такое кластер Kubernetes?</summary><br><b>

Определение Red Hat: «Кластер Kubernetes — это набор узловых компьютеров для запуска контейнерных приложений. Если вы используете Kubernetes, вы используете кластер.
Как минимум, кластер содержит рабочий узел и главный узел».

Подробнее читайте [здесь](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-cluster)

</b></details>

<details>
<summary>Что такое узел?</summary><br><b>

Узел — это виртуальная или физическая машина, служащая рабочим устройством для запуска приложений.<br>
Рекомендуется иметь как минимум 3 узла в производственной среде.

</b></details>

<details>
<summary>За что отвечает мастер-нода?</summary><br><b>

Мастер координирует все рабочие процессы в кластере:

* Планирование подов
* Управление желаемым состоянием
* Выпуск новых обновлений

</b></details>

<details>
<summary>Кратко и подробно опишите, что происходит, когда вы запускаете <code>kubectl get nodes</code>.</summary><br><b>

1. Ваш пользователь проходит аутентификацию
2. Запрос проверяется kube-apiserver.
3. Данные извлекаются из etcd.

</b></details>

<details>
<summary>Правда или ложь? В каждом кластере должно быть 0 или более главных узлов и как минимум 1 рабочий узел.</summary><br><b>

Неверно. Кластер Kubernetes состоит как минимум из 1 мастера и может иметь 0 воркеров (хотя это было бы не очень полезно...)

</b></details> 

<details>
<summary>Каковы компоненты главного узла (он же плоскости управления)?</summary><br><b>

* Сервер API — API Kubernetes. Через него общаются все компоненты кластера.
  * Планировщик — назначает приложению рабочий узел, на котором оно может работать.
  * Диспетчер контроллеров — обслуживание кластера (репликации, сбои узлов и т. д.)
  *etcd — хранит конфигурацию кластера

</b></details>

<details>
<summary>Каковы компоненты рабочего узла (он же плоскости данных)?</summary><br><b>

* Kubelet — агент, отвечающий за связь узла с мастером.
  * Kube-proxy — балансировка нагрузки между компонентами приложения.
  * Время выполнения контейнера — движок запускает контейнеры (Podman, Docker,...)

</b></details>

<details>
<summary>Разместите компоненты в правой части изображения в нужном месте чертежа<br>
<img src="images/cluster_architecture_exercise.png"/></summary><br><b>

<img src="images/cluster_architecture_solution.png"/>

</b></details>

<details>
<summary>Вы управляете несколькими кластерами Kubernetes. Как быстро переключаться между кластерами с помощью kubectl?</summary><br><b>

`kubectl config use-context`

</b></details>

<details>
<summary>Как предотвратить чрезмерное использование памяти в кластере Kubernetes и возможные проблемы, такие как утечка памяти и OOM?</summary><br><b>

Применяйте запросы и ограничения, особенно к сторонним приложениям (где неопределенность еще больше)

</b></details>

<details>
<summary>Есть ли у вас опыт развертывания кластера Kubernetes? Если да, можете ли вы описать процесс на высоком уровне?</summary><br><b>

1. Создайте несколько экземпляров, которые вы будете использовать в качестве узлов/работников Kubernetes. Создайте также экземпляр, который будет действовать как Мастер. Экземпляры могут быть подготовлены в облаке или представлять собой виртуальные машины на хостах с голым железом.
2. Предоставьте центр сертификации, который будет использоваться для создания сертификатов TLS для различных компонентов кластера Kubernetes (kubelet, etcd,...).
  1. Создайте сертификат и закрытый ключ для различных компонентов.
3. Сгенерируйте конфигурации kubeconfig, чтобы разные клиенты Kubernetes могли находить серверы API и проходить аутентификацию.
4. Создайте ключ шифрования, который будет использоваться для шифрования данных кластера.
5. Создайте кластер etcd

</b></details>

<details>
<summary>Какая команда выведет список всех типов объектов в кластере?</summary><br><b>

`kubectl api-resources`

</b></details>

<details>
<summary>Что делает <code>kubectl get componentstatuses</code>?</summary><br><b>

Выводит состояние каждого из компонентов плоскости управления.

</b></details>

<a id="kubelet"></a>
#### Кубелет

<details>
<summary>Что произойдет с запуском подов, если вы остановите Kubelet на рабочих узлах?</summary><br><b>

Когда вы останавливаете службу kubelet на рабочем узле, она больше не сможет взаимодействовать с сервером API Kubernetes. В результате узел будет помечен как NotReady, а поды, работающие на этом узле, будут отмечены как Unknown. Затем плоскость управления Kubernetes попытается перепланировать поды на другие доступные узлы кластера.

</b></details>

<a id="nodes-commands"></a>
#### Команды узлов

<details>
<summary>Запустите команду для просмотра всех узлов кластера</summary><br><b>

`kubectl get nodes`

Примечание. Возможно, вы захотите создать псевдоним («alias k=kubectl») и привыкнуть к «k get no».

</b></details>

<details>
<summary>Создайте список всех узлов в формате JSON и сохраните его в файле с именем «some_nodes.json».</summary><br><b>

`k get nodes -o json > some_nodes.json`

</b></details>

<details>
<summary>Проверьте, какие метки имеет один из ваших узлов в кластере.</summary><br><b>

`kubectl get nodes --show-labels`

</b></details>

<a id="pods-questions"></a>
### Поды: вопросы

<details>
<summary>Объясните, что такое Pod</summary><br><b>

Под — это группа из одного или нескольких контейнеров с общим хранилищем и сетевыми ресурсами, а также спецификацией запуска контейнеров.

Поды — это наименьшие развертываемые вычислительные единицы, которые вы можете создавать и управлять ими в Kubernetes.

</b></details>

<details>
<summary>Разверните под под названием «my-pod», используя образ nginx:alpine.</summary><br><b>

`kubectl run my-pod --image=nginx:alpine`

Если вы новичок в Kubernetes, вы должны знать, что это не распространенный способ запуска подов. Обычный способ — запустить развертывание, которое, в свою очередь, запускает поды.

Кроме того, поды Pod и/или развертывания обычно определяются в файлах, а не выполняются напрямую с использованием только аргументов CLI.

</b></details>

<details>
<summary>Что вы думаете по поводу «Поды не предназначены для непосредственного создания»?</summary><br><b>

Поды обычно не создаются напрямую. Вы заметите, что поды обычно создаются как часть других объектов, таких как развертывания или наборы реплик.

Если под умирает, Kubernetes не вернет его обратно. Вот почему более полезно, например, определить наборы реплик, которые будут гарантировать, что заданное количество подов будет всегда работать, даже после смерти определенного пода.

</b></details>

<details>
<summary>Сколько контейнеров может содержать под?</summary><br><b>

Под может включать в себя несколько контейнеров, но в большинстве случаев это будет один контейнер на каждый под.

Существуют некоторые шаблоны, позволяющие запускать более одного контейнера, например шаблон «sidecar», где вам может потребоваться выполнить ведение журнала или какую-либо другую операцию, выполняемую другим контейнером, работающим с контейнером вашего приложения в том же поде.

</b></details>

<details>
<summary>Какие варианты использования существуют для запуска нескольких контейнеров в одном поде?</summary><br><b>

Одним из примеров является веб-приложение с отдельными (= в своих собственных контейнерах) компонентами/адаптерами ведения журнала и мониторинга.<br>
Конвейер CI/CD (например, с использованием Tekton) может запускать несколько контейнеров в одном поде, если задача содержит несколько команд.

</b></details>

<details>
<summary>Каковы возможные фазы Pod?</summary><br><b>

* Работает — под привязан к узлу и хотя бы один контейнер запущен.
  * Сбой/ошибка — по крайней мере один контейнер в поде завершился со сбоем.
  * Успешно — каждый контейнер в поде завершён успешно.
  * Неизвестно — состояние Pod невозможно получить.
  * Ожидание — контейнеры еще не запущены (возможно, изображения все еще загружаются или под еще не запланирован).

</b></details>

<details>
<summary>Правда или ложь? По умолчанию поды изолированы. Это означает, что они не могут получать трафик из любого источника.</summary><br><b>

Неверно. По умолчанию поды неизолированы: поды принимают трафик из любого источника.

</b></details>

<details>
<summary>Правда или ложь? Фаза `Pending` означает, что под еще не принят кластером Kubernetes, поэтому планировщик не сможет запустить его, пока он не будет принят.</summary><br><b>

Неверно. `Pending` — это после того, как под был принят кластером, но контейнер не может работать по разным причинам, например, изображения еще не загружены.

</b></details>

<details>
<summary>Правда или ложь? Один под может быть разделен на несколько узлов.</summary><br><b>

Неверно. Один под может работать на одном узле.

</b></details>

<details>
<summary>Вы запускаете под и видите статус <code>ContainerCreating</code>.</summary><br><b>

Под уже принят планировщиком и назначен на узел. Kubelet на узле скачивает образ(ы), монтирует тома и создаёт контейнеры — это нормальная промежуточная фаза. Если статус долго не меняется, смотрите `kubectl describe pod <POD_NAME>` (Events: `ImagePullBackOff`, `ErrImagePull`, проблемы с volume).

</b></details>

<details>
<summary>Правда или ложь? Том, определенный в Pod, доступен всем контейнерам этого Pod.</summary><br><b>

Верно.

</b></details>

<details>
<summary>Что происходит, когда вы запускаете под с помощью kubectl?</summary><br><b>

1. Kubectl отправляет запрос на сервер API (kube-apiserver) для создания пода.
   1. В процессе пользователь проходит аутентификацию и запрос проверяется.
   2. etcd обновляется с учетом данных
2. Планировщик обнаруживает наличие неназначенного пода, отслеживая сервер API (kube-apiserver).
3. Планировщик выбирает узел для назначения пода.
   1. etcd обновляется информацией
4. Планировщик сообщает серверу API о том, какой узел он выбрал.
5. Kubelet (который также отслеживает сервер API) замечает, что под тому же узлу, на котором он работает, назначен под, и что под не работает.
6. Kubelet отправляет запрос движку контейнеров (например, Docker) для создания и запуска контейнеров.
7. Kubelet отправляет обновление на сервер API (уведомляя его о том, что под запущен).
   1. etcd снова обновляется сервером API

</b></details>

<details>
<summary>Как убедиться, что контейнер запущен после запуска команды <code>kubectl run web --image nginxinc/nginx-unprivileged</code></summary><br><b>

* Когда вы запустите `kubectl describe pod <POD_NAME>`, он сообщит, запущен ли контейнер:
`State: Running` (в `kubectl describe pod`)
* Запустите команду внутри контейнера: `kubectl exec web -- ls`

</b></details>

<details>
<summary>После запуска <code>kubectl run Database --image mongo</code> вы увидите статус «CrashLoopBackOff». Что могло пойти не так и что вы делаете, чтобы это подтвердить?</summary><br><b>

«CrashLoopBackOff» означает, что под запускается, выходит из строя, запускается... и так повторяется.<br>
Существует много разных причин появления этой ошибки: отсутствие разрешений, неправильная конфигурация инициализационного контейнера, постоянная проблема с подключением тома и т. д.

Один из способов — `kubectl describe pod <POD_NAME>` и блок **Last State** / **Exit Code**:

```
Last State:     Terminated
Reason:         Error
Exit Code:      100
```

Другой способ — `kubectl logs <POD_NAME>` (журналы контейнеров в поде).

</b></details>

<details>
<summary>Объясните назначение следующих строк

```
livenessProbe:
  exec:
    command:
    - cat
    - /appStatus
  initialDelaySeconds: 10
  periodSeconds: 5
```

</summary><br><b>

Здесь настроена **liveness probe**. Она перезапускает контейнер при неуспешной проверке.<br>
Если `cat /appStatus` завершается с ошибкой, kubelet перезапустит контейнер согласно `restartPolicy`. `initialDelaySeconds: 10` — пауза перед первой проверкой; `periodSeconds: 5` — интервал между проверками.

</b></details>

<details>
<summary>Объясните назначение следующих строк

```
readinessProbe:
  tcpSocket:
    port: 2017
  initialDelaySeconds: 15
  periodSeconds: 20
```

</summary><br><b>

Это **readiness probe**: под не получит трафик от Service, пока TCP-проверка на порт `2017` не станет успешной. Первая проверка — через 15 с после старта контейнера, далее каждые 20 с.

</b></details>

<details>
<summary>Что означает статус пода «ErrImagePull»?</summary><br><b>

Не удалось получить образ, указанный для запуска контейнера(ов). Это может произойти, например, если клиент не прошел аутентификацию.<br>
Более подробную информацию можно получить с помощью `kubectl describe pod <POD_NAME>`.

</b></details>

<details>
<summary>Что произойдет, если вы удалите под?</summary><br><b>

1. Сигнал `TERM` отправляется для завершения основных процессов внутри контейнеров данного пода.
2. Каждому контейнеру дается 30 секунд на корректное завершение процессов.
3. Если льготный период истекает, сигнал KILL используется для принудительного завершения процессов, а также контейнеров.

</b></details>

<details>
<summary>Объясните, как работают датчики жизнеспособности</summary><br><b>

Проверка работоспособности — это полезный механизм, используемый для перезапуска контейнера в случае сбоя определенной проверки/проверки, определенной пользователем.<br>
Например, пользователь может определить, что команда `cat /app/status` будет выполняться каждые X секунд, и в момент сбоя этой команды контейнер будет перезапущен.

Подробнее об этом можно прочитать в [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes).

</b></details>

<details>
<summary>Объясните проверки готовности</summary><br><b>

тесты готовности, используемые Kubelet, чтобы узнать, когда контейнер готов начать работу и принимать трафик.<br>
Например, проверкой готовности может быть подключение порта 8080 контейнера. Как только Kubelet удастся его подключить, под помечается как готовый.

Подробнее об этом можно прочитать в [kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes).

</b></details>

<details>
<summary>Как статус проверки готовности влияет на услуги при их объединении?</summary><br><b>

Только контейнеры, состояние которых установлено на `Succeeded`, смогут получать запросы, отправленные в Сервис.

</b></details>

<details>
<summary>Почему в большинстве случаев на каждый под приходится иметь только один контейнер?</summary><br><b>

Одна из причин заключается в том, что масштабирование усложняется, когда вам нужно масштабировать только один из контейнеров в данном поде.

</b></details>

<details>
<summary>Правда или ложь? Как только под назначен рабочему узлу, он будет работать только на этом узле, даже если в какой-то момент он выйдет из строя и запустит новый под.</summary><br><b>

Верно.

</b></details>

<details>
<summary>Правда или ложь? Каждый под при создании получает свой собственный общедоступный IP-адрес.</summary><br><b>

Неверно. Каждый под получает IP-адрес, но внутренний и недоступный публично.

Чтобы сделать под доступным извне, нам нужно использовать объект под названием Service в Kubernetes.

</b></details>

<a id="static-pods"></a>
#### Статические поды

<details>
<summary>Что такое статические поды?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/): «Статические поды управляются непосредственно демоном kubelet на определенном узле, без наблюдения за ними со стороны сервера API. В отличие от подов, которые управляются плоскостью управления (например, развертыванием); вместо этого kubelet наблюдает за каждым статическим подом (и перезапускает его в случае сбоя).»

</b></details>

<details>
<summary>Правда или ложь? Помимо «статических подов», существуют и другие статические ресурсы, такие как «развертывания» и «репликасеты».</summary><br><b>

Неверно.

</b></details>

<details>
<summary>Каковы некоторые варианты использования Static Pods?</summary><br><b>

Одним из очевидных вариантов использования является запуск подов Control Plane — запуск таких подов, как kube-apiserver, планировщик и т. д. Они должны запускаться и работать независимо от того, работают некоторые компоненты кластера или нет, и они должны запускаться на определенных узлах кластера.

</b></details>

<details>
<summary>Как определить, какие поды являются статическими?</summary><br><b>

Имя static pod обычно имеет суффикс с именем узла (например, `kube-apiserver-minikube` на узле `minikube`). Надёжнее смотреть манифесты в `/etc/kubernetes/manifests/` на узле или поле `ownerReferences` в `kubectl get pod -o yaml`.

</b></details>

<details>
<summary>Что из перечисленного не является статическим подом?:

* kube-scheduler
* kube-proxy
* kube-apiserver</summary><br><b>

kube-proxy — это DaemonSet (поскольку он должен быть представлен на каждом узле кластера). Не существует какого-то конкретного узла, на котором он должен работать.

</b></details>

<details>
<summary>Где находятся статические манифесты подов?</summary><br><b>

Большую часть времени он находится в /etc/kubernetes/manifests, но вы можете проверить его с помощью `grep -i static /var/lib/kubelet/config.yaml`, чтобы найти значение `statisPodsPath`.

Возможно, ваша конфигурация находится в другом пути. Чтобы проверить, запустите `ps -ef | grep kubelet` и посмотрите, какое значение имеет аргумент --config процесса `/usr/bin/kubelet`

Сам ключ для определения пути статических подов — staticPodPath. Итак, если ваша конфигурация находится в `/var/lib/kubelet/config.yaml`, вы можете запустить `grep staticPodPath /var/lib/kubelet/config.yaml`.

</b></details>

<details>
<summary>Опишите, как бы вы удалили статический под</summary><br><b>

Найдите каталог статических подов (посмотрите staticPodPath в файле конфигурации kubelet).

Перейдите в этот каталог и удалите манифест/определение статического пода (`rm <STATIC_POD_PATH>/<POD_DEFINITION_FILE>`)

</b></details>

<a id="pods-commands"></a>
#### Команды подов

<details>
<summary>Как проверить, на каком рабочем узле были запланированы поды? Другими словами, как проверить, на каком узле работает тот или иной под?</summary><br><b>

`kubectl get pods -o Wide`

</b></details>

<details>
<summary>Как удалить под?</summary><br><b>

`kubectl delete pod pod_name`

</b></details>

<details>
<summary>Перечислите все поды с меткой «env=prod».</summary><br><b>

`k get po -l env=prod`

Чтобы их подсчитать: `k get po -l env=prod --no-headers | wc -l`

</b></details>

<details>
<summary>Как составить список подов в текущем пространстве имен?</summary><br><b>

`kubectl get po`

</b></details>

<details>
<summary>Как просмотреть все поды, работающие во всех пространствах имен?</summary><br><b>

`kubectl get pods --all-namespaces`

</b></details>

<a id="pods-troubleshooting"></a>
#### Устранение неполадок и отладка подов

<details>
<summary>Вы пытаетесь запустить под, но он находится в состоянии `Pending`. В чем может быть причина?</summary><br><b>

Одна из возможных причин заключается в том, что планировщик, который должен планировать поды на узлах, не работает. Чтобы проверить это, вы можете запустить `kubectl get po -A | grep scheduler` или проверьте непосредственно в пространстве имен `kube-system`.

</b></details>

<details>
<summary>Что делает команда <code>kubectl logs [pod-name]</code>?</summary><br><b>

Печатает журналы для контейнера в поде.

</b></details>

<details>
<summary>Что делает команда <code>kubectl describe pod [имя пода]</code>?</summary><br><b>

Показать подробную информацию о конкретном ресурсе или группе ресурсов.

</b></details>

<details>
<summary>Создайте статический под с изображением <code>python</code>, который запускает команду <code>sleep 2017</code></summary><br><b>

Сначала перейдите в каталог, отслеживаемый kubelet для создания статического пода: `cd /etc/kubernetes/manifests` (вы можете проверить путь, прочитав файл конфигурации kubelet)

Теперь создайте определение/манифест в этом каталоге.
`k run some-pod --image=python --command Sleep 2017 --restart=Never --dry-run=client -o yaml > statuc-pod.yaml`

</b></details>

<a id="labels-and-selectors-questions"></a>
### Метки и селекторы

<details>
<summary>Объяснение ярлыков</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/): «Метки (labels) — это пары ключ/значение, прикреплённые к объектам, таким как поды. Метки предназначены для использования для указания идентифицирующих атрибутов объектов, которые имеют смысл и актуальны для пользователей, но не подразумевают напрямую семантику для базовой системы. Метки можно использовать для организации и выбора подмножеств объектов. Метки могут быть прикреплены к объектам во время создания, а затем добавлены и изменены в любое время. Для каждого объекта может быть определен набор меток «ключ/значение». Каждый ключ должен быть уникальным для данного объекта.

</b></details>

<details>
<summary>Объяснение селекторов</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors): «В отличие от имен и UID, метки не обеспечивают уникальности. В общем, мы ожидаем, что многие объекты будут иметь одинаковые метки.

С помощью селектора меток клиент/пользователь может идентифицировать набор объектов. Селектор меток — это основной примитив группировки в Kubernetes.

В настоящее время API поддерживает два типа селекторов: на основе равенства и на основе набора. Селектор меток может состоять из нескольких требований, разделенных запятыми. В случае нескольких требований все они должны быть удовлетворены, чтобы разделитель-запятая действовал как логический оператор И (&&).

</b></details>

<details>
<summary>Приведите несколько реальных примеров использования меток.</summary><br><b>

* Может использоваться планировщиком для размещения определенных подов (с определенными метками) на определенных узлах.
* Используется наборами реплик для отслеживания подов, которые необходимо масштабировать.

</b></details>

<details>
<summary>Что такое аннотации?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/): «Вы можете использовать аннотации Kubernetes для прикрепления произвольных неидентифицирующих метаданных к объектам. Клиенты, такие как инструменты и библиотеки, могут получать эти метаданные».

</b></details>

<details>
<summary>Чем аннотации отличаются от меток?</summary><br><b>

[Kuberenets.io](Ярлыки могут использоваться для выбора объектов и для поиска коллекций объектов, удовлетворяющих определенным условиям. Напротив, аннотации не используются для идентификации и выбора объектов. Метаданные в аннотации могут быть маленькими или большими, структурированными или неструктурированными и могут включать символы, не разрешенные метками.): «Ярлыки можно использовать для выбора объектов и для поиска коллекций объектов, которые удовлетворяют определенным условиям. Напротив, аннотации не используются для идентификации и выбора объектов. Метаданные аннотации могут быть маленькими или большими, структурированными или неструктурированными и могут включать символы, не разрешенные метками».

</b></details>

<details>
<summary>Как просмотреть журналы контейнера, работающего в поде?</summary><br><b>

`k журналов POD_NAME`

</b></details>

<details>
<summary>Внутри пода есть два контейнера, которые называются «some-pod». Что произойдет, если вы запустите <code>kubectl logs some-pod</code></summary><br><b>

Это не сработает, потому что внутри пода есть два контейнера, и вам нужно указать один из них с помощью `kubectl logs POD_NAME -c CONTAINER_NAME`

</b></details>

<a id="deployments-questions"></a>
### Развертывания

<details>
<summary>Что такое «развертывание» в Kubernetes?</summary><br><b>

Развертывание Kubernetes используется, чтобы сообщить Kubernetes, как создавать или изменять экземпляры подов, содержащих контейнеризованное приложение.
При развертывании можно масштабировать количество подов реплик, обеспечивать контролируемое развертывание обновленного кода или при необходимости выполнять откат к более ранней версии развертывания. 

Развертывание — это декларативное заявление о желаемом состоянии подов и наборов реплик.

</b></details>

<details>
<summary>Как создать развертывание с образом «nginx:alpine»?</summary><br><b>

`kubectl create deployment my-first-deployment --image=nginx:alpine`

Или через манифест:

```bash
cat <<'EOF' | kubectl create -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
EOF
```

</b></details>

<details>
<summary>Как проверить, что развертывание было создано?</summary><br><b>

`kubectl get Deployments` или `kubectl get Deployment`

Эта команда выводит список всех Deployment в кластере. Это не означает, что поды уже запущены — смотрите столбцы **READY** и **AVAILABLE**.

</b></details>

<details>
<summary>Как редактировать Deployment?</summary><br><b>

`kubectl edit deployment <DEPLOYMENT_NAME>`

</b></details>

<details>
<summary>Что произойдет после редактирования развертывания и изменения образа?</summary><br><b>

Под завершится и будет создан другой, новый под.

Кроме того, просматривая набор реплик, вы увидите, что в старой реплике нет подов, и создается новый набор реплик.

</b></details>

<details>
<summary>Как удалить развертывание?</summary><br><b>

Один из способов — указать имя развертывания: `kubectl delete Deployment [deployment_name]`

Другой способ — использовать файл конфигурации развертывания: `kubectl delete -f Deployment.yaml`

</b></details>

<details>
<summary>Что произойдет, если вы удалите развертывание?</summary><br><b>

Под, связанный с развертыванием, завершится, а набор реплик будет удален.

</b></details>

<details>
<summary>Что происходит за кулисами, когда вы создаете объект развертывания?</summary><br><b>

Следующее происходит, когда вы запускаете `kubectl create Deployment some_deployment --image=nginx`

1. HTTP-запрос отправляется на API-сервер Kubernetes в кластере для создания нового развертывания.
2. Создается новый объект Pod и назначается одному из рабочих узлов.
3. Kublet на рабочем узле замечает новый под и дает команду механизму среды выполнения контейнера извлечь образ из реестра.
4. Новый контейнер создается с использованием только что полученного образа.

</b></details>

<details>
<summary>Как сделать приложение доступным в частной или внешней сети?</summary><br><b>

Использование сервиса.

</b></details>

<details>
<summary>Можете ли вы использовать развертывание для приложений с отслеживанием состояния?</summary><br><b>

Технически да, но для stateful-нагрузок обычно выбирают **StatefulSet**: стабильные имена подов (`pod-0`, `pod-1`), упорядоченный запуск/масштабирование, отдельные PVC на реплику. Deployment подходит для stateless; для БД и кластеров с постоянной идентичностью узлов — StatefulSet.

</b></details>

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

<a id="deployments-commands"></a>
#### Команды развертывания

<details>
<summary>Создайте определение файла/манифест развертывания под названием «dep» с тремя репликами, использующими образ «redis».</summary><br><b>

`kubectl create deployment dep -o yaml --image=redis --dry-run=client --replicas 3 > Deployment.yaml `

</b></details>

<details>
<summary>Удалите развертывание `depdep`</summary><br><b>

`kubectl delete deployment depdep`

</b></details>

<details>
<summary>Создайте развертывание под названием «pluck», используя образ «redis», и убедитесь, что оно запускает 5 реплик.</summary><br><b>

`kubectl create deployment pluck --image=redis`

`kubectl scale deployment pluck --replicas=5`

</b></details>

<details>
<summary>Создайте развертывание со следующими свойствами:

* называется "блеф"
* используя изображение «питон»
* запускает 3 реплики
* все поды будут размещены на узле с меткой «blufer».</summary><br><b>

`kubectl create deployment blufer --image=python --replicas=3 -o yaml --dry-run=client > Deployment.yaml`

Отредактируйте `Deployment.yaml` и добавьте блок:

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

Затем: `kubectl apply -f Deployment.yaml`

</b></details>

<a id="services-questions"></a>
### Сервисы

<details>
<summary>Что такое служба в Kubernetes?</summary><br><b>

«Абстрактный способ представить приложение, работающее на наборе подов, в качестве сетевой службы». - подробнее читайте [здесь](https://kubernetes.io/docs/concepts/services-networking/service)

Проще говоря, он позволяет вам добавить внутреннее или внешнее подключение к определенному приложению, работающему в контейнере.

</b></details>

<details>
<summary>Разместите компоненты в нужных местах для службы Kubernetes<br>
<img src="images/service_exercise.png"/></summary><br><b>

<img src="images/service_solution.png"/>

</b></details>


<details>
<summary>Как создать службу для существующего развертывания под названием «alle» на порту 8080, чтобы поды были доступны через балансировщик нагрузки?</summary><br><b>

Императивный способ:

`kubectl expose deployment alle --type=LoadBalancer --port 8080`

</b></details>

<details>
<summary>Правда или ложь? Жизненный цикл подов и служб не связан, поэтому, когда под умирает, служба все равно остается.</summary><br><b>

Верно

</b></details>

<details>
<summary>Как после создания сервиса проверить, что он создан?</summary><br><b>

`kubectl get svc`

</b></details>

<details>
<summary>Какой тип службы по умолчанию?</summary><br><b>

ClusterIP — используется для внутренней связи.

</b></details>

<details>
<summary>Какие типы услуг существуют?</summary><br><b>

* ClusterIP
* NodePort
* LoadBalancer
* ExternalName

Подробнее об этой теме [здесь](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)

</b></details>

<details>
<summary>Как связаны обслуживание и развертывание?</summary><br><b>

Правда в том, что они не связаны. Служба указывает на поды напрямую, без какого-либо подключения к развертыванию.

</b></details>

<details>
<summary>Каковы важные шаги при определении/добавлении услуги?</summary><br><b>

1. Убедитесь, что целевой порт службы соответствует порту контейнера пода.
2. Убедитесь, что селектор соответствует хотя бы одному из ярлыков пода.

</b></details>

<details>
<summary>Какой тип службы по умолчанию в Kubernetes и для чего он используется?</summary><br><b>

По умолчанию используется ClusterIP, и он используется для внутреннего раскрытия порта. Это полезно, если вы хотите включить внутреннюю связь между подами и предотвратить любой внешний доступ.

</b></details>

<details>
<summary>Как получить информацию по определенной услуге?</summary><br><b>

`kubectl describe svc <SERVICE_NAME>`

</b></details>

<details>
<summary>Что делает следующая команда?

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```

</summary><br><b>

Он предоставляет ReplicaSet, создавая службу под названием «replicaset-svc». Открытый порт — 2017 (это порт, используемый приложением), а тип службы — NodePort, что означает, что он будет доступен извне.

</b></details>

<details>
<summary>Правда или ложь? целевой порт в случае выполнения следующей команды будет доступен только на одном из узлов кластера Kubernetes, но будет перенаправлен на все поды

```
kubectl expose rs some-replicaset --name=replicaset-svc --target-port=2017 --type=NodePort
```

</summary><br><b>

Неверно. Он будет доступен на каждом узле кластера и будет перенаправлен на один из подов (которые принадлежат ReplicaSet).

</b></details>

<details>
<summary>Как проверить, что определенная служба настроена на пересылку запросов в данный под</summary><br><b>

Выполните `kubectl describe svc <SERVICE_NAME>` и сравните IP в **Endpoints** с какими-либо IP-адресами из вывода `kubectl get pods -o wide`

</b></details>

<details>
<summary>Объясните, что произойдет при запуске Apply в следующем блоке.

```
apiVersion: v1
kind: Service
metadata:
  name: some-app
spec:
  type: NodePort
  ports:
  - port: 8080
    nodePort: 2017
    protocol: TCP
  selector:
    type: backend
    service: some-app
```

</summary><br><b>

Он создает новую службу типа «NodePort», что означает, что ее можно использовать для внутренней и внешней связи с приложением.<br>
Порт приложения — 8080, и запросы будут перенаправляться на этот порт. Открытый порт — 2017. Обратите внимание: указание nodePort не является общепринятой практикой.<br>
В качестве порта использовался TCP (вместо UDP), это также порт по умолчанию, поэтому его не нужно указывать.<br>
Селектор, используемый Службой, чтобы знать, в какие поды пересылать запросы. В данном случае это поды с метками «type: backend» и «service: some-app».<br>

</b></details>

<details>
<summary>Как превратить следующий сервис во внешний?

```
spec:
  selector:
    app: some-app
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
```

</summary><br><b>

Добавьте `type: LoadBalancer` и при необходимости `nodePort`:

```
spec:
  selector:
    app: some-app
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 32412
```

</b></details>

<details>
<summary>Что бы вы использовали для маршрутизации трафика за пределами кластера Kubernetes к службам внутри кластера?</summary><br><b>

Вход

</b></details>

<details>
<summary>Правда или ложь? При использовании «NodePort» «ClusterIP» будет создан автоматически?</summary><br><b>

Верно

</b></details>

<details>
<summary>Когда вы будете использовать тип «LoadBalancer»</summary><br><b>

В основном, когда вы хотите объединить его с балансировщиком нагрузки облачного провайдера.

</b></details>

<details>
<summary>Как бы вы сопоставили службу с внешним адресом?</summary><br><b>

Использование директивы «Внешнее имя».

</b></details>

<details>
<summary>Подробно опишите, что происходит при создании сервиса.</summary><br><b>

1. Kubectl отправляет запрос на сервер API для создания Сервиса.
2. Контроллер обнаруживает новую услугу.
3. Объекты конечных точек, созданные контроллером с тем же именем, что и служба.
4. Контроллер использует селектор услуг для идентификации конечных точек.
5. kube-proxy обнаруживает наличие нового объекта конечной точки + новой службы и добавляет правила iptables для захвата трафика к порту службы и перенаправления его на конечные точки.
6. kube-dns обнаруживает наличие новой службы и добавляет запись контейнера на DNS-сервер.

</b></details>

<details>
<summary>Как перечислить конечные точки определенного приложения?</summary><br><b>

`kubectl get ep <имя>`

</b></details>

<details>
<summary>Как вы можете узнать информацию об Сервисе, относящемся к определенному поду, если все, что вы можете использовать, это <code>kubectl exec <POD_NAME> -- </code></summary><br><b>

Вы можете запустить `kubectl exec <POD_NAME> -- env`, который предоставит вам пару переменных среды, связанных со Службой.<br>
Такие переменные, как `[SERVICE_NAME]_SERVICE_HOST`, `[SERVICE_NAME]_SERVICE_PORT`,...

</b></details>

<details>
<summary>Опишите, что происходит, когда контейнер впервые пытается подключиться к соответствующей службе. Объясните, кто добавил каждый из компонентов, которые вы включаете в описание.</summary><br><b>

- Контейнер просматривает сервер имен, определенный в /etc/resolv.conf.
  - Контейнер запрашивает сервер имен, чтобы адрес был преобразован в IP-адрес службы.
  - Запросы, отправленные на IP-адрес службы, пересылаются с помощью правил iptables (или другого выбранного программного обеспечения) на конечные точки.

Объяснение того, кто их добавил:

  — Сервер имен в контейнере добавляется kubelet во время планирования пода с помощью kube-dns.
  - DNS-запись сервиса добавляется kube-dns при создании сервиса.
  - правила iptables добавляются kube-proxy во время создания конечной точки и службы.

</b></details>

<details>
<summary>Опишите в общих чертах, что происходит при запуске <code>kubectl expose Deployment Remo --type=LoadBalancer --port 8080</code></summary><br><b>

1. Kubectl отправляет запрос Kubernetes API на создание объекта Service.
2. Kubernetes просит поставщика облачных услуг (например, AWS, GCP, Azure) предоставить балансировщик нагрузки.
3. Вновь созданный балансировщик нагрузки перенаправляет входящий трафик на соответствующие рабочие узлы, которые пересылают трафик в соответствующие контейнеры.

</b></details>

<details>
<summary>После создания службы, которая перенаправляет входящий внешний трафик в контейнерное приложение, как убедиться, что она работает?</summary><br><b>

Вы можете запустить `curl <SERVICE IP>:<SERVICE PORT>`, чтобы проверить выходные данные.

</b></details>

<details>
<summary>Внутренний балансировщик нагрузки в Kubernetes называется <code>____</code>, а внешний балансировщик нагрузки — <code>____</code>.</summary><br><b>

Внутренний балансировщик нагрузки в Kubernetes называется Service, а внешний балансировщик нагрузки — Ingress.

</b></details>

<a id="ingress-questions"></a>
### Вход

<details>
<summary>Что такое Ингресс?</summary><br><b>

Из документации Kubernetes: «Ingress предоставляет маршруты HTTP и HTTPS извне кластера службам внутри кластера. Маршрутизация трафика контролируется правилами, определенными в ресурсе Ingress».

Подробнее читайте [здесь](https://kubernetes.io/docs/concepts/services-networking/ingress/)

</b></details>

<details>
<summary>Заполните следующий файл конфигурации, чтобы сделать его входным.

```
metadata:
  name: someapp-ingress
spec:
```

</summary><br><b>

Есть несколько способов ответить на этот вопрос.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          serviceName: someapp-internal-service
          servicePort: 8080
```

</b></details>


<details>
<summary>Объясните значение директив «http», «host» и «backend».

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: someapp-ingress
spec:
  rules:
  - host: my.host
    http:
      paths:
      - backend:
          service:
            name: someapp-internal-service
            port:
              number: 8080
```

</summary><br><b>

хост — это точка входа в кластер, поэтому, по сути, это действительный адрес домена, который соответствует IP-адресу узла кластера<br>
строка http, используемая для указания того, что входящие запросы будут пересылаться во внутреннюю службу с использованием http.<br>
серверная часть ссылается на внутреннюю службу (serviceName — это имя в метаданных, а servicePort — это порт в разделе портов).

</b></details>

<details>
<summary>Почему использование подстановочного знака на входном хосте может привести к проблемам?</summary><br><b>

Причина, по которой вам не следует использовать подстановочные знаки в хосте (например, `-host: *`), заключается в том, что вы, по сути, указываете своему кластеру Kubernetes перенаправлять весь трафик в контейнер, в котором вы использовали этот входной трафик. Это может привести к выходу из строя всего кластера.

</b></details>

<details>
<summary>Что такое входной контроллер?</summary><br><b>

Реализация для Ingress. По сути, это еще один под (или набор подов), который оценивает и обрабатывает правила Ingress и управляет всеми перенаправлениями. 

Существует несколько реализаций Ingress Controller (одна из Kubernetes — Kubernetes Nginx Ingress Controller).

</b></details>

<details>
<summary>Каковы некоторые варианты использования Ingress?</summary><br><b>

* Несколько поддоменов (несколько записей хостов, каждая со своей службой)
* Один домен с несколькими службами (несколько путей, каждый из которых сопоставлен с разными службами/приложениями).

</b></details>

<details>
<summary>Как включить Ingress в ваше пространство имен?</summary><br><b>

kubectl get ingress

</b></details>

<details>
<summary>Что такое входной бэкэнд по умолчанию?</summary><br><b>

Он определяет, что делать с входящим запросом к кластеру Kubernetes, который не сопоставлен ни с одним бэкэндом (= нет правила для сопоставления запроса со службой). Если серверная служба по умолчанию не определена, рекомендуется определить ее, чтобы пользователи по-прежнему видели какое-то сообщение вместо ничего или неясной ошибки.

</b></details>

<details>
<summary>Как настроить бэкэнд по умолчанию?</summary><br><b>

Создайте ресурс службы, который указывает имя серверной части по умолчанию, как указано в `kubectl describe ingress...`, и порт в разделе портов.

</b></details>

<details>
<summary>Как настроить TLS с Ingress?</summary><br><b>

Добавьте записи tls и secretName.

```
spec:
  tls:
  - hosts:
    - some_app.com
    secretName: someapp-secret-tls
```

</b></details>

<details>
<summary>Правда или ложь? При настройке Ingress с помощью TLS компонент Secret должен находиться в том же пространстве имен, что и компонент Ingress.</summary><br><b>

Верно

</b></details>

<details>
<summary>Какую концепцию Kubernetes вы бы использовали для управления потоком трафика на уровне IP-адреса или порта?</summary><br><b>

Сетевые политики

</b></details>

<details>
<summary>Как масштабировать приложение (развертывание), чтобы оно запускало более одного экземпляра приложения?</summary><br><b>

Запустить два экземпляра приложения?

`kubectl scale deployment <DEPLOYMENT_NAME> --replicas=2`

Вы можете указать любое другое число, при условии, что ваше приложение умеет масштабироваться.

</b></details>

<a id="replicasets-questions"></a>
### Наборы реплик

<details>
<summary>Какова цель ReplicaSet?</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset): «Цель ReplicaSet — поддерживать стабильный набор подов-реплик, работающих в любой момент времени. Таким образом, он часто используется для гарантии доступности определенного количества идентичных подов».

Проще говоря, ReplicaSet гарантирует, что указанное количество реплик подов будет запущено для выбранного пода. Если подов больше, чем определено в ReplicaSet, некоторые из них будут удалены. Если их меньше, чем определено в ReplicaSet, будет добавлено больше реплик.

</b></details>

<details>
<summary>Что делает следующий блок строк?

```
spec:
  replicas: 2
  selector:
    matchLabels:
      type: backend
  template:
    metadata:
      labels:
        type: backend
    spec:
      containers:
      - name: httpd-yeah
        image: httpd
```

</summary><br><b>

Определяет ReplicaSet для подов с меткой `type: backend`; одновременно будут работать 2 пода.

</b></details>

<details>
<summary>Что произойдет, если под, созданный ReplicaSet, будет удален напрямую с помощью <code>kubectl delete po ...</code>?</summary><br><b>

ReplicaSet создаст новый под, чтобы достичь желаемого количества реплик.

</b></details>

<details>
<summary>Правда или ложь? Если ReplicaSet определяет 2 реплики, но работают 3 пода, соответствующие селектору ReplicaSet, он ничего не сделает.</summary><br><b>

Неверно. Он завершит работу одного из подов для достижения желаемого состояния двух реплик.

</b></details>

<details>
<summary>Опишите последовательность событий в случае создания ReplicaSet.</summary><br><b>

* Клиент (например, kubectl) отправляет запрос на сервер API для создания ReplicaSet.
* Контроллер обнаруживает новое событие, запрашивающее набор реплик.
* Контроллер создает новые определения Pod (точное количество зависит от того, что определено в определении ReplicaSet).
* Планировщик обнаруживает неназначенные поды и решает, каким узлам их назначить. Эта информация отправляется на сервер API
* Kubelet обнаруживает, что к узлу, на котором он работает, были назначены два пода (поскольку он постоянно наблюдает за сервером API).
* Kubelet отправляет запросы контейнерному движку для создания контейнеров, которые являются частью Pod.
* Kubelet отправляет запрос на сервер API, чтобы уведомить его о создании подов.

</b></details>

<details>
<summary>Как перечислить наборы реплик в текущем пространстве имен?</summary><br><b>

`kubectl get rs`

</b></details>

<details>
<summary>Можно ли удалить ReplicaSet, не удаляя созданные им поды?</summary><br><b>

Да, с `--cascase=false`.

`kubectl delete -f rs.yaml --cascade=false`

</b></details>

<details>
<summary>Каково количество реплик по умолчанию, если оно не указано явно?</summary><br><b>

1

</b></details>

<details>
<summary>Что означает следующий вывод <code>kubectl get rs</code>?

ИМЯ ЖЕЛАЕМЫЙ НАСТОЯЩИЙ ВОЗРАСТ ГОТОВНОСТИ
сеть 2 2 0 2м23с</summary><br><b>

Набор реплик `web` имеет 2 реплики. Похоже, что контейнеры внутри подов еще не запущены, поскольку значение READY равно 0. Это может быть нормально, поскольку для запуска некоторых контейнеров требуется время, и это может быть связано с ошибкой. Выполнение `kubectl describe pod POD_NAME` или `kubectl logs POD_NAME` может дать нам дополнительную информацию.

</b></details>

<details>
<summary>Правда или ложь? Поды, указанные в поле выбора ReplicaSet, должны быть созданы самим ReplicaSet.</summary><br><b>

Неверно. Поды могут быть уже запущены и изначально могут быть созданы любым объектом. Для ReplicaSet это не имеет значения и не требует от него их получения и мониторинга.

</b></details>

<details>
<summary>Правда или ложь? В случае ReplicaSet, если поды, указанные в поле выбора, не существуют, ReplicaSet будет ждать их запуска, прежде чем что-либо делать.</summary><br><b>

Неверно. Он позаботится о запуске недостающих подов.

</b></details>

<details>
<summary>В случае набора реплик какое поле является обязательным в разделе спецификации?</summary><br><b>

Поле «шаблон» в разделе спецификации является обязательным. Он используется ReplicaSet для создания новых подов при необходимости.

</b></details>

<details>
<summary>Вы создали ReplicaSet. Как проверить, нашел ли ReplicaSet соответствующие поды или создал новые поды?</summary><br><b>

`kubectl describe rs <имя ReplicaSet>`

Оно будет видно в разделе «События» (самые последние строки).

</b></details>

<details>
<summary>Правда или ложь? Удаление ReplicaSet приведет к удалению созданных им подов.</summary><br><b>

Верно (и не только Pods, но и все остальное, что он создал).

</b></details>

<details>
<summary>Правда или ложь? Удаление метки из пода, отслеживаемого набором реплик, приведет к тому, что набор реплик создаст новый под.</summary><br><b>

Верно. Когда метка, используемая ReplicaSet в поле выбора, удаляется из пода, этот под больше не контролируется ReplicaSet, и ReplicaSet создаст новый под, чтобы компенсировать тот, который он «потерял».

</b></details>

<details>
<summary>Как масштабировать развертывание до 8 реплик?</summary><br><b>

`kubectl scale deployment <DEPLOYMENT_NAME> --replicas=8`

</b></details>

<details>
<summary>Наборы реплик запускаются в тот момент, когда пользователь выполнил команду для их создания (например, <code>kubectl create -f rs.yaml</code>).</summary><br><b>

Неверно. Создание может занять время. Проверьте `kubectl get rs` и столбец **READY**.

</b></details>

<details>
<summary>Как представить ReplicaSet как новую услугу?</summary><br><b>

`kubectl expose rs <Имя набора реплик> --name=<Имя службы> --target-port=<Порт для предоставления> --type=NodePort`

Несколько примечаний:
  - целевой порт зависит от того, какой порт приложение использует в контейнере
  - тип может быть другим и не обязательно должен быть именно «NodePort».

</b></details>

<details>
<summary>Исправьте следующее определение ReplicaSet.

```yaml
apiVersion: apps/v1
kind: ReplicaCet
metadata:
  name: редис
  labels:
    app: редис
    tier: кэш
spec:
  selector:
    matchLabels:
      tier: кэш
  template:
    metadata:
      labels:
        tier: тайник
    spec:
      containers:
      - name: редис
        image: редис
```

</summary><br><b>

вид должен быть ReplicaSet, а не ReplicaCet :)

</b></details>

<details>
<summary>Исправьте следующее определение ReplicaSet.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: редис
  labels:
    app: редис
    tier: кэш
spec:
  selector:
    matchLabels:
      tier: кэш
  template:
    metadata:
      labels:
        tier: тайник
    spec:
      containers:
      - name: редис
        image: редис
```

</summary><br><b>

Селектор не соответствует метке (кэш против кэша). Чтобы решить эту проблему, исправьте кэширование, чтобы вместо него использовался кэш.

</b></details>

<details>
<summary>Как проверить, какой образ контейнера использовался как часть набора реплик под названием «repli»?</summary><br><b>

`kubectl describe rs repli | grep -i image`

</b></details>

<details>
<summary>Как проверить, сколько подовs готово в составе набора реплик под названием «repli»?</summary><br><b>

`kubectl describe rs repli | grep -i "Pods Status"`

</b></details>

<details>
<summary>Как удалить набор реплик под названием «рори»?</summary><br><b>

`kubectl delete rs rori`

</b></details>

<details>
<summary>Как изменить набор реплик под названием «рори», чтобы использовать другое изображение?</summary><br><b>

`к эдис рс рори`

</b></details>

<details>
<summary>Увеличьте масштаб набора реплик под названием «rori», чтобы запускать 5 подов вместо 2.</summary><br><b>

`kubectl scale rs rori --replicas=5`

</b></details>

<details>
<summary>Уменьшите масштаб набора реплик под названием «rori», чтобы запустить 1 под вместо 5.</summary><br><b>

`kubectl scale rs rori --replicas=1`

</b></details>

<a id="daemonset"></a>
### DaemonSet

<details>
<summary>Что такое DaemonSet?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset): «DaemonSet гарантирует, что на всех (или некоторых) узлах выполняется копия пода. Когда узлы добавляются в кластер, к ним добавляются поды. Когда узлы удаляются из кластера, эти поды подлежат сборке мусора. Удаление DaemonSet очистит созданные им поды».

</b></details>

<details>
<summary>В чем разница между ReplicaSet и DaemonSet?</summary><br><b>

Цель ReplicaSet — поддерживать стабильный набор подов реплик, работающих в любой момент времени.
DaemonSet гарантирует, что на всех узлах будет запущена копия пода.

</b></details>

<details>
<summary>Каковы некоторые варианты использования DaemonSet?</summary><br><b>

* Мониторинг: вы хотите осуществлять мониторинг на каждом узле кластера. Например, под datadog запускается на каждом узле с использованием набора демонов.
* Ведение журнала: вы хотели бы настроить ведение журнала на каждом узле вашего кластера.
* Сеть: на каждом узле необходим сетевой компонент, чтобы все узлы могли обмениваться данными между собой.

</b></details>

<details>
<summary>Как работает DaemonSet?</summary><br><b>

Исторически, начиная с версии 1.12, это делалось с помощью атрибута NodeName.

Начиная с версии 1.12, это достигается с помощью обычного планировщика и привязки узлов.

</b></details>

<a id="daemonset-commands"></a>
#### DaemonSet — команды

<details>
<summary>Как составить список всех наборов демонов в текущем пространстве имен?</summary><br><b>

`kubectl get ds`

</b></details>

<a id="statefulset"></a>
### StatefulSet

<details>
<summary>Объясните StatefulSet</summary><br><b>

StatefulSet — это объект API рабочей нагрузки, используемый для управления приложениями с отслеживанием состояния. Управляет развертыванием и масштабированием набора подов и предоставляет гарантии порядка и уникальности этих подов.[Подробнее](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

</b></details>

<a id="storage-questions"></a>
### Хранилище

<a id="volumes-under-storage"></a>
#### Тома

<details>
<summary>Что такое объем в отношении Kubernetes?</summary><br><b>

Каталог, доступный контейнерам внутри определенного пода и контейнеров. Механизм, отвечающий за создание каталога, управление им... в основном зависит от типа тома.

</b></details>

<details>
<summary>Какие типы томов вам известны?</summary><br><b>

*emptyDir: создается, когда под назначается узлу, и перестает существовать, когда под больше не работает на этом узле.
* HostPath: монтирует путь от самого хоста. Обычно не используется из-за угроз безопасности, но имеет множество случаев использования, где это необходимо, например, доступ к некоторым внутренним путям хоста (/sys, /var/lib и т. д.).

</b></details>

<details>
<summary>Какие проблемы решают тома в Kubernetes?</summary><br><b>

1. Совместное использование файлов между контейнерами, работающими в одном поде.
2. Хранение в контейнерах кратковременно – обычно оно длится недолго. Например, при сбое контейнера вы теряете все данные на диске. Определенные тома позволяют управлять такой ситуацией с помощью постоянных томов.

</b></details>

<details>
<summary>Объясните типы эфемерных томов и постоянные тома в отношении подов.</summary><br><b>

Эфемерные типы томов имеют срок службы пода, в отличие от постоянных томов, которые существуют после окончания срока службы пода.

</b></details>

<details>
<summary>Укажите хотя бы один вариант использования для каждого из следующих типов томов:

* пустой каталог
* путь хоста</summary><br><b>

* EmptyDir: вам нужны временные данные, которые вы можете позволить себе потерять в случае удаления пода. Например, кратковременные данные, необходимые для одноразовых операций.
* HostPath: вам нужен доступ к путям на самом хосте (например, к данным из `/sys` или данным, сгенерированным в `/var/lib`)

</b></details>

<a id="network-questions"></a>
### Сеть

<details>
<summary>Правда или ложь? По умолчанию между двумя подами в двух разных пространствах имен нет связи.</summary><br><b>

Неверно. По умолчанию два пода в двух разных пространствах имен могут взаимодействовать друг с другом.

Попробуйте сами:

kubectl run test-prod -n prod --image ubuntu -- sleep 2000000000
kubectl run test-dev -n dev --image ubuntu -- sleep 2000000000

`kubectl describe pod test-prod -n prod`, чтобы получить IP-адрес пода test-prod.

Доступ к поду разработчика: `kubectl exec --stdin --tty test-dev -n dev -- /bin/bash`

И проверьте IP-адрес пода test-prod, который вы получили ранее. Вы увидите, что между двумя подами существует связь в двух отдельных пространствах имен.

</b></details>

<a id="network-policies"></a>
### Сетевые политики

<details>
<summary>Объясните сетевую политику</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies): «NetworkPolicies — это конструкция, ориентированная на приложение, которая позволяет вам указать, как поду разрешено взаимодействовать с различными сетевыми «объектами»…»

Проще говоря, сетевые политики определяют, как подам разрешено/запрещено взаимодействовать друг с другом и/или с другими конечными точками сети.

</b></details>

<details>
<summary>Каковы некоторые варианты использования сетевых политик?</summary><br><b>

- Безопасность: вы хотите запретить всем общаться с определенным подом по соображениям безопасности.
  - Управление сетевым трафиком: вы хотите запретить сетевой поток между двумя конкретными узлами.

</b></details>

<details>
<summary>Правда или ложь? Если к поду не применяются сетевые политики, то никакие подключения к нему или из него не допускаются.</summary><br><b>

Неверно. По умолчанию поды не изолированы.

</b></details>

<details>
<summary>В случае двух подов, если в источнике существует политика исходящего трафика, определяющая трафик, и политика входящего трафика в пункте назначения, разрешающая трафик, тогда трафик будет разрешен или запрещен?</summary><br><b>

Отклонен. Политика источника и назначения должна разрешать трафик, чтобы он был разрешен.

</b></details>

<details>
<summary>Где кластер Kubernetes хранит состояние кластера?</summary><br><b>

Состояние кластера (желаемое и наблюдаемое состояние ресурсов API) хранится в **etcd** — см. следующий раздел.

</b></details>

<a id="etcd"></a>
### etcd

<details>
<summary>Что такое etcd?</summary><br><b>

etcd — это распределенное хранилище значений ключей с открытым исходным кодом, используемое для хранения и управления важной информацией, необходимой для работы распределенных систем.

[Подробнее читайте здесь](https://www.redhat.com/en/topics/containers/what-is-etcd)

</b></details>

<details>
<summary>Правда или ложь? Etcd хранит текущий статус любого компонента Kubernetes.</summary><br><b>

Верно

</b></details>

<details>
<summary>Правда или ложь? Сервер API — единственный компонент, который напрямую взаимодействует с etcd.</summary><br><b>

Верно

</b></details>

<details>
<summary>Правда или ложь? данные приложения не хранятся в etcd</summary><br><b>

Верно

</b></details>

<details>
<summary>Почему для этого используют etcd, а не классическую SQL/NoSQL БД?</summary><br><b>

Когда в качестве хранилища данных был выбран etcd, было (и, конечно же, остается):

* Высокая доступность — вы можете развернуть несколько узлов.
* Полностью реплицированный — любой узел в кластере etcd является «основным» узлом и имеет полный доступ к данным.
* Согласованность: чтение возвращает последние данные.
* Защищено — поддерживает как TLS, так и SSL.
* Скорость — высокопроизводительное хранилище данных (10 000 операций записи в секунду!)

</b></details>

<a id="namespaces-questions"></a>
### Пространства имён

<details>
<summary>Что такое пространства имен?</summary><br><b>

Пространства имен позволяют разделить кластер на виртуальные кластеры, в которых вы можете группировать свои приложения разумным образом и полностью отделить их от других групп (так что вы можете, например, создать приложение с одинаковым именем в двух разных пространствах имен).

</b></details>

<details>
<summary>Зачем использовать пространства имен? В чем проблема с использованием одного пространства имен по умолчанию?</summary><br><b>

При использовании только пространства имен по умолчанию со временем становится сложно получить обзор всех приложений, которыми вы управляете в своем кластере. Пространства имен упрощают организацию приложений в группы, что имеет смысл, например, пространство имен всех приложений мониторинга, пространство имен для всех приложений безопасности и т. д.

Пространства имен также могут быть полезны для управления синими/зелеными средами, где каждое пространство имен может включать в себя разные версии приложения, а также совместно использовать ресурсы, находящиеся в других пространствах имен (таких пространствах имен, как ведение журнала, мониторинг и т. д.).

Другой вариант использования пространств имен — один кластер, несколько команд. Когда несколько команд используют один и тот же кластер, они могут в конечном итоге наступить друг другу на пятки. Например, если они в конечном итоге создают приложение с тем же именем, это означает, что одна из команд переопределила приложение другой команды, потому что в Kubernetes не может быть слишком много приложений с тем же именем (в том же пространстве имен).

</b></details>

<details>
<summary>Правда или ложь? При удалении пространства имен все ресурсы в этом пространстве имен не удаляются, а перемещаются в другое пространство имен по умолчанию.</summary><br><b>

Неверно. Когда пространство имен удаляется, ресурсы в этом пространстве имен также удаляются.

</b></details>

<details>
<summary>Какие специальные пространства имен используются по умолчанию при создании кластера Kubernetes?</summary><br><b>

* `default`
* `kube-system`
* `kube-public`
* `kube-node-lease`

</b></details>

<details>
<summary>Что вы можете найти в пространстве имен kube-system?</summary><br><b>

* Компоненты control plane (kube-apiserver, scheduler, controller-manager и др.)
* Системные DaemonSet и служебные поды (CNI, CoreDNS, kube-proxy и т.д.)

</b></details>

<details>
<summary>Хотя пространства имен предоставляют пространство для ресурсов, они не изолируют их.</summary><br><b>

Верно. Попробуйте создать, например, два пода в двух отдельных пространствах имен, и вы увидите, что между ними существует связь.

</b></details>

<a id="namespaces-commands"></a>
#### Пространства имён — команды

<details>
<summary>Как составить список всех пространств имен?</summary><br><b>

`kubectl get namespaces` ИЛИ `kubectl get ns`

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
<summary>Создайте под под названием «kartos» в пространстве имен dev. Под должен использовать образ «redis».</summary><br><b>

Если namespace ещё не существует: `kubectl create namespace dev`

`kubectl run kratos --image=redis -n dev`

</b></details>

<details>
<summary>Вы ищете под с именем «Atreus». Как узнать, в каком namespace он работает?</summary><br><b>

`kubectl get pods -A | grep Atreus`

</b></details>

<details>
<summary>Что содержит kube-public?</summary><br><b>

* Карта конфигурации, содержащая информацию о кластере.
* Публично доступные данные

</b></details>

<details>
<summary>Как получить имя текущего пространства имен?</summary><br><b>

`kubectl config view --minify -o jsonpath='{.contexts[0].context.namespace}'`

</b></details>

<details>
<summary>Что содержит kube-node-lease?</summary><br><b>

Он содержит информацию о пульсе узлов. Каждый узел получает объект, который содержит информацию о его доступности.

</b></details>

<details>
<summary>Правда или ложь? С помощью пространств имен вы можете ограничить ресурсы, потребляемые пользователями/командами.</summary><br><b>

Верно. С помощью пространств имен вы можете ограничить использование ЦП, ОЗУ и хранилища.

</b></details>

<details>
<summary>Как переключиться на другое пространство имен? Другими словами, как изменить активное пространство имен?</summary><br><b>

`kubectl config set-context --current --namespace=some-namespace` и проверьте: `kubectl config view --minify | grep namespace`

ИЛИ

`kubens некоторое пространство имен`

</b></details>

<a id="resource-quota"></a>
#### Ресурсная квота

<details>
<summary>Что такое квота ресурсов?</summary><br><b>

Квота ресурсов обеспечивает ограничения, которые ограничивают совокупное потребление ресурсов для каждого пространства имен. Он может ограничивать количество объектов, которые могут быть созданы в пространстве имен, по типу, а также общий объем вычислительных ресурсов, которые могут потребляться ресурсами в этом пространстве имен.

</b></details>

<details>
<summary>Как создать квоту ресурсов?</summary><br><b>

kubectl create quota some-quota --hard=cpu=2,pods=2

</b></details>

<details>
<summary>Какие ресурсы доступны из разных пространств имен?</summary><br><b>

Услуги.

</b></details>

<details>
<summary>На какую службу и в каком пространстве имен ссылается следующий файл?

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
data:
  some_url: samurai.jack
```

</summary><br><b>

Это ссылка на сервис «самурай» в пространстве имен «джек».

</b></details>

<details>
<summary>Какие компоненты нельзя создать в пространстве имен?</summary><br><b>

Том и узел.

</b></details>

<details>
<summary>Как составить список всех компонентов, привязанных к пространству имен?</summary><br><b>

`kubectl api-resources --namespaced=true`

</b></details>

<details>
<summary>Как создать компоненты в пространстве имен?</summary><br><b>

Один из способов — указать --namespace следующим образом: `kubectl apply -f my_comComponent.yaml --namespace=some-namespace`
Другой способ — указать его в самом YAML:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: some-configmap
  namespace: some-namespace

и вы можете проверить это с помощью: `kubectl get configmap -n some-namespace`

</b></details>

<details>
<summary>Как выполнить команду «ls» в существующем поде?</summary><br><b>

kubectl exec some-pod -it -- ls

</b></details>

<details>
<summary>Как создать службу, предоставляющую развертывание?</summary><br><b>

kubectl expose deployment some-deployment --port=80 --target-port=8080

</b></details>

<details>
<summary>Как создать под и сервис одной командой?</summary><br><b>

kubectl run nginx --image=nginx --restart=Never --port 80 --expose

</b></details>

<details>
<summary>Подробно опишите, что делает следующая команда: <code>kubectl create Deployment kubernetes-httpd --image=httpd</code></summary><br><b>

Создаёт объект **Deployment** `kubernetes-httpd` с одной репликой. Контроллер Deployment создаёт **ReplicaSet**, тот — **Pod** с контейнером на образе `httpd`. Дальше Deployment поддерживает желаемое число реплик и может выполнять rolling update.

</b></details>

<details>
<summary>Зачем создавать Deployment, если поды можно запускать с помощью ReplicaSet?</summary><br><b>

Deployment добавляет поверх ReplicaSet: **rolling update** и **rollback** (`kubectl rollout undo`), историю ревизий, паузу/возобновление выката, стратегии обновления (`RollingUpdate` / `Recreate`). ReplicaSet только держит нужное число одинаковых подов.

</b></details>

<details>
<summary>Как получить список ресурсов, не привязанных к определенному пространству имен?</summary><br><b>

kubectl api-resources --namespaced=false

</b></details>

<details>
<summary>Как удалить все поды, статус которых не «Работает»?</summary><br><b>

kubectl delete pods --field-selector=status.phase!=Running

</b></details>

<details>
<summary>Как отобразить использование ресурсов подов?</summary><br><b>

`kubectl top pod`

</b></details>

<details>
<summary>Возможно, это общий вопрос, но вы подозреваете, что у одного из подов возникла проблема, и вы не знаете, в чем именно. Что вы делаете?</summary><br><b>

Начните с проверки состояния подов. мы можем использовать команду `kubectl get pods` (--all-namespaces для подов в системном пространстве имен)<br>

Если статус Failed/Error — `kubectl describe pod <имя>` и `kubectl logs <имя>`. Для потока логов с нескольких подов — **stern**.<br>

В случае, если мы обнаружим, что возникла временная проблема с подом или системой, мы можем попробовать перезапустить под с помощью следующего `kubectl scale deployment [name] --replicas=0`<br>

Установка реплик на 0 приведет к остановке процесса. Теперь запустите его с помощью `kubectl scale deployment [name] --replicas=1`

</b></details>

<details>
<summary>Что происходит, если поды используют слишком много памяти? (больше своего предела)</summary><br><b>

Они становятся кандидатами на увольнение.

</b></details>

<details>
<summary>Опишите, как работает откат</summary><br><b>

У Deployment хранится история ReplicaSet (ревизии). При `kubectl rollout undo deployment/<NAME>` (или откат к конкретной ревизии) контроллер переключает шаблон пода на предыдущую версию и выполняет rolling update к старой конфигурации. Статус: `kubectl rollout status` / `kubectl rollout history`.

</b></details>

<details>
<summary>Правда или ложь? Память — это сжимаемый ресурс, а это означает, что когда контейнер достигает предела памяти, он продолжает работать.</summary><br><b>

Неверно. ЦП — это сжимаемый ресурс, а память — несжимаемый ресурс: как только контейнер достигнет предела памяти, он будет завершен.

</b></details>

<a id="operators-questions"></a>
### Операторы

<details>
<summary>Что такое оператор?</summary><br><b>

Объяснено [здесь](https://kubernetes.io/docs/concepts/extend-kubernetes/operator)

«Операторы — это программные расширения Kubernetes, которые используют специальные ресурсы для управления приложениями и их компонентами. Операторы следуют принципам Kubernetes, в частности, циклу управления».

Проще говоря, вы можете думать об операторе как о специальном цикле управления в Kubernetes.

</b></details>

<details>
<summary>Зачем нам нужны операторы?</summary><br><b>

Процесс управления приложениями с сохранением состояния в Kubernetes не так прост, как управление приложениями без сохранения состояния, где достижение желаемого статуса и обновления обрабатываются одинаково для каждой реплики. В приложениях с отслеживанием состояния обновление каждой реплики может потребовать разной обработки из-за особенностей приложения с отслеживанием состояния: каждая реплика может находиться в различном состоянии. В результате нам часто нужен человек-оператор для управления приложениями с отслеживанием состояния. Предполагается, что оператор Kubernetes поможет в этом.

Это также помогает автоматизировать стандартный процесс в нескольких кластерах Kubernetes.

</b></details>

<details>
<summary>Из каких компонентов состоит Оператор?</summary><br><b>

1. CRD (настраиваемое определение ресурса). Вы знакомы с ресурсами Kubernetes, такими как развертывание, под, служба и т. д. CRD также является ресурсом, но тот, который определяете вы или разработчик, оператор.
2. Контроллер — пользовательский контур управления, работающий на основе CRD.

</b></details>

<details>
<summary>Объясните CRD</summary><br><b>

CRD (Custom Resource Definition) — способ расширить API Kubernetes собственными типами ресурсов (например, `CronTab`, `Backup`). После регистрации CRD можно создавать объекты этого типа через `kubectl` и обрабатывать их контроллером/оператором. Схема полей задаётся в OpenAPI v3 внутри манифеста CRD.

</b></details>

<details>
<summary>Как работает Оператор?</summary><br><b>

Он использует цикл управления, используемый в Kubernetes в целом. Он отслеживает изменения в состоянии приложения. Разница в том, что здесь используется собственный цикл управления.

Кроме того, он также использует CRD (определения пользовательских ресурсов), поэтому по сути он расширяет API Kubernetes.

</b></details>

<details>
<summary>Правда или ложь? Оператор Kubernetes, используемый для приложений с отслеживанием состояния</summary><br><b>

Верно

</b></details>

<details>
<summary>Объясните, что такое OLM (Operator Lifecycle Manager) и для чего он используется.</summary><br><b>

**OLM** — компонент экосистемы операторов (часто OpenShift/Operator Framework): устанавливает, обновляет и удаляет **Operators** из каталога, управляет CRD и подписками. Упрощает жизненный цикл сложных приложений в кластере без ручной сборки манифестов.

</b></details>

<details>
<summary>Что такое операторская структура?</summary><br><b>

набор инструментов с открытым исходным кодом, используемый для автоматизированного и эффективного управления собственными приложениями k8s, называемыми операторами.

</b></details>

<details>
<summary>Из каких компонентов состоит операторская платформа?</summary><br><b>

1. SDK оператора - позволяет разработчикам создавать операторов.
2. Operation Lifecycle Manager — помогает устанавливать, обновлять и в целом управлять жизненным циклом всех операторов.
3. Измерение операторов. Позволяет операторам, предоставляющим специализированные услуги, создавать отчеты об использовании.
4.

</b></details>

<details>
<summary>Подробно опишите, что такое Operation Lifecycle Manager.</summary><br><b>

Это часть оператора Framework, используемая для управления жизненным циклом операторов. По сути, он расширяет Kubernetes, позволяя пользователю использовать декларативный способ управления операторами (установка, обновление и т. д.).

</b></details>

<details>
<summary>Что включает в себя пространство имен openshift-operator-lifecycle-manager?</summary><br><b>

Он включает в себя:

  * оператор каталога — разрешение и установка ClusterServiceVersions указанного ими ресурса.
  * olm-operator — развертывает приложения, определенные ресурсом ClusterServiceVersion.

</b></details>

<details>
<summary>Что такое кубконфиг? Для чего вы его используете?</summary><br><b>

Файл kubeconfig — это файл, используемый для настройки доступа к Kubernetes при использовании вместе с инструментом командной строки kubectl (или другими клиентами).
Используйте файлы kubeconfig для организации информации о кластерах, пользователях, пространствах имен и механизмах аутентификации.

</b></details>

<details>
<summary>Вы бы использовали Helm, Go или что-то еще для создания оператора?</summary><br><b>

Зависит от масштаба и зрелости Оператора. Если речь идет в основном об установке и обновлении, Helm может быть достаточно. Если вы хотите использовать управление жизненным циклом, аналитику и автопилот, вам, вероятно, стоит использовать Go.

</b></details>

<details>
<summary>Есть ли какие-либо инструменты и проекты, которые вы используете для создания Операторов?</summary><br><b>

Это больше основано на личном опыте и вкусе...

* Структура оператора
* Кубебилдер
* Время выполнения контроллера
...

</b></details>

<a id="secrets-questions"></a>
### Секреты

<details>
<summary>Объясните секреты Kubernetes</summary><br><b>

Секреты позволяют хранить конфиденциальную информацию (пароли, SSH-ключи и т. д.) и управлять ею.

</b></details>

<details>
<summary>Как создать секрет из ключа и значения?</summary><br><b>

`kubectl create secret generic some-secret --from-literal=password='donttellmypassword'`

</b></details>

<details>
<summary>Как создать секрет из файла?</summary><br><b>

`kubectl create secret generic some-secret --from-file=/some/file.txt`

</b></details>

<details>
<summary>Что означает <code>type: Opaque</code> в секретном файле? Какие еще виды существуют?</summary><br><b>

Непрозрачный — это тип по умолчанию, используемый для пар ключ-значение.

</b></details>

<details>
<summary>Правда или ложь? хранение данных в секретном компоненте делает их автоматически защищенными</summary><br><b>

Неверно. Некоторые известные механизмы безопасности, такие как «шифрование», по умолчанию не включены.

</b></details>

<details>
<summary>В чем проблема со следующим секретным файлом:

```
apiVersion: v1
kind: Secret
metadata:
  name: some-secret
type: Opaque
data:
  password: mySecretPassword
```

</summary><br><b>

Пароль не зашифрован.
Вы должны запустить что-то вроде этого: `echo -n 'mySecretPassword' | base64` и вставьте результат в файл вместо использования обычного текста.

</b></details>

<details>
<summary>Что означает следующее в файле конфигурации развертывания?

```
spec:
  containers:
    - name: USER_PASSWORD
      valueFrom:
        secretKeyRef:
          name: some-secret
          key: password
```

</summary><br><b>

Переменная окружения `USER_PASSWORD` возьмёт значение ключа `password` из Secret `some-secret`.
Другими словами, вы ссылаетесь на значение из секрета Kubernetes.

</b></details>

<details>
<summary>Как передать секреты в Git и вообще как использовать зашифрованные секреты?</summary><br><b>

Один из возможных процессов может быть следующим:

1. Вы создаете секрет Kubernetes (но не передаете его)
2. Вы шифруете его с помощью стороннего проекта (например, kubeseal).
3. Вы применяете запечатанный/зашифрованный секрет.
4. Вы передаете запечатанный секрет в Git.
5. Вы развертываете приложение, которому требуется секрет, и его можно автоматически расшифровать, например, с помощью контроллера секретов Bitnami Sealed.

</b></details>

<a id="volume-mounts"></a>
### Тома

<details>
<summary>Правда или ложь? Kubernetes обеспечивает постоянство данных «из коробки», поэтому при перезапуске пода данные сохраняются.</summary><br><b>

Неверно

</b></details>

<details>
<summary>Объясните «постоянные тома». Зачем нам это нужно?</summary><br><b>

Постоянные тома позволяют нам сохранять данные, поэтому они предоставляют хранилище, не зависящее от жизненного цикла пода.

</b></details>

<details>
<summary>Правда или ложь? Постоянный том должен быть доступен для всех узлов, поскольку под может перезапуститься на любом из них.</summary><br><b>

Верно

</b></details>

<details>
<summary>Какие типы постоянных томов существуют?</summary><br><b>

* НФС
* iSCSI
* CephFS
* ...

</b></details>

<details>
<summary>Что такое PersistentVolumeClaim?</summary><br><b>

**PVC** — запрос пода на постоянное хранилище (размер, режим доступа, StorageClass). Кластер связывает PVC с **PersistentVolume** (PV) — существующим или созданным динамически. Под монтирует том через `volumeMounts` в spec.

</b></details>

<details>
<summary>Объяснение снимков тома</summary><br><b>

Снимки тома позволяют создать копию тома в определенный момент времени.

</b></details>

<details>
<summary>Правда или ложь? Kubernetes управляет постоянством данных</summary><br><b>

Неверно

</b></details>

<details>
<summary>Объяснение классов хранения</summary><br><b>

**StorageClass** описывает «тип» диска и провайдер (CSI, cloud disk и т.д.). В PVC указывают `storageClassName` — тогда том создаётся **динамически** по шаблону класса (reclaim policy, параметры IOPS и др.).

</b></details>

<details>
<summary>Объясните «динамическую подготовку» и «статическую подготовку».</summary><br><b>

Основное различие зависит от момента, когда вы хотите настроить хранилище. Например, если вам нужно предварительно заполнить данные в томе, вы выбираете статическую подготовку. Принимая во внимание, что если вам нужно создавать тома по требованию, вы выбираете динамическое предоставление.

</b></details>

<details>
<summary>Объясните режимы доступа</summary><br><b>

Режимы доступа к томам (PersistentVolume):

* **ReadWriteOnce (RWO)** — чтение/запись с одного узла.
* **ReadOnlyMany (ROX)** — только чтение, несколько узлов.
* **ReadWriteMany (RWX)** — чтение/запись с нескольких узлов (NFS и аналоги).

Выбор зависит от того, сколько подов и на скольких узлах монтируют том.

</b></details>

<details>
<summary>Что такое клонирование тома CSI?</summary><br><b>

Механизм **CSI Volume Cloning**: новый PVC создаётся как копия данных существующего PVC (указание `dataSource` на исходный claim). Полезно для копий БД, тестовых сред без полного бэкапа/restore через снимок.

</b></details>

<details>
<summary>Объясните «эфемерные тома»</summary><br><b>

Тома, **привязанные к жизненному циклу пода**: создаются вместе с подом и удаляются при его удалении (если не общий том с другой политикой). Данные не переживают пересоздание пода на другом узле — в отличие от PV/PVC.

</b></details>

<details>
<summary>Какие типы эфемерных томов поддерживает Kubernetes?</summary><br><b>

Например: **emptyDir**, **configMap**, **secret**, **downwardAPI**, **projected**; также ephemeral volumes через **CSI** и **generic ephemeral volumes** (в новых версиях). Часто используют `emptyDir` для кэша и временных файлов.

</b></details>

<details>
<summary>Что такое политика возврата?</summary><br><b>

**Reclaim policy** у PersistentVolume определяет судьбу тома после удаления PVC: оставить данные (**Retain**), удалить (**Delete**) или переиспользовать (**Recycle** — устарело). Задаётся в PV или в StorageClass.

</b></details>

<details>
<summary>Какие существуют политики возврата?</summary><br><b>

* Сохранить
* Переработка
* Удалить

</b></details>

<a id="rbac-questions"></a>
### Контроль доступа

<details>
<summary>Что такое РБАК?</summary><br><b>

RBAC в Kubernetes — это механизм, который позволяет вам настраивать детальные и конкретные наборы разрешений, определяющие, как данный пользователь или группа пользователей может взаимодействовать с любым объектом Kubernetes в кластере или в определенном пространстве имен кластера.

</b></details>

<details>
<summary>Объясните объекты <code>Role</code> и <code>RoleBinding</code>.</summary><br><b>

**Role** — набор правил RBAC в **namespace** (какие verb на какие resources). **RoleBinding** связывает Role (или ClusterRole через RoleBinding) с субъектом (User, Group, ServiceAccount) в том же namespace. Вместе задают «кто что может» в пространстве имён.

</b></details>

<details>
<summary>В чем разница между объектами <code>Role</code> и <code>ClusterRole</code>?</summary><br><b>

Разница между ними заключается в том, что роль используется на уровне пространства имен, а ClusterRole — для всего кластера.

</b></details>

<details>
<summary>Объясните, что такое «служебные учетные записи» и в каком сценарии будет использоваться их создание/использование.</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account): «Служебная учетная запись обеспечивает идентификацию процессов, которые выполняются в поде».

Пример того, когда его использовать:
Вы определяете конвейер, который должен создать и отправить образ. Чтобы иметь достаточные разрешения для создания принудительного образа, этому конвейеру потребуется учетная запись службы с достаточными разрешениями.

</b></details>

<details>
<summary>Что произойдет, если вы создадите под и НЕ укажете учетную запись службы?</summary><br><b>

Модулю автоматически назначается учетная запись службы по умолчанию (в пространстве имен, где работает под).

</b></details>

<details>
<summary>Объясните, чем учетные записи служб отличаются от учетных записей пользователей.</summary><br><b>

- Учетные записи пользователей являются глобальными, а учетные записи служб уникальны для каждого пространства имен.
  - Учетные записи пользователей предназначены для людей или клиентских процессов, а учетные записи служб предназначены для процессов, которые выполняются в подах.

</b></details>

<details>
<summary>Как составить список сервисных аккаунтов?</summary><br><b>

`kubectl get serviceaccounts`

</b></details>

<details>
<summary>Объясните «Контекст безопасности»</summary><br><b>

[kubernetes.io](https://kubernetes.io/docs/tasks/configure-pod-container/security-context): «Контекст безопасности определяет параметры контроля привилегий и доступа для пода или контейнера».

</b></details>

<a id="templates-questions"></a>
### Шаблоны


<a id="cronjob-questions"></a>
### CronJob

<details>
<summary>Объясните, что такое CronJob и для чего он используется.</summary><br><b>

CronJob создает задания по повторяющемуся расписанию. Один объект CronJob похож на одну строку файла crontab (таблицы cron). Он периодически запускает задание по заданному расписанию, написанному в формате Cron.

</b></details>

<details>
<summary>Какая возможная проблема может возникнуть при использовании следующей спецификации и как ее исправить?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: some-cron-job
spec:
  schedule: '*/1 * * * *'
  startDeadlineSeconds: 10
  concurrencyPolicy: Allow
```

</summary><br><b>

Если задание CronJob завершается с ошибкой, следующий запуск не заменит предыдущий при `concurrencyPolicy: Allow`. Он будет продолжать создавать новые задания, и в конечном итоге система будет заполнена неудачными заданиями cron.
Чтобы избежать накопления failed jobs, задайте `concurrencyPolicy: Replace` или `Forbid`.

</b></details>

<details>
<summary>Какая проблема может возникнуть при использовании следующего CronJob и как ее исправить?

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: "some-cron-job"
spec:
  schedule: '*/1 * * * *'
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
      concurrencyPolicy: Forbid
      successfulJobsHistoryLimit: 1
      failedJobsHistoryLimit: 1
```

</summary><br><b>

Поля `concurrencyPolicy`, `successfulJobsHistoryLimit` и `failedJobsHistoryLimit` должны быть на уровне `spec` CronJob (рядом с `schedule`), а не внутри `jobTemplate.spec.template.spec`. Иначе ограничения не применяются — возможны OOM и перегрузка API server.<br>
Исправление:

```
spec:
  schedule: '*/1 * * * *'
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 1
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
```

</b></details>

<a id="kubernetes-misc"></a>
### Разное

<details>
<summary>Объясните императивное управление и декларативное управление.</summary><br><b>

* **Императивное** — команды «сделай сейчас»: `kubectl run`, `create`, `delete`, `scale` без сохранённого манифеста.
* **Декларативное** — описание желаемого состояния в YAML и `kubectl apply`: API server приводит кластер к этому состоянию. Предпочтительно для GitOps и повторяемости.

</b></details>

<details>
<summary>Объясните, что означает обнаружение службы Kubernetes.</summary><br><b>

Поды находят друг друга через **Service**: стабильный DNS (`<service>.<namespace>.svc.cluster.local`) и виртуальный IP. Endpoints (или EndpointSlice) связывают Service с IP подов по селектору. Kube-proxy (или dataplane CNI) направляет трафик на backend-поды.

</b></details>

<details>
<summary>У вас есть один кластер Kubernetes и несколько команд, которые хотели бы его использовать. Вы хотите ограничить ресурсы, потребляемые каждой командой в кластере. Какую концепцию Kubernetes вы бы для этого использовали?</summary><br><b>

Пространства имен позволят ограничить ресурсы, а также гарантировать отсутствие конфликтов между командами при работе в кластере (например, при создании приложения с таким же именем).

</b></details>

<details>
<summary>Что делает Kube Proxy?</summary><br><b>

Kube Proxy — это сетевой прокси, который работает на каждом узле вашего кластера и реализует часть концепции Kubernetes Service.

</b></details>

<details>
<summary>Для чего и как используются «квоты ресурсов»?</summary><br><b>

**ResourceQuota** в namespace ограничивает суммарное потребление (CPU, memory, число подов, PVC, LoadBalancer и т.д.). Создаётся объектом `ResourceQuota`; команды/поды в namespace не превысят квоту. Часто сочетают с **LimitRange** для дефолтных limits на под.

</b></details>

<details>
<summary>Объясните ConfigMap</summary><br><b>

Отдельная конфигурация от подов.
Это хорошо для случаев, когда вам может потребоваться изменить конфигурацию в какой-то момент, но вы не хотите перезапускать приложение или перестраивать образ, поэтому вы создаете ConfigMap и подключаете его к поду, но внешне к поду.

В целом это хорошо для:
* Совместное использование одной и той же конфигурации между разными подами.
* Хранение внешней конфигурации пода

</b></details>

<details>
<summary>Как использовать ConfigMaps?</summary><br><b>

1. Создайте его (из ключа и значения, файла или файла env).
2. Прикрепите его. Смонтировать конфигурационную карту как том

</b></details>

<details>
<summary>Правда или ложь? Конфиденциальные данные, такие как учетные данные, следует хранить в ConfigMap.</summary><br><b>

Неверно. Используйте секрет.

</b></details>

<details>
<summary>Объясните «Горизонтальное автомасштабирование подов»</summary><br><b>

В Kubernetes HorizontalPodAutoscaler автоматически обновляет ресурс рабочей нагрузки с целью автоматического масштабирования рабочей нагрузки в соответствии с потребностями.

</b></details>

<details>
<summary>Когда вы удаляете под, он удаляется мгновенно? (через мгновение после выполнения команды)</summary><br><b>

Нет. Сначала под переходит в **Terminating**: kubelet отправляет **SIGTERM** контейнерам и ждёт **grace period** (`terminationGracePeriodSeconds`, по умолчанию 30 с). После истечения — **SIGKILL**. Удаление «сразу» возможно только при `grace-period=0 --force`.

</b></details>

<details>
<summary>Что значит быть облачным?</summary><br><b>

Термин «нативный для облака» относится к концепции создания и запуска приложений, позволяющих использовать преимущества распределенных вычислений, предлагаемых моделью доставки в облаке.

</b></details>

<details>
<summary>Объясните подход к инфраструктуре, основанный на домашних животных и скоте, применительно к Kubernetes.</summary><br><b>

**Pets** — уникальные, долгоживущие серверы с ручным уходом; **cattle** — взаимозаменяемые узлы/поды, которые можно удалить и пересоздать. В K8s поды и ноды — «скот»: при сбое их заменяют, а не «лечат» вручную; state хранят в PVC/внешних сервисах.

</b></details>

<details>
<summary>Опишите, как вы запускаете контейнерное веб-приложение в K8s, которое должно быть доступно по общедоступному URL-адресу.</summary><br><b>

1. **Deployment** (или Pod) с образом приложения, probes, requests/limits.<br>
2. **Service** (NodePort или LoadBalancer) для доступа к подам.<br>
3. При необходимости **Ingress** + TLS для доменного имени и маршрутизации HTTP(S).<br>
4. В облаке — часто LoadBalancer/Ingress controller автоматически выдаёт внешний IP/DNS.

</b></details>

<details>
<summary>Как бы вы устраняли неполадки в своем кластере, если некоторые приложения больше не доступны?</summary><br><b>

`kubectl get pods,svc,ingress -A` → проблемные namespace; `kubectl describe pod/svc` (Events); `kubectl logs` / `kubectl logs --previous`; проверить **Endpoints** у Service; сеть (NetworkPolicy, DNS); узлы `kubectl get nodes`; недавние деплои `kubectl rollout history`. При необходимости — метрики/алерты и события control plane.

</b></details>

<details>
<summary>Опишите, какие CustomResourceDefinitions существуют в мире Kubernetes? Для чего их можно использовать?</summary><br><b>

**CRD** расширяют API кластера своими типами ресурсов (например `Certificate`, `Prometheus`, `Application` в Argo CD). Их обрабатывает **контроллер/оператор**. Позволяют описывать доменную логику (GitOps, сертификаты, БД) декларативно, как встроенные объекты K8s.

</b></details>

<details>
<summary>Как работает планирование в Kubernetes?</summary><br><b>

Компонент kube-scheduler плоскости управления задает следующие вопросы:
1. Что запланировать? Он пытается понять спецификации определения пода.
2. Какой узел запланировать? Он пытается определить лучший узел с доступными ресурсами для запуска пода.
3. Привязывает под к заданному узлу.

Посмотреть больше [здесь](https://www.youtube.com/watch?v=rDCWxkvPlAw)

</b></details>

<details>
<summary>Как используются метки и селекторы?</summary><br><b>

**Labels** (ключ=значение) вешают на объекты для группировки и фильтрации. **Selectors** в Deployment, Service, ReplicaSet указывают, какие поды/объекты «принадлежат» ресурсу (`matchLabels` / `matchExpressions`). Пример: Service с `selector: app=web` направляет трафик на поды с меткой `app=web`.

</b></details>

<details>
<summary>Какие классы QoS существуют?</summary><br><b>

* Гарантировано
* Взрывной
* БестЭффорт

</b></details>

<details>
<summary>Объясните этикетки. Что это такое и зачем их использовать?</summary><br><b>

Метки Kubernetes — это пары «ключ-значение», которые могут связывать идентифицирующие метаданные с объектами Kubernetes.

</b></details>

<details>
<summary>Объяснение селекторов</summary><br><b>

Селектор — правило отбора объектов по меткам: **equality** (`app=web`) или **set-based** (`env in (prod,staging)`). Используются в Service, Deployment, NetworkPolicy и др., чтобы связать контроллер или сеть с нужным набором подов.

</b></details>

<details>
<summary>Что такое kubeconfig?</summary><br><b>

Файл конфигурации (по умолчанию `~/.kube/config`) с **clusters**, **users** (credentials), **contexts** (связка cluster+user+namespace). `kubectl` читает его для адреса API server и аутентификации; переключение кластера — `kubectl config use-context`.

</b></details>

<a id="gatekeeper"></a>
### Gatekeeper

<details>
<summary>Что такое Гейткипер?</summary><br><b>

[Документация Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs): «Gatekeeper — это проверяющий (изменяющий TBA) веб-перехватчик, который обеспечивает соблюдение политик на основе CRD, выполняемых агентом открытой политики»

</b></details>

<details>
<summary>Объясните, как работает Gatekeeper</summary><br><b>

При каждом запросе, отправленном в кластер Kubernetes, Gatekeeper отправляет политики и ресурсы OPA (агенту открытой политики), чтобы проверить, не нарушает ли он какую-либо политику. Если это произойдет, гейткипер вернет сообщение об ошибке политики обратно. Если это не нарушает какую-либо политику, запрос достигнет кластера.

</b></details>

<a id="policy-testing"></a>
### Тестирование политики

<details>
<summary>Что такое Conftest?</summary><br><b>

Conftest позволяет писать тесты для структурированных файлов. Вы можете думать об этом как о библиотеке тестов для ресурсов Kubernetes.<br>
Он в основном используется в средах тестирования, таких как конвейеры CI или локальные перехватчики.

</b></details>

<details>
<summary>Что такое Datree? Чем он отличается от Conftest?</summary><br><b>

Как и Conftest, он используется для тестирования и обеспечения соблюдения политик. Разница в том, что он поставляется со встроенными политиками.

</b></details>

<a id="helm-questions"></a>
### Helm

<details>
<summary>Что такое Хелм?</summary><br><b>

Менеджер пакетов для Kubernetes. По сути, это возможность упаковывать файлы YAML, распространять их среди других пользователей и применять в кластерах.

Как концепция, она довольно распространена и ее можно найти на многих платформах и сервисах. Подумайте, например, о менеджерах пакетов в операционных системах. Если вы используете Fedora/RHEL, это будет dnf. Если вы используете Ubuntu, apt. Если вы не используете Linux, то следует задать другой вопрос, а вот почему? но это другая тема :)

</b></details>

<details>
<summary>Зачем нам нужен Хелм? Каков будет вариант его использования?</summary><br><b>

Иногда, когда вы хотите развернуть определенное приложение в своем кластере, вам необходимо создать несколько файлов/компонентов YAML, таких как Secret, Service, ConfigMap и т. д. Это может быть утомительной задачей. Поэтому было бы разумно упростить этот процесс, внедрив что-то, что позволит нам делиться этим набором YAML-файлов каждый раз, когда мы хотим добавить приложение в наш кластер. Это нечто называется Хелм.

Распространенный сценарий — наличие нескольких кластеров Kubernetes (prod, dev, staging). Вместо индивидуального применения разных YAML-файлов в каждом кластере имеет смысл создать одну диаграмму и установить ее в каждом кластере.

Другой сценарий: вы хотите поделиться с сообществом тем, что вы создали. Чтобы люди и компании могли легко развернуть ваше приложение в своем кластере.

</b></details>

<details>
<summary>Объясните «Хелм-диаграммы»</summary><br><b>

Helm Charts — это набор файлов YAML. Пакет, который вы можете использовать из репозиториев или создать свой собственный и опубликовать его в репозиториях.

</b></details>

<details>
<summary>Говорят, что Helm также является шаблонизатором. Что это значит?</summary><br><b>

Это полезно в сценариях, когда у вас есть несколько приложений, и все они похожи, поэтому в их файлах конфигурации есть незначительные различия, а большинство значений совпадают. С помощью Helm вы можете определить общий план для всех, а значения, которые не являются фиксированными и изменяются, могут быть заполнителями. Это называется файлом шаблона и выглядит примерно так:

```
apiVersion: v1
kind: Pod
metadata:
  name: {[ .Values.name ]}
spec:
  containers:
  - name: {{ .Values.container.name }}
  image: {{ .Values.container.image }}
  port: {{ .Values.container.port }}


Сами значения будут в отдельном файле:


name: some-app
container:
  name: some-app-container
  image: some-app-image
  port: 1991
```

</b></details>

<details>
<summary>Каковы некоторые варианты использования файла шаблона Helm?</summary><br><b>

* Развертывание одного и того же приложения в нескольких разных средах.
* CI/CD

</b></details>

<details>
<summary>Объясните структуру каталогов диаграммы Helm</summary><br><b>

someChart/ -> имя диаграммы
  Chart.yaml -> метаинформация на графике
  values.yaml -> значения для файлов шаблонов
  диаграммы/ -> зависимости диаграммы
  шаблоны/ -> файлы шаблонов :)

</b></details>

<details>
<summary>Как Helm поддерживает управление выпусками?</summary><br><b>

Helm позволяет обновлять, удалять и выполнять откат к предыдущим версиям диаграмм. В версии 2 Helm это было с так называемым «Тиллером». В версии 3 он был удален из соображений безопасности.

</b></details>

<a id="helm-commands"></a>
#### Команды

<details>
<summary>Как вы ищете диаграммы?</summary><br><b>

`helm search hub [some_keyword]`

</b></details>

<details>
<summary>Можно ли переопределить значения в файлеvalues.yaml при установке диаграммы?</summary><br><b>

Да. Вы можете передать другой файл значений:
`helm install --values=override-values.yaml [CHART_NAME]`

Или прямо в командной строке: `helm install --set some_key=some_value`

</b></details>

<details>
<summary>Как вы составляете список развернутых выпусков?</summary><br><b>

`helm ls` или `helm list`

</b></details>

<details>
<summary>Как выполнить откат?</summary><br><b>

`helm rollback RELEASE_NAME REVISION_ID`

</b></details>

<details>
<summary>Как просмотреть историю изменений для определенного выпуска?</summary><br><b>

`helm history RELEASE_NAME`

</b></details>

<details>
<summary>Как обновить релиз?</summary><br><b>

`helm upgrade RELEASE_NAME CHART_NAME`

</b></details>

<a id="pod-security"></a>
### Безопасность

<details>
<summary>Каким передовым практикам безопасности вы следуете в отношении кластера Kubernetes?</summary><br><b>

* Безопасная связь между сервисами (один из способов — использовать Istio для обеспечения взаимного TLS).
  * Изолируйте разные ресурсы в отдельные пространства имен на основе некоторых логических групп.
  * Используйте поддерживаемый **CRI** (containerd, CRI-O). Docker Engine как runtime в Kubernetes устарел; для CLI на хосте часто используют `crictl` или `nerdctl`, для локальной разработки — `podman`/`docker`.
  * Правильно тестируйте изменения в кластере (например, рассмотрите возможность использования Datree для предотвращения неправильных конфигураций Kubernetes).
  * Ограничьте, кто и что может делать (например, используя привратник OPA) в кластере.
  * Используйте NetworkPolicy для применения сетевой безопасности.
  * Рассмотрите возможность использования инструментов (например, Falco) для мониторинга угроз.

</b></details>

<a id="troubleshooting-scenarios"></a>
### Сценарии устранения неполадок

<details>
<summary>Запустив <code>kubectl get pods</code>, вы увидите поды в статусе `Pending`. Что бы вы сделали?</summary><br><b>

Один из возможных путей — запустить `kubectl describe pod <имя пода>`, чтобы получить более подробную информацию.<br>
Вы можете увидеть одно из следующего:
  * Кластер заполнен. В этом случае расширьте кластер.
  * Ограничения ResourceQuota соблюдены. В этом случае вы можете изменить их.
  * Проверьте, ожидает ли монтирование PersistentVolumeClaim.

Если ничего из вышеперечисленного не помогло, выполните `kubectl get pods -o wide` и проверьте, назначен ли под узлу (`NODE`). Если колонка `NODE` пуста — возможна проблема планировщика или ограничений (taints, resources, affinity).

</b></details>

<details>
<summary>Пользователи не могут получить доступ к приложению, работающему в поде в Kubernetes. В чем может быть проблема и как проверить?</summary><br><b>

Один из возможных путей — начать с проверки статуса пода:

1. **Pending** — `kubectl describe pod <POD>` (события, taints, ресурсы, PVC).
2. **Running, но нет доступа** — проверьте Service/Endpoints, `kubectl port-forward`, NetworkPolicy, readiness probe.
3. **CrashLoopBackOff** — логи: `kubectl logs <POD>`, предыдущий контейнер: `kubectl logs <POD> --previous`.
4. **DNS/сеть** — `kubectl exec -it <POD> -- curl` к Service по имени, проверка CoreDNS.
5. **Ingress/Service type** — правильный порт, selector совпадает с labels пода.

</b></details>

<a id="istio"></a>
### Istio

<details>
<summary>Что такое Истио? Для чего он используется?</summary><br><b>

Istio — это сервисная сетка с открытым исходным кодом, которая помогает организациям запускать распределенные приложения на основе микросервисов где угодно. Istio позволяет организациям защищать, подключать и контролировать микросервисы, чтобы они могли быстрее и безопаснее модернизировать свои корпоративные приложения.

</b></details>

<a id="controllers"></a>
### Контроллеры

<details>
<summary>Что такое контроллеры?</summary><br><b>

[Kubernetes.io](https://kubernetes.io/docs/concepts/architecture/controller): «В Kubernetes контроллеры — это циклы управления, которые наблюдают за состоянием вашего кластера, а затем при необходимости вносят или запрашивают изменения. Каждый контроллер пытается приблизить текущее состояние кластера к желаемому».

</b></details>

<details>
<summary>Назовите два контроллера, с которыми вы знакомы.</summary><br><b>

1. Контроллер узла: управляет узлами кластера. Помимо прочего, контроллер отвечает за мониторинг работоспособности узлов — если узел внезапно станет недоступен, он эвакуирует все работающие на нем поды и соответствующим образом отметит состояние узла.
2. Контроллер репликации — отслеживает состояние реплик подов в зависимости от того, что должно быть запущено. Он гарантирует, что количество подов, которые должны быть запущены, действительно работает.

</b></details>

<details>
<summary>Какой процесс отвечает за запуск и установку различных контроллеров?</summary><br><b>

Kube-Контроллер-Менеджер

</b></details>

<details>
<summary>Что такое контур управления? Как это работает?</summary><br><b>

Объяснение [здесь](https://www.youtube.com/watch?v=i9V4oCa5f9I)

</b></details>

<details>
<summary>Каковы все фазы/этапы контура управления?</summary><br><b>

- Наблюдение – определение текущего состояния кластера.
- Разница. Определите, существует ли разница между текущим и желаемым состоянием.
- Действовать - привести текущее состояние кластера в желаемое состояние (по сути, достичь состояния, в котором нет различий)

</b></details>

<a id="scheduler"></a>
### Планировщик

<details>
<summary>Правда или ложь? Планировщик отвечает как за принятие решения о том, где будет запускаться под, так и за его фактический запуск.</summary><br><b>

Неверно. Хотя планировщик отвечает за выбор узла, на котором будет работать под, именно Kubelet фактически запускает под.

</b></details>

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

<a id="node-affinity"></a>
#### Node affinity

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

<details>
<summary>Правда или ложь? Использование типа привязки узла «requiredDuringSchedulingIgnoredDuringExecution» означает, что планировщик не может планировать, если правило не соблюдается.</summary><br><b>

Верно

</b></details>

<details>
<summary>Правда или ложь? Использование типа привязки узла «preferredDuringSchedulingIgnoredDuringExecution» означает, что планировщик не может планировать, если правило не соблюдается.</summary><br><b>

Неверно. Планировщик пытается найти узел, который соответствует требованиям/правилам, и если это не так, он все равно запланирует под.

</b></details>

<details>
<summary>Можете ли вы развернуть несколько планировщиков?</summary><br><b>

Да, это возможно. Можно запустить отдельный Pod с kube-scheduler, например:

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

<a id="taints"></a>
### Taints и tolerations

<details>
<summary>Проверьте, есть ли на узле <code>master</code> taints.</summary><br><b>

`kubectl describe node master | grep -i taints`

</b></details>

<details>
<summary>Добавьте taint на один из узлов вашего кластера с ключом «app», значением «web» и эффектом «NoSchedule». Убедитесь, что оно было применено</summary><br><b>

`kubectl taint nodes minikube app=web:NoSchedule`

`kubectl describe node minikube | grep -i taints`

</b></details>

<details>
<summary>Вы добавили <code>kubectl taint nodes minikube app=web:NoSchedule</code> на единственном узле кластера, затем выполнили <code>kubectl run some-pod --image=redis</code>. Что произойдёт?</summary><br><b>

Под останется в состоянии `Pending`, потому что на узле есть taint `app=web:NoSchedule`, а у пода нет toleration.

</b></details>

<details>
<summary>Вы добавили taint на единственном узле и запустили <code>kubectl run some-pod --image=redis</code>, но под в <code>Pending</code>. Как исправить?</summary><br><b>

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

<details>
<summary>Какие эффекты taint существуют? Объясните каждый из них</summary><br><b>

`NoSchedule`: предотвращает планирование ресурсов на определенном узле.
`PreferNoSchedule`: предпочтет планировать ресурсы на других узлах, прежде чем прибегать к планированию ресурса на выбранном узле (с этим taint).
`NoExecute`: применение «NoSchedule» не приведет к удалению уже запущенных подов (или других ресурсов) из узла, в отличие от «NoExecute», которое исключит любой уже запущенный ресурс из узла.

</b></details>

<a id="resource-limits"></a>
### Ограничения ресурсов

<details>
<summary>Объясните, почему нужно указывать ограничения ресурсов в отношении подов.</summary><br><b>

* Вы знаете, сколько ОЗУ и/или ЦП должно потреблять ваше приложение, а все, что выше этого значения, недействительно.
* Вы хотите убедиться, что каждый может запускать свои приложения в кластере, а ресурсы не используются только одним типом приложений.

</b></details>

<details>
<summary>Правда или ложь? Ограничения ресурсов применяются на уровне пода. Это означает, что если ограничения составляют 2 ГБ ОЗУ и в поде есть два контейнера, каждый из них имеет 1 ГБ ОЗУ.</summary><br><b>

Неверно. Лимиты и requests задаются **на уровне контейнера**, а не пода в целом.

</b></details>

<a id="resource-limits-commands"></a>
#### Ограничения ресурсов — команды

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

<a id="monitoring"></a>
### Мониторинг

<details>
<summary>Какие решения для мониторинга Kubernetes вам известны?</summary><br><b>

Существует множество типов решений для мониторинга Kubernetes. Некоторые из них с открытым исходным кодом, некоторые в памяти, некоторые из них стоят денег... вот краткий список:

* сервер метрик: мониторинг с открытым исходным кодом в памяти.
* datadog: $$$
* promethues: решение для мониторинга с открытым исходным кодом

</b></details>

<details>
<summary>Опишите, как решение для мониторинга, с которым вы работаете, контролирует Kubernetes</summary><br><b>

Зависит от стека. Типичные варианты:

* **metrics-server** — метрики CPU/RAM из kubelet/cAdvisor; `kubectl top nodes` / `kubectl top pods`.
* **Prometheus + kube-state-metrics** — метрики объектов API (Deployments, Pods, …), алерты, Grafana.
* **Datadog / New Relic / Dynatrace** — агенты на узлах или cluster agent, APM, логи, SLO.
* **Elastic / Loki** — сбор логов подов и событий кластера.
* **Cloud-native** — CloudWatch Container Insights, Google Cloud Monitoring, Azure Monitor for containers.

Обычно: discovery через Kubernetes API или annotations, scrape/kubelet, экспорт в TSDB или SaaS.

</b></details>

<a id="kustomize-overlays"></a>
### Kustomize

<details>
<summary>Что такое кастомизация?</summary><br><b>

Речь о **Kustomize**: декларативном оверлее поверх манифестов без форков исходников (`kustomization.yaml`, `bases`, `patches`, `images`, генераторы ConfigMap/Secret).

</b></details>

<details>
<summary>Объясните необходимость настройки, описав реальные случаи использования.</summary><br><b>

* У вас есть контрольная диаграмма приложения, используемого несколькими командами в вашей организации, и необходимо добавить к приложению аннотацию с указанием имени команды, владеющей приложением.
  * Без настройки Kustomize вам нужно будет скопировать файлы (в данном случае шаблон диаграммы) и изменить их, включив в них конкретные аннотации, которые нам нужны.
  * С помощью Kustomize вам не нужно копировать весь репозиторий или файлы целиком.
* Вас попросят применить изменение/исправление к какому-либо приложению, не изменяя исходные файлы приложения.
  * С помощью Kustomize вы можете определить файл kustomization.yml, который определяет эти настройки, поэтому вам не нужно трогать исходные файлы приложения.

</b></details>

<details>
<summary>Опишите в общих чертах, как работает Kustomize.</summary><br><b>

1. Вы добавляете файл kustomization.yml в папку приложения, которое хотите настроить.
   1. Вы определяете настройки, которые хотите выполнить.
2. Вы запускаете `kustomize build APP_PATH` (или `kubectl kustomize`), где лежит ваш `kustomization.yaml`.

</b></details>

<a id="deployment-strategies"></a>
### Стратегии развёртывания

<details>
<summary>Какие стратегии развертывания/развертывания вам известны?</summary><br><b>

* Синие/зеленые развертывания: вы развертываете новую версию своего приложения, пока старая версия все еще работает, и начинаете перенаправлять трафик на новую версию приложения.
* Канарские развертывания: вы развертываете новую версию своего приложения и начинаете перенаправлять **часть** своих пользователей/трафика на новую версию. Таким образом, переход на новую версию происходит гораздо более постепенно.

</b></details>

<details>
<summary>Подробное объяснение синего/зеленого развертывания/развертывания.</summary><br><b>

Этапы развертывания синего/зеленого цвета:

1. Трафик, поступающий от пользователей через балансировщик нагрузки в приложение, которое на данный момент имеет версию 1.

Пользователи -> Балансировщик нагрузки -> Версия приложения 1.

2. Развертывается новая версия приложения 2 (при этом версия 1 все еще работает).

Пользователи -> Балансировщик нагрузки -> Версия приложения 1.
                          Версия приложения 2

3. Если версия 2 работает корректно, трафик переключился на нее вместо версии 1.

Пользователь -> Приложение Load Balancer, версия 1.
                       -> Версия приложения 2

4. Удаляется ли старая версия или она продолжает работать, но без перенаправления на нее пользователей, зависит от решения команды или компании.

Плюсы:
  * Мы можем быстро откатиться/переключиться на предыдущую версию в любой момент
Минусы:
  * В случае возникновения проблемы с новой версией затрагиваются ВСЕ пользователи (а не небольшая часть/процент)

</b></details>

<details>
<summary>Подробное объяснение развертывания/развертывания Canary.</summary><br><b>

Этапы развертывания Canary:

1. Трафик, поступающий от пользователей через балансировщик нагрузки в приложение, которое на данный момент имеет версию 1.

Пользователи -> Балансировщик нагрузки -> Версия приложения 1.

2. Развертывается новое приложение версии 2 (при этом версия 1 еще работает) и часть трафика перенаправляется на новую версию.

Пользователи -> Балансировщик нагрузки -> (95% трафика) Версия приложения 1
                       ->(5% трафика) Версия приложения 2

3. Если новая версия (2) работает хорошо, на нее перенаправляется больше трафика.

Пользователи -> Балансировщик нагрузки -> (70% трафика) Версия приложения 1
                       ->(30% трафика) Версия приложения 2

3. Если все работает хорошо, в какой-то момент весь трафик перенаправляется на новую версию.

Пользователи -> Балансировщик нагрузки -> Версия приложения 2.


Плюсы:
  * Если есть какие-либо проблемы с новой развернутой версией приложения, затронуты только некоторые пользователи, а не все.
Минусы:
  * Тестирование новой версии обязательно в производственной среде (так как пользовательский трафик существует только там)

</b></details>

<details>
<summary>Какие способы реализации стратегий развертывания (например, canary, blue/green) в Kubernetes вам известны?</summary><br><b>

Есть несколько способов. Один из них — Argo Rollouts.

</b></details>

<a id="scenarios"></a>
### Сценарии

<details>
<summary>Инженер из вашей организации сказал вам, что его интересует только доступ к ресурсам своей команды в Kubernetes. Вместо этого на самом деле он видит ресурсы всей организации, из множества разных команд. Какую концепцию Kubernetes вы можете использовать, чтобы справиться с этим?</summary><br><b>

Пространства имен. Дополнительную информацию см. в следующем [вопросе и ответе о пространствах имен](#namespaces-use-cases).

</b></details>

<details>
<summary>Инженер из вашей команды запускает под, но видит статус «CrashLoopBackOff». Что это значит? Как определить проблему?</summary><br><b>

Контейнер не удалось запустить (по разным причинам), и Kubernetes пытается снова запустить под через некоторую задержку (= время ожидания).

Некоторые причины неудачи:
  - Неправильная конфигурация: опечатка, неподдерживаемое значение и т. д.
  - Ресурс недоступен - узлы не работают, фотоэлектрическая система не установлена и т. д.

Некоторые способы отладки:

1. `kubectl describe pod POD_NAME`
   1. Сосредоточьтесь на «Состоянии» (это должно быть `Pending`, «CrashLoopBackOff») и «Последнее состояние», которые должны сообщать, что произошло раньше (например, почему произошел сбой).
2. Запустите kubectl logs mypod.
   1. Это должно обеспечить точный вывод 
   2. Для конкретного контейнера вы можете добавить `-c CONTAINER_NAME`

</b></details>

<details>
<summary>Инженер из вашей организации спросил, есть ли способ запретить планирование подов (с заданной меткой) на одном из узлов кластера. Ваш ответ:</summary><br><b>

Да, используя taints, мы могли бы запустить следующую команду, и она предотвратит планирование всех ресурсов с меткой «app=web» на узле 1: `kubectl taint node node1 app=web:NoSchedule`

</b></details>

<details>
<summary>Вы хотите ограничить количество ресурсов, используемых в вашем кластере. Например, не более 4 наборов реплик, 2 сервисов и т. д. Как бы вы этого достигли?</summary><br><b>

Использование ResourceQuats

</b></details><!-- {% endraw %} -->