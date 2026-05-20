## AWS — Cloud Practitioner

Краткий обзор материала к экзамену — [на сайте AWS](https://aws.amazon.com/certification/certified-cloud-practitioner/).

#### Основы облака

<details>
<summary>Что такое облачные вычисления?</summary><br><b>

[Википедия](https://en.wikipedia.org/wiki/Cloud_computing): «Облачные вычисления — это предоставление по требованию ресурсов компьютерной системы, прежде всего хранения данных (облачное хранилище) и вычислительной мощности, без прямого активного управления со стороны пользователя».

Облако позволяет масштабировать ресурсы вверх или вниз по необходимости и платить только за фактическое потребление.
</b></details>

<details>
<summary>Какие бывают модели облачных сервисов?</summary><br><b>

IaaS  
PaaS  
SaaS

</b></details>

<details>
<summary>Объясните каждую модель и приведите пример

  * IaaS
  * PaaS
  * SaaS</summary><br><b>

- **IaaS (Infrastructure as a Service)** — поставщик облака сдаёт в аренду ИТ-инфраструктуру: вычисления, сеть, хранение (например, Amazon EC2).<br>

- **PaaS (Platform as a Service)** — готовая платформа с доступом по требованию к инструментам развёртывания, управления приложениями и DevOps (например, AWS Elastic Beanstalk).<br>

- **SaaS (Software as a Service)** — приложение размещается у поставщика облака; пользователь получает сервис «как есть» (например, AWS WorkSpaces или веб-почта).
</b></details>

<details>
<summary>Какие бывают типы облака (модели развёртывания)?</summary><br><b>

  * Публичное
  * Гибридное
  * Частное

</b></details>

<details>
<summary>Объясните каждую модель развёртывания

  * Публичное
  * Гибридное
  * Частное</summary><br><b>

- **Публичное** — сервисы в интернете на оборудовании провайдера; ресурсы совместно используются клиентами. Обычно дешевле и проще масштабировать.<br>

- **Гибридное** — сочетание публичного облака, частного облака и/или локального ЦОД. Даёт гибкость и больше вариантов размещения рабочих нагрузок.<br>

- **Частное** — инфраструктура выделена одной организации; ресурсы не делятся с другими — выше контроль над безопасностью и данными.

[Подробнее у AWS](https://aws.amazon.com/types-of-cloud-computing/)
</b></details>

#### Глобальная инфраструктура AWS

<details>
<summary>Объясните термины

  * Зона доступности (Availability Zone)
  * Регион (Region)
  * Пограничная точка (Edge location)</summary><br><b>

**Регионы AWS** — географически разнесённые площадки с дата-центрами; регионы независимы друг от друга.<br>

Внутри региона есть несколько изолированных **зон доступности (AZ)**. Несколько AZ повышают отказоустойчивость. Каждая AZ физически отделена: своё электропитание, сеть и связность.<br>

**Edge locations** — точки сети доставки контента (CDN): кэшируют данные и снижают задержку для пользователей по всему миру; обычно расположены в крупных городах.
</b></details>

#### Сеть в AWS

<details>
<summary>Что такое VPC?</summary><br><b>

«Логически изолированный участок облака AWS, в котором вы запускаете ресурсы в определённой вами виртуальной сети».  
Подробнее: [Amazon VPC](https://aws.amazon.com/vpc).

Одна VPC охватывает все зоны доступности **одного** региона.
</b></details>

<details>
<summary>Верно или нет? VPC охватывает несколько регионов</summary><br><b>

Неверно. VPC привязана к региону и не может охватывать несколько регионов.
</b></details>

<details>
<summary>Верно или нет? Подсети принадлежат одной VPC и могут находиться в разных зонах доступности</summary><br><b>

Верно. Уточнение: одна подсеть целиком лежит в **одной** AZ, но в одной VPC может быть много подсетей в разных AZ.
</b></details>

<details>
<summary>Что такое Internet Gateway?</summary><br><b>

«Компонент, обеспечивающий обмен трафиком между инстансами в VPC и интернетом» (документация AWS).  
Подробнее: [VPC Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)

Масштабируется горизонтально, высокодоступен; входящий и исходящий трафик не упирается в искусственные лимиты пропускной способности со стороны шлюза.
</b></details>

<details>
<summary>Верно или нет? NACL разрешают или запрещают трафик на уровне подсети</summary><br><b>

Верно.
</b></details>

<details>
<summary>Верно или нет? К одной VPC можно подключить несколько Internet Gateway</summary><br><b>

Неверно. К одной VPC подключается **один** Internet Gateway.
</b></details>

<details>
<summary>Верно или нет? Таблицы маршрутизации служат для разрешения или запрета трафика из интернета к инстансам AWS</summary><br><b>

Неверно. Таблицы маршрутизации **направляют** трафик к нужной цели (Internet Gateway, NAT Gateway и т.д.), а не решают allow/deny — этим занимаются NACL и security groups.
</b></details>

<details>
<summary>Объясните Security Groups и Network ACL</summary><br><b>

* **NACL** — уровень **подсети**; **без состояния (stateless)**: входящие и исходящие правила оцениваются отдельно.<br>
* **Security group** — уровень **инстанса**; **с отслеживанием состояния (stateful)**: разрешив входящий ответный трафик, исходящий для установленной сессии обычно разрешается автоматически.

Документация: [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html), [VPC security](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

<details>
<summary>Что такое AWS Direct Connect?</summary><br><b>

Выделенное сетевое подключение корпоративной сети к сети AWS; даёт более предсказуемую производительность, чем типичный доступ через интернет.
</b></details>

#### Вычисления (Compute) в AWS

<details>
<summary>Что такое EC2?</summary><br><b>

«Веб-сервис, который предоставляет безопасные изменяемые по размеру вычислительные мощности в облаке».  
Подробнее: [Amazon EC2](https://aws.amazon.com/ec2).

EC2 позволяет быстро масштабировать мощность под нагрузку и платить только за время использования вычислений.
</b></details>

<details>
<summary>Что такое AMI?</summary><br><b>

**Amazon Machine Image (AMI)** — «образ, который содержит информацию, необходимую для запуска инстанса».  
Документация: [AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html).

Обычно в AMI входят ОС, прикладной стек и приложения — чтобы поднимать новые инстансы с одинаковой конфигурацией.
</b></details>

<details>
<summary>Откуда берутся AMI?</summary><br><b>

* **Свои AMI** — созданные вами.
* **AWS Marketplace** — платные AMI, часто с лицензируемым ПО.
* **Community AMIs** — бесплатные образы сообщества.

При необходимости AMI можно **делиться между аккаунтами** AWS.
</b></details>

<details>
<summary>Что такое тип инстанса (instance type)?</summary><br><b>

«Тип инстанса определяет аппаратную платформу хоста, на котором выполняется ваш инстанс».  
Справочник типов: [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html).

Типы различаются по CPU, памяти, диску и сети (например, `t2.micro`, `c5.large` и т.д.).
</b></details>

<details>
<summary>Верно или нет? В AWS доступны такие «семейства» инстансов:

  * compute optimized
  * network optimized
  * web optimized</summary><br><b>

Неверно. Из перечисленного как отдельного «семейства» в классификации AWS нет **web optimized** и **network optimized**; есть, например, compute-, memory- и storage-optimized и другие линейки.
</b></details>

<details>
<summary>Что такое EBS?</summary><br><b>

«Блочные тома хранения для инстансов EC2; ведут себя как «сырые» блочные устройства».  
Подробнее: [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html).

Том EBS привязан к **зоне доступности**. Его можно снапшотить в S3 для долговечности и подключать/отключать к инстансам **в той же AZ**.
</b></details>

<details>
<summary>Какие модели оплаты за EC2 существуют?</summary><br><b>

**On-Demand** — фиксированная ставка за час/секунду без обязательств; можно создавать и удалять в любой момент.<br>
**Reserved Instances** — резервирование мощности на срок (1 или 3 года); чем дольше обязательство, тем ниже цена.<br>
**Spot** — цена рынка спота; подходит для **прерываемых** нагрузок.<br>
**Dedicated Hosts** — физический сервер EC2 под вас; удобно для лицензирования ПО и требований compliance.
</b></details>

<details>
<summary>Что такое security groups?</summary><br><b>

«Security group действует как виртуальный файрвол для одного или нескольких инстансов».  
Подробнее: [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).

Они **stateful**: правило на вход часто подразумевает корректный ответный исходящий трафик для установленной сессии (в рамках модели отслеживания соединений).
</b></details>

<details>
<summary>Что можно подключить к EC2 для хранения данных?</summary><br><b>

Прежде всего **EBS**.

Дополнительно: у части типов инстансов есть **Instance Store** (локальный эфемерный диск); для общей файловой системы между инстансами — **Amazon EFS**.
</b></details>

<details>
<summary>Какие бывают типы Reserved Instances для EC2?</summary><br><b>

**Standard RI** — максимальная скидка при стабильной нагрузке.<br>
**Convertible RI** — ниже скидка, но можно **менять атрибуты** RI при той же стабильной модели использования.<br>
**Scheduled RI** — инстансы в **заранее забронированных** временных окнах.

Подробнее: [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances).

У части RI различаются варианты оплаты (без предоплаты, частичная и полная предоплата) — от этого зависит уровень скидки.
</b></details>

#### Контейнеры в AWS

<details>
<summary>Что такое Amazon ECS?</summary><br><b>

По определению AWS: «Amazon Elastic Container Service (ECS) — полностью управляемый сервис оркестрации контейнеров». Крупные заказчики используют ECS для критичных приложений из‑за безопасности, надёжности и масштабируемости.

Подробнее: [Amazon ECS](https://aws.amazon.com/ecs)
</b></details>

<details>
<summary>Что такое Amazon ECR?</summary><br><b>

«Amazon Elastic Container Registry (ECR) — полностью управляемый реестр образов контейнеров (Docker/OCI), в котором удобно хранить, управлять и развёртывать образы».

Подробнее: [Amazon ECR](https://aws.amazon.com/ecr)
</b></details>

<details>
<summary>Что такое AWS Fargate?</summary><br><b>

«AWS Fargate — бессерверная среда выполнения для контейнеров, которая работает и с **Amazon ECS**, и с **Amazon EKS**».

Подробнее: [AWS Fargate](https://aws.amazon.com/fargate)
</b></details>

#### Хранение данных в AWS

<details>
<summary>Что такое Amazon S3?</summary><br><b>

**S3** — **S**imple **S**torage **S**ervice: объектное хранилище, рассчитанное на высокую скорость, масштаб и долговечность. Объект может быть до **5 ТБ** (с учётом лимитов на составной upload).

Подробнее: [Amazon S3](https://aws.amazon.com/s3)
</b></details>

<details>
<summary>Что такое bucket (бакет)?</summary><br><b>

Бакет S3 — контейнер верхнего уровня (аналог «корня» или префиксов в ключах объектов), в котором хранятся **объекты** — данные и метаданные.
</b></details>

<details>
<summary>Верно или нет? Имя бакета должно быть глобально уникальным</summary><br><b>

Верно — в пределах партиции S3 имя бакета глобально уникально.
</b></details>

<details>
<summary>«Папки» и объекты в S3 — что это?</summary><br><b>

* **Префикс («папка»)** — часть **ключа объекта** до `/`; S3 не является классической иерархической ФС, но префиксы отображаются как каталоги в консоли.
* **Объект** — неделимая сущность с данными, ключом и метаданными внутри бакета.
</b></details>

<details>
<summary>Объясните возможности

  * жизненный цикл объектов (Lifecycle)
  * совместный доступ к объектам (Sharing)
  * версионирование (Versioning)</summary><br><b>

* **Lifecycle** — автоматические переходы между классами хранения или удаление по правилам и срокам.
* **Sharing** — выдача доступа по URL (presigned URL, ACL, политики бакета и т.д.).
* **Versioning** — хранение нескольких версий одного ключа объекта.
</b></details>

<details>
<summary>Долговечность и доступность объекта в S3 — что означают?</summary><br><b>

**Durability** — насколько маловероятна потеря объекта за длительный период (для стандартных классов S3 заявляется крайне высокая долговечность — порядка «одиннадцати девяток» в год).  
**Availability** — какой процент времени объект ожидаемо **доступен** для операций (зависит от класса хранения и архитектуры сервиса).
</b></details>

<details>
<summary>Что такое класс хранения (storage class)? Какие классы бывают?</summary><br><b>

У каждого объекта есть класс хранения — от него зависят **цена**, **доступность** и **модель доступа** (в т.ч. время выборки для архивных классов).

Кратко по линейке (актуальные названия смотрите в документации AWS):

  * **S3 Standard** — частый доступ, универсальные данные; высокая доступность; класс по умолчанию.
  * **Standard-IA** — редкий доступ, но когда понадобилось — нужен быстрый доступ; ниже цена за хранение, выше за запросы.
  * **One Zone-IA** — как IA, но данные в **одной** AZ; дешевле, ниже устойчивость к локальному сбою AZ.
  * **S3 Intelligent-Tiering** — автоматический выбор уровня по паттерну доступа; плата за автоматизацию + хранение по фактическому уровню.
  * **Glacier** и **Glacier Deep Archive** — архивы с **минутами–часами** времени выборки (Deep Archive дольше и дешевле хранение).

Сводная таблица и цены: [S3 storage classes](https://aws.amazon.com/s3/storage-classes)

</b></details>

<details>
<summary>Клиент хочет перевести редко читаемые данные из Standard в **самый дешёвый** класс хранения. Что выбрать из списка?

  * One Zone-IA
  * Glacier Deep Archive
  * Intelligent-Tiering</summary><br><b>

**Glacier Deep Archive** — минимальная стоимость хранения при допустимости долгой выборки.
</b></details>

<details>
<summary>Какие режимы выборки (retrieval) бывают у Glacier?</summary><br><b>

**Expedited**, **Standard**, **Bulk** (набор и названия зависят от подтипа архива; детали — в документации Glacier).
</b></details>

<details>
<summary>Верно или нет? В аккаунте AWS жёсткий лимит 500 ПБ данных; сверх — плата удваивается</summary><br><b>

Неверно. S3 масштабируется под очень большие объёмы; конкретные лимиты и цены — в документации и калькуляторе AWS.
</b></details>

<details>
<summary>Что такое AWS Storage Gateway?</summary><br><b>

«Гибридный сервис хранения: даёт приложениям **на площадке заказчика** доступ к практически неограниченному облачному хранилищу AWS».

Подробнее: [Storage Gateway](https://aws.amazon.com/storagegateway)
</b></details>

<details>
<summary>Типы развёртывания Storage Gateway

  * File Gateway
  * Volume Gateway
  * Tape Gateway</summary><br><b>

Сравнение и сценарии: [Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs)
</b></details>

<details>
<summary>Чем stored volumes отличаются от cached volumes?</summary><br><b>

**Stored volumes** — основной массив данных остаётся **локально** у заказчика, в облако уходит резервное копирование/синхронизация по политике.  
**Cached volumes** — основной массив в **AWS**, в ЦОД кэшируется «горячий» поднабор для низкой задержки.
</b></details>

<details>
<summary>Что такое Amazon S3 Transfer Acceleration?</summary><br><b>

«Ускорение передачи в S3 для быстрых и безопасных загрузок/выгрузок на больших расстояниях между клиентом и бакетом».

Подробнее: [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)
</b></details>

<details>
<summary>Что такое Amazon EFS?</summary><br><b>

«Полностью управляемая эластичная файловая система **NFS** для облачных и гибридных сценариев».

Подробнее: [Amazon EFS](https://aws.amazon.com/efs)
</b></details>

<details>
<summary>Что такое AWS Snowmobile?</summary><br><b>

«Сервис переноса данных эксабайтного масштаба для перемещения очень больших объёмов в AWS».

Подробнее: [AWS Snowmobile](https://aws.amazon.com/snowmobile)
</b></details>

#### AWS IAM

<details>
<summary>Что такое IAM? Какие у него основные сущности?</summary><br><b>

**IAM (Identity and Access Management)** — управление **пользователями**, **группами**, **ролями** и **политиками** доступа в AWS.

Обзор: [AWS IAM](https://aws.amazon.com/iam)
</b></details>

<details>
<summary>Верно или нет? Настройки IAM глобальны для аккаунта, а не «на регион»</summary><br><b>

Верно: пользователи, группы, роли и политики IAM — **глобальные** сущности аккаунта AWS.
</b></details>

<details>
<summary>Верно или нет? При создании аккаунта AWS появляется пользователь root — его рекомендуется использовать и раздавать коллегам</summary><br><b>

Неверно. **Root** нужен для ограниченного набора административных операций; повседневную работу ведут **IAM-пользователи** (или SSO), с принципом наименьших привилегий.
</b></details>

<details>
<summary>Верно или нет? В IAM группа может содержать только пользователей, но не другие группы</summary><br><b>

Верно: вложенных «групп групп» в IAM нет.
</b></details>

<details>
<summary>Верно или нет? IAM-пользователь может состоять только в одной группе</summary><br><b>

Неверно. Пользователь может входить **в несколько** групп.
</b></details>

<details>
<summary>Что такое роли (roles)?</summary><br><b>

Способ **делегировать** права: сервис или принципал временно «надевает» роль и получает разрешения из её политик. Роли часто назначают **ресурсам** (например, инстансу EC2), чтобы он обращался к S3 без долгоживущих ключей на диске.

Пример: роль для EC2 с правами чтения/записи в конкретные бакеты S3.
</b></details>

<details>
<summary>Что такое политики (policies)?</summary><br><b>

Документы (обычно **JSON**), описывающие **разрешения** и **условия** для пользователей, групп или ролей.
</b></details>

<details>
<summary>Пользователь не может получить доступ к бакету S3. Что проверить в первую очередь?</summary><br><b>

Типичные причины: нет нужной **политики** (ни на пользователе/группе, ни через роль), запрет в **bucket policy**, конфликт **ACL** (если используется), неверный **ключ объекта**, запрет со стороны **KMS** для шифрования, ограничения **VPC endpoint** и т.д. Администратору стоит явно привязать минимально достаточную политику и проверить отказ в CloudTrail.
</b></details>

<details>
<summary>Чем задать доступ

  * между двумя сервисами/ресурсами?
  * пользователю к сервисам/ресурсам?</summary><br><b>

* **Роль** (часто для сервис-к-сервису и для временных учётных данных).
* **Политика** (на пользователя, группу или роль).

</b></details>

<details>
<summary>Какие права по умолчанию у только что созданного IAM-пользователя?</summary><br><b>

По сути **нет прав на API-операции**, пока явно не назначены политики; может быть настроен только вход (пароль/ключи — по решению администратора).
</b></details>

##### Elastic Load Balancing (ELB)

<details>
<summary>Что такое ELB (Elastic Load Balancing)?</summary><br><b>

«Elastic Load Balancing автоматически распределяет входящий трафик приложения между целями — инстансами EC2, контейнерами, IP-адресами, функциями Lambda и др.»

Подробнее: [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing)
</b></details>

<details>
<summary>Что такое Auto Scaling?</summary><br><b>

«AWS Auto Scaling следит за приложением и автоматически подстраивает мощность, чтобы сохранять стабильную производительность при разумных затратах».

Подробнее: [AWS Auto Scaling](https://aws.amazon.com/autoscaling)
</b></details>

<details>
<summary>Верно или нет? Auto Scaling только добавляет ресурсы (инстансы), но никогда их не убирает</summary><br><b>

Неверно. Масштабирование **двустороннее**: при падении нагрузки лишние инстансы могут быть завершены по политике.
</b></details>

<details>
<summary>Какие типы балансировщиков нагрузки поддерживаются в экосистеме EC2 и для чего они?</summary><br><b>

* **Application Load Balancer (ALB)** — балансировка на **уровне 7** (HTTP/HTTPS).
* **Network Load Balancer (NLB)** — **уровень 4**, очень высокая производительность, статические IP/Elastic IP на фронте.
* **Classic Load Balancer (CLB)** — прежнее поколение; для новых проектов обычно выбирают ALB/NLB.

</b></details>

#### DNS в AWS

<details>
<summary>Что такое Route 53?</summary><br><b>

«Amazon Route 53 — высокодоступный и масштабируемый **DNS**-веб-сервис».

Возможности: регистрация доменов, публичные/приватные зоны, маршрутизация трафика, **проверки работоспособности (health checks)**.

Подробнее: [Amazon Route 53](https://aws.amazon.com/route53)
</b></details>

#### Amazon CloudFront

<details>
<summary>Что такое CloudFront?</summary><br><b>

«Amazon CloudFront — CDN для безопасной доставки данных, видео, приложений и API по всему миру с низкой задержкой и высокой скоростью».

Подробнее: [Amazon CloudFront](https://aws.amazon.com/cloudfront)
</b></details>

<details>
<summary>Объясните термины

  * Origin
  * Edge location
  * Distribution</summary><br><b>

* **Origin** — исходный источник контента (например, бакет S3, ALB/API в VPC, MediaPackage и т.д.), откуда CloudFront забирает объекты при промахе кэша.
* **Edge location** — пограничная точка CDN, где хранится кэш и обрабатывается запрос пользователя.
* **Distribution** — конфигурация CDN: источники, поведение кэша, сертификаты TLS, политики, связь edge↔origin.

</b></details>

#### Мониторинг и журналирование в AWS

<details>
<summary>Что такое Amazon CloudWatch?</summary><br><b>

«Amazon CloudWatch — сервис мониторинга и наблюдаемости за метриками, логами и событиями в AWS».

Подробнее: [Amazon CloudWatch](https://aws.amazon.com/cloudwatch)
</b></details>

<details>
<summary>Что такое AWS CloudTrail?</summary><br><b>

«AWS CloudTrail записывает действия API в вашем аккаунте и помогает аудиту, расследованиям и соответствию требованиям».

Подробнее: [AWS CloudTrail](https://aws.amazon.com/cloudtrail)
</b></details>

<details>
<summary>Что такое Amazon Simple Notification Service (SNS)?</summary><br><b>

«Высокодоступный управляемый сервис pub/sub для обмена сообщениями между микросервисами, распределёнными системами и бессерверными приложениями».

Подробнее: [Amazon SNS](https://aws.amazon.com/sns)
</b></details>

<details>
<summary>Термины SNS: Topics, Subscribers, Publishers</summary><br><b>

* **Topic** — именованный канал; сообщение публикуется в topic и доставляется подписчикам.
* **Subscriber** — получатель: email, HTTP(s), SQS, Lambda, мобильные push и др.
* **Publisher** — кто отправляет сообщение в topic (сервис AWS, приложение, человек).

</b></details>

#### Безопасность в AWS

<details>
<summary>Что такое модель общей ответственности (shared responsibility)? Кто за что отвечает?</summary><br><b>

Модель разделяет ответственность: **AWS** отвечает за безопасность **облака** (площадки, сеть виртуализации, изоляция «соседей» и т.д.), а **клиент** — за безопасность **в облаке** (конфигурация сервисов, данные, управление доступом, патчи гостевой ОС на EC2 и т.п.).

Подробнее: [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Верно или нет? По модели общей ответственности Amazon отвечает за физические CPU **и** за ваши security groups на инстансах</summary><br><b>

Неверно. За физическую инфраструктуру отвечает AWS; **security groups** задаёт и ведёт **клиент** (как часть конфигурации VPC/EC2).
</b></details>

<details>
<summary>Что такое «Shared Controls» в модели общей ответственности?</summary><br><b>

«Общие меры» применяются и к инфраструктуре AWS, и к использованию сервисов клиентом, но **в разных плоскостях**: AWS задаёт базовые требования к платформе, а клиент реализует контроли в своей архитектуре и политиках.

Подробнее: [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Что такое программа соответствия (compliance) AWS?</summary><br><b>

Набор сертификаций, отчётов и рамок (например, ISO, SOC, HIPAA BAA и др.), подтверждающих, что AWS строит и эксплуатирует платформу согласно требованиям регуляторов и отраслевых стандартов. Конкретный перечень зависит от региона и сервиса — см. официальный **AWS Compliance** раздел.
</b></details>

<details>
<summary>Что такое AWS Artifact?</summary><br><b>

«Централизованный доступ к отчётам AWS по безопасности и соответствию и к ряду соглашений (NDA и т.п.)».

Подробнее: [AWS Artifact](https://aws.amazon.com/artifact)
</b></details>

<details>
<summary>Что такое Amazon Inspector?</summary><br><b>

«Сервис автоматической оценки безопасности рабочих нагрузок: уязвимости, открытые поверхности, отклонения от практик».

Подробнее: [Amazon Inspector](https://aws.amazon.com/inspector)
</b></details>

<details>
<summary>Что такое Amazon GuardDuty?</summary><br><b>

Управляемый сервис **обнаружения угроз**: анализирует логи и события (CloudTrail, VPC Flow Logs, DNS и др.) и сигнализирует о подозрительной активности в аккаунте.
</b></details>

<details>
<summary>Что такое AWS Shield?</summary><br><b>

«Управляемая защита от DDoS для приложений в AWS» (уровни Standard/Advanced).

Документация: [AWS Shield](https://aws.amazon.com/shield/)
</b></details>

<details>
<summary>Что такое AWS WAF? Пример использования и с чем интегрируют</summary><br><b>

**AWS WAF** — правила на уровне L7 для фильтрации HTTP(S): боты, SQLi, XSS, гео- и rate-limit. Часто ставят **перед** приложением на **CloudFront** или **Application Load Balancer**, чтобы отсечь атаки до origin.
</b></details>

<details>
<summary>Для чего нужен AWS Site-to-Site VPN?</summary><br><b>

Шифрованный **IPsec-туннель** между **вашим шлюзом** (или SD-WAN) и **Virtual Private Gateway / Transit Gateway** в AWS для связи on-prem сети с VPC.
</b></details>

<details>
<summary>Чем AWS Client VPN отличается от Site-to-Site VPN?</summary><br><b>

**Client VPN** — удалённые пользователи подключаются клиентским OpenVPN-профилем к облачной сети. **Site-to-Site** — постоянный туннель между **сайтами** (двумя маршрутизируемыми сетями), а не «с лаптопа одного сотрудника».
</b></details>

<details>
<summary>Что такое AWS CloudHSM?</summary><br><b>

«Облачный аппаратный модуль безопасности (HSM) для генерации и использования ваших ключей в AWS с FIPS 140-2 Level 3».

Подробнее: [AWS CloudHSM](https://aws.amazon.com/cloudhsm)
</b></details>

<details>
<summary>Верно или нет? Amazon Inspector может выполнять и сетевые, и хостовые оценки (в зависимости от поколения/режима сервиса)</summary><br><b>

Верно в смысле экзаменационного ожидания: Inspector развивается и покрывает разные типы находок; детали — в текущей документации сервиса.
</b></details>

<details>
<summary>Что такое AWS Acceptable Use Policy (AUP)?</summary><br><b>

Документ, который перечисляет **запрещённые** виды использования сервисов AWS (злоупотребления, незаконный контент и т.д.).

Текст политики: [AWS AUP](https://aws.amazon.com/aup)
</b></details>

<details>
<summary>Что такое AWS KMS?</summary><br><b>

«Сервис для создания и управления криптографическими ключами и контроля их использования в сервисах AWS и ваших приложениях».

Подробнее: [AWS KMS](https://aws.amazon.com/kms)
</b></details>

<details>
<summary>Верно или нет? Пентест **любых** сервисов AWS без ограничений разрешён всегда</summary><br><b>

Неверно. Есть **политика пентеста** с перечнем разрешённых сервисов и условий; часть действий требует предварительного запроса/исключений.
</b></details>

<details>
<summary>Верно или нет? DDoS-атака — пример разрешённого пентеста</summary><br><b>

Неверно.
</b></details>

<details>
<summary>Верно или нет? Access Key AWS — это тип MFA-устройства</summary><br><b>

Неверно. **Access key** — долгоживущие программные учётные данные пользователя; MFA — отдельный второй фактор (TOTP, U2F/WebAuthn и т.д.).
</b></details>

<details>
<summary>Что такое Amazon Cognito?</summary><br><b>

«Сервис аутентификации и авторизации пользователей для веб- и мобильных приложений» (пулы пользователей, федерация, hosted UI).

Документация: [Amazon Cognito](https://docs.aws.amazon.com/cognito/index.html)
</b></details>

<details>
<summary>Что такое AWS Certificate Manager (ACM)?</summary><br><b>

«Сервис выдачи и обновления публичных и приватных TLS-сертификатов для интеграции с сервисами AWS».

Подробнее: [AWS Certificate Manager](https://aws.amazon.com/certificate-manager)
</b></details>

#### Базы данных в AWS

<details>
<summary>Что такое Amazon RDS?</summary><br><b>

**Amazon Relational Database Service (RDS)** — управляемый сервис для реляционных СУБД (выбор движка, резервные копии, патчи, реплики, Multi-AZ и т.д.) с оплатой по потреблению.

Документация: [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
</b></details>

<details>
<summary>Что такое Amazon DynamoDB?</summary><br><b>

Полностью управляемая **NoSQL** база данных модели «ключ–значение» и документов с предсказуемой масштабируемостью и низкой задержкой; подходит для сессий, каталогов, игровых таблиц лидеров и т.п.
</b></details>

<details>
<summary>Что даёт Point-in-Time Recovery (PITR) в DynamoDB?</summary><br><b>

«Непрерывные бэкапы с восстановлением таблицы на произвольную секунду в окне хранения». Есть и **on-demand** снимки таблиц.

Подробнее: [PITR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
</b></details>

<details>
<summary>Что такое Global Tables в DynamoDB?</summary><br><b>

«**Глобальная таблица** — набор реплик одной логической таблицы в нескольких регионах под одним аккаунтом AWS с автоматической многонаправленной репликацией».

Подробнее: [Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
</b></details>

<details>
<summary>Что такое DynamoDB Accelerator (DAX)?</summary><br><b>

«Полностью управляемый in-memory кэш перед DynamoDB, который снижает задержку чтения с миллисекунд до микросекунд для горячих ключей».

Подробнее: [Amazon DAX](https://aws.amazon.com/dynamodb/dax)
</b></details>

<details>
<summary>Чем Amazon Redshift отличается от RDS?</summary><br><b>

**Redshift** — колонночное **хранилище данных** для аналитики на больших объёмах (часто — петабайты) и сложных SQL-запросов.  
**RDS** — транзакционные OLTP-сценарии веб-приложений с типичными CRUD-операциями и меньшими объёмами данных на инстанс.
</b></details>

<details>
<summary>Что такое Amazon ElastiCache? Типичные сценарии</summary><br><b>

Управляемые **Redis** или **Memcached** в памяти. Часто используют как кэш второго уровня в веб-приложениях, для сессий, rate limiting, очередей с коротким TTL и т.д., чтобы снизить нагрузку на основную БД.
</b></details>

<details>
<summary>Что такое Amazon Aurora?</summary><br><b>

Совместимые с **MySQL** и **PostgreSQL** облачные движки от AWS с автоматическим хранением в распределённом кластере, быстрыми failover и удобными бэкапами. Часто предлагается как «движок по умолчанию» при создании БД в RDS для новых проектов.
</b></details>

<details>
<summary>Что такое Amazon DocumentDB?</summary><br><b>

«Управляемая документная БД с **совместимостью с MongoDB** для JSON-документов, индексов и запросов».

Подробнее: [Amazon DocumentDB](https://aws.amazon.com/documentdb)
</b></details>

<details>
<summary>Для чего нужен AWS Database Migration Service (DMS)?</summary><br><b>

Сервис **миграции и непрерывной репликации** между гетерогенными источниками и целями (on-prem → AWS, облако → облако, смена движка) с минимизацией простоя при корректной архитектуре CDC.
</b></details>

<details>
<summary>Какое хранилище использует Amazon RDS под капотом?</summary><br><b>

Данные инстанса RDS размещаются на **Amazon EBS** (тома привязаны к AZ; см. документацию по типам хранения RDS).
</b></details>

<details>
<summary>Что такое Read Replicas в Amazon RDS?</summary><br><b>

«**Реплики чтения** снимают нагрузку чтения с основного инстанса, масштабируют чтение горизонтально и могут участвовать в DR-сценариях (в т.ч. промоут в standalone — по правилам движка)».

Подробнее: [Read Replicas](https://aws.amazon.com/rds/features/read-replicas)
</b></details>

#### Бессерверные вычисления

<details>
<summary>Что такое AWS Lambda?</summary><br><b>

«Lambda запускает код без выделения серверов; плата за фактическое время выполнения и число запросов».

Подробнее: [AWS Lambda](https://aws.amazon.com/lambda)
</b></details>

<details>
<summary>Верно или нет? За Lambda платят, пока «существует» функция, даже если она не вызывается</summary><br><b>

Неверно. Оплата за **вызовы**, **GB-секунды** (и связанные метрики вроде провижининга для Lambda с выделением); простое существование функции само по себе не тарифицируется как постоянный сервер.
</b></details>

<details>
<summary>Какой из наборов языков поддерживает Lambda?

  * R, Swift, Rust, Kotlin
  * Python, Ruby, Go
  * Python, Ruby, PHP</summary><br><b>

**Python, Ruby, Go** — из перечисленных это корректный ответ в духе материала; фактический список рантаймов обновляется в документации AWS.
</b></details>

#### Подберите сервис или инструмент

<details>
<summary>Чем автоматизировать выкладку кода на инстансы/контейнеры/Lambda?</summary><br><b>

**AWS CodeDeploy**
</b></details>

<details>
<summary>Чем удобно создавать повторяемые однотипные стеки ресурсов для разных заказчиков?</summary><br><b>

**AWS CloudFormation** (или **AWS CDK**, но в классическом ответе — CloudFormation)
</b></details>

<details>
<summary>Какой сервис выбрать для простого веб-сайта или небольшого веб-приложения «всё включено»?</summary><br><b>

**Amazon Lightsail** или **AWS Elastic Beanstalk** (зависит от требований к контролю и масштабированию).
</b></details>

<details>
<summary>Какой инструмент помогает сравнивать стоимость Reserved и On-Demand?</summary><br><b>

**AWS Cost Explorer**
</b></details>

<details>
<summary>Как проверить, сколько у вас неассоциированных Elastic IP?</summary><br><b>

**AWS Trusted Advisor** (или отчёты **Cost Optimization Hub** / собственные скрипты, но в ответе курса — Trusted Advisor).
</b></details>

<details>
<summary>Какой сервис для переноса петабайт данных в/из AWS физическими устройствами?</summary><br><b>

**AWS Snowball** / семейство **Snow** (Snowcone, Snowball Edge; для экстремальных объёмов — Snowmobile).
</b></details>

<details>
<summary>Что даёт изолированную виртуальную сеть в аккаунте AWS?</summary><br><b>

**Amazon VPC**
</b></details>

<details>
<summary>Что выбрать для приложения с MySQL и автоматическими бэкапами «из коробки»?</summary><br><b>

**Amazon Aurora** (часто через **Amazon RDS**)
</b></details>

<details>
<summary>Чем мигрировать on-prem БД в AWS?</summary><br><b>

**AWS Database Migration Service (DMS)**
</b></details>

<details>
<summary>Где смотреть, кто и почему завершил инстансы EC2?</summary><br><b>

**AWS CloudTrail** (+ **CloudWatch Events/EventBridge** для алертов)
</b></details>

<details>
<summary>Какая управляемая SQL-база «по умолчанию» в ответах курса?</summary><br><b>

**Amazon RDS**
</b></details>

<details>
<summary>Какая управляемая NoSQL БД для ключ-значение/документов?</summary><br><b>

**Amazon DynamoDB**
</b></details>

<details>
<summary>Чем выполнять ad-hoc SQL по данным в S3?</summary><br><b>

**Amazon Athena**
</b></details>

<details>
<summary>Чем добавить распознавание образов/видео в приложение?</summary><br><b>

**Amazon Rekognition**
</b></details>

<details>
<summary>Чем трассировать запросы в микросервисах и искать узкие места?</summary><br><b>

**AWS X-Ray**
</b></details>

<details>
<summary>Какой сервис для push/SMS/email уведомлений?</summary><br><b>

**Amazon SNS**
</b></details>

<details>
<summary>Кто ищет вредоносную активность по логам аккаунта?</summary><br><b>

**Amazon GuardDuty**
</b></details>

<details>
<summary>Как централизовать биллинг и политики для нескольких аккаунтов?</summary><br><b>

**AWS Organizations** (+ **Control Tower** в зрелых средах)
</b></details>

<details>
<summary>Чем защитить веб-приложение на уровне L7?</summary><br><b>

**AWS WAF**
</b></details>

<details>
<summary>Как мониторить метрики разных сервисов и алертиться?</summary><br><b>

**Amazon CloudWatch**
</b></details>

<details>
<summary>Какой сервис для автоматической оценки уязвимостей (контейнеры/хосты — по продукту)?</summary><br><b>

**Amazon Inspector**
</b></details>

<details>
<summary>Какой сервис для DNS-записей?</summary><br><b>

**Amazon Route 53**
</b></details>

<details>
<summary>Какая управляемая документная БД с совместимостью с MongoDB API?</summary><br><b>

**Amazon DocumentDB**
</b></details>

<details>
<summary>Как добавить регистрацию/вход пользователей в приложение?</summary><br><b>

**Amazon Cognito**
</b></details>

<details>
<summary>Какая управляемая очередь сообщений?</summary><br><b>

**Amazon SQS**
</b></details>

<details>
<summary>Какая управляемая защита от DDoS?</summary><br><b>

**AWS Shield**
</b></details>

<details>
<summary>Как кэшировать горячие данные в памяти рядом с приложением?</summary><br><b>

**Amazon ElastiCache**
</b></details>

<details>
<summary>Чем ускорить загрузку в S3 через дальние каналы?</summary><br><b>

**Amazon S3 Transfer Acceleration**
</b></details>

#### Биллинг и поддержка в AWS

<details>
<summary>Что такое AWS Organizations?</summary><br><b>

«**AWS Organizations** помогает централизованно управлять политиками, счетами и ростом среды по мере масштабирования нагрузок в AWS».

Подробнее: [AWS Organizations](https://aws.amazon.com/organizations)
</b></details>

<details>
<summary>Объясните модель ценообразования AWS</summary><br><b>

В основе — **оплата по факту использования** (pay-as-you-go): платите за ресурсы, которые реально потребляете, в период их работы.

Примеры: в **S3** — объём хранения, класс хранения, запросы (GET/PUT/Lifecycle и т.д.); в **EC2** — модель закупки (On-Demand, Reserved, Spot и др.), тип инстанса, ОС/лицензии, регион и доп. сервисы (EBS, трафик).

Обзор: [AWS Pricing](https://aws.amazon.com/pricing)
</b></details>

<details>
<summary>Как оценить стоимость AWS при сравнении с on-prem?</summary><br><b>

* **Migration Evaluator** / **AWS Pricing Calculator** для прогноза облачных затрат  
* **TCO Calculator** (где применимо) для сопоставления с капексом/опексом on-prem  
* **Cost Explorer** и отчёты **Cost & Usage** для анализа фактических расходов после миграции
</b></details>

<details>
<summary>Что входит в Basic Support в AWS?</summary><br><b>

* Круглосуточный **Customer Service** (биллинг, лимиты аккаунта, общие вопросы)  
* **AWS Personal Health Dashboard** — события, влияющие на ваши ресурсы  
* **Trusted Advisor** — **ограниченный** набор проверок (в отличие от платных планов поддержки)
</b></details>

<details>
<summary>Как тарифицируются инстансы EC2?</summary><br><b>

Обычно **посекундно** (минимум 60 с за запуск On-Demand/Spot в большинстве регионов) за **вычислительные** ресурсы + отдельно **EBS**, публичный исходящий трафик, лицензии ПО. **Reserved** и **Savings Plans** дают скидку за обязательство по потреблению/типу использования.
</b></details>

<details>
<summary>Для чего нужен AWS Pricing Calculator?</summary><br><b>

Интерактивная **оценка месячной стоимости** набора сервисов до развёртывания: регион, конфигурации, объёмы данных, сравнение сценариев и экспорт оценки для бизнес-кейса.
</b></details>

<details>
<summary>Что такое Amazon Connect?</summary><br><b>

«Облачный **омниканальный контакт-центр** для голоса, чата и интеграций с CRM с оплатой по использованию».

Подробнее: [Amazon Connect](https://aws.amazon.com/connect)
</b></details>

<details>
<summary>Кто такие APN Consulting Partners?</summary><br><b>

«Партнёры-консультанты **AWS Partner Network** — профессиональные сервисные компании, которые помогают проектировать, строить, мигрировать и сопровождать нагрузки в AWS».

Подробнее: [APN Consulting](https://aws.amazon.com/partners/consulting)
</b></details>

<details>
<summary>Какие из перечисленных — **планы поддержки** AWS (в порядке возрастания возможностей)?

  * Basic, Developer, Business, Enterprise
  * Newbie, Intermediate, Pro, Enterprise
  * Developer, Basic, Business, Enterprise
  * Beginner, Pro, Intermediate Enterprise</summary><br><b>

**Basic, Developer, Business, Enterprise**
</b></details>

<details>
<summary>Верно или нет? Регион влияет на цену EC2</summary><br><b>

Верно. Тарифы за час/секунду и связанные сервисы **зависят от региона**.
</b></details>

<details>
<summary>Что такое AWS Infrastructure Event Management?</summary><br><b>

«Структурированная программа для **Enterprise Support** (и **Business** за доп. плату), помогающая спланировать крупные события: запуск продукта, миграция, маркетинговые пики нагрузки».
</b></details>

#### Автоматизация в AWS

<details>
<summary>Что такое AWS CodeDeploy?</summary><br><b>

«Полностью управляемый сервис **развёртывания** кода на EC2, Lambda, ECS и on-prem агентах с поэтапными стратегиями».

Подробнее: [AWS CodeDeploy](https://aws.amazon.com/codedeploy)
</b></details>

<details>
<summary>Что такое AWS CloudFormation?</summary><br><b>

**IaC**: декларативное описание стека ресурсов AWS (JSON/YAML), версионирование, откаты изменений, **Drift detection**, интеграция с конвейерами. Альтернатива в том же духе — **AWS CDK** (генерация шаблонов из кода).
</b></details>

#### Прочие сервисы и инструменты AWS

<details>
<summary>Что такое Amazon Lightsail?</summary><br><b>

«Простая платформа **фиксированной цены в месяц** для сайтов и небольших приложений (ВМ, БД, балансировщики, статика) с предсказуемым счётом».
</b></details>

<details>
<summary>Что такое Amazon Rekognition?</summary><br><b>

«Сервис **анализа изображений и видео** (детекция объектов, лица, модерация контента и др.) на управляемых ML-моделях без собственного обучения».

Подробнее: [Amazon Rekognition](https://aws.amazon.com/rekognition)
</b></details>

<details>
<summary>Для чего нужны AWS Resource Groups?</summary><br><b>

«**Группы ресурсов** объединяют связанные ресурсы по тегам/запросам для массовых операций, отчётов и автоматизации».

Документация: [Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
</b></details>

<details>
<summary>Что такое AWS Global Accelerator?</summary><br><b>

«Сервис с **статическими anycast IP** и маршрутизацией трафика по глобальной сети AWS к ближайшим здоровым эндпоинтам для снижения задержек и повышения отказоустойчивости».

Подробнее: [Global Accelerator](https://aws.amazon.com/global-accelerator)
</b></details>

<details>
<summary>Что такое AWS Config?</summary><br><b>

«**Инвентаризация и аудит конфигураций** ресурсов: снимки состояния, правила соответствия, история изменений».

Подробнее: [AWS Config](https://aws.amazon.com/config)
</b></details>

<details>
<summary>Что такое AWS X-Ray?</summary><br><b>

«Сервис **распределённой трассировки** для анализа задержек и ошибок в микросервисах».

Подробнее: [AWS X-Ray](https://aws.amazon.com/xray)
</b></details>

<details>
<summary>Что такое AWS OpsWorks?</summary><br><b>

«Управляемый **Chef/Puppet** для конфигурации стеков приложений (legacy-сценарии; для новых проектов чаще смотрят Systems Manager / контейнеры)».

Подробнее: [AWS OpsWorks](https://aws.amazon.com/opsworks)
</b></details>

<details>
<summary>Что такое AWS Service Catalog?</summary><br><b>

«Каталог **утверждённых IT-услуг** (шаблоны CloudFormation), который конечные пользователи могут заказывать в рамках политик организации».

Подробнее: [Service Catalog](https://aws.amazon.com/servicecatalog)
</b></details>

<details>
<summary>Что такое AWS CAF?</summary><br><b>

«**Cloud Adoption Framework** — методология и перспективы (бизнес, люди, говернанс, платформа, безопасность, операции) для ускоренной и контролируемой миграции в облако».

Подробнее: [AWS CAF](https://aws.amazon.com/professional-services/CAF)
</b></details>

<details>
<summary>Что такое AWS Cloud9?</summary><br><b>

«Облачная **IDE** в браузере для написания, запуска и отладки кода с совместной работой».
</b></details>

<details>
<summary>Что такое AWS Application Discovery Service?</summary><br><b>

«Сбор данных об **on-prem инфраструктуре** (агенты/безагентно) для планирования миграции в AWS Migration Hub».

Подробнее: [Application Discovery Service](https://aws.amazon.com/application-discovery)
</b></details>

<details>
<summary>Что такое AWS Trusted Advisor?</summary><br><b>

Автоматические **рекомендации по оптимизации**: безопасность, отказоустойчивость, производительность, лимиты сервисов, экономия. Полный набор проверок доступен на **Business/Enterprise** поддержке.
</b></details>

<details>
<summary>Что такое AWS Well-Architected Framework и на каких столпах он основан?</summary><br><b>

«Руководство для архитекторов по построению **безопасной, устойчивой и эффективной** облачной системы. Пять столпов: **операционное совершенство, безопасность, надёжность, эффективность производительности, оптимизация затрат**» (плюс столп **устойчивое развитие** в актуальных версиях Lens).

Подробнее: [Well-Architected](https://aws.amazon.com/architecture/well-architected)
</b></details>

<details>
<summary>Какие сервисы AWS считаются бессерверными (или имеют бессерверный режим)?</summary><br><b>

Примеры: **AWS Lambda**, **Amazon Athena**, **Amazon API Gateway**, **Amazon DynamoDB**, **Amazon S3** (как управляемое хранилище без серверов), **AWS Step Functions**, **Amazon EventBridge**, **AWS Fargate** (бессерверные контейнеры).
</b></details>

<details>
<summary>Что такое Amazon EMR?</summary><br><b>

«Управляемый **big data** кластер для Spark, Hive, HBase, Flink, Presto и др. с масштабированием под пакетную и потоковую обработку».

Подробнее: [Amazon EMR](https://aws.amazon.com/emr)
</b></details>

<details>
<summary>Что такое Amazon Athena?</summary><br><b>

«**Интерактивный SQL** поверх данных в **Amazon S3** (табличный каталог в Glue), оплата за объём просканированных данных».

Подробнее: [Amazon Athena](https://aws.amazon.com/athena)
</b></details>

<details>
<summary>Что такое Amazon Cloud Directory?</summary><br><b>

«Высокодоступное **иерархическое хранилище объектов** с гибкой схемой связей (не LDAP AD Replacement; для каталогов приложений)».

Документация: [Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
</b></details>

<details>
<summary>Что такое AWS Elastic Beanstalk?</summary><br><b>

«PaaS для **развёртывания веб-приложений**: загружаете артефакт — платформа поднимает EC2, балансировщик, автоскейлинг по политикам; вы сохраняете контроль над базой (EC2) при желании».

Подробнее: [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk)
</b></details>

<details>
<summary>Что такое Amazon SWF?</summary><br><b>

«**Simple Workflow** — координация фоновых задач с шагами, состоянием и воркерами (legacy; для новых систем чаще **Step Functions** + SQS/Lambda)».

Подробнее: [Amazon SWF](https://aws.amazon.com/swf)
</b></details>

<details>
<summary>Что такое Amazon Simple Queue Service (SQS)?</summary><br><b>

«Полностью управляемая **очередь сообщений** для развязки микросервисов, пакетной обработки и паттернов буферизации».

Подробнее: [Amazon SQS](https://aws.amazon.com/sqs)
</b></details>

#### Аварийное восстановление (DR) в AWS

<details>
<summary>Что такое RTO и RPO в контексте DR?</summary><br><b>

**RTO (Recovery Time Objective)** — максимально допустимое время **простоя** сервиса после аварии.  
**RPO (Recovery Point Objective)** — максимально допустимый **интервал потери данных** (насколько «старым» может быть последний восстановимый снимок/реплика).
</b></details>

<details>
<summary>Какие типовые стратегии DR на AWS?</summary><br><b>

* **Backup & Restore («холодный»)** — периодические бэкапы, восстановление в новый регион/AZ по требованию  
* **Pilot Light** — минимальный живой контур + быстрое масштабирование прод-стека  
* **Warm Standby** — уменьшенная копия прод-среды, готовая к масштабированию  
* **Active-Active / Multi-Site** — полноценные параллельные площадки с постоянным трафиком
</b></details>

<details>
<summary>У какой стратегии DR обычно самый большой простой, а у какой — наименьший?</summary><br><b>

**Наименьший простой** — **Active-Active / Multi-Site**.  
**Наибольший** — **холодный** сценарий **backup & restore** (дольше RTO/RPO без непрерывной репликации).
</b></details>

### Итог

Удачи на экзамене — у вас получится.
