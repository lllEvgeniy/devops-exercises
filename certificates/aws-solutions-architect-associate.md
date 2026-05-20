## AWS — Solutions Architect Associate

Последнее обновление материала: 2021

#### Глобальная инфраструктура AWS

<details>
<summary>Объясните следующие понятия

  * Зона доступности (Availability Zone)
  * Регион (Region)
  * Пограничная точка (Edge location)</summary><br><b>

**Регионы AWS** — географически разделённые области с несколькими изолированными зонами доступности; регионы независимы друг от друга по умолчанию.<br>

Внутри региона — несколько **зон доступности (AZ)**: изолированные площадки с собственной электросетью и сетью; несколько AZ дают отказоустойчивость при сбое одной зоны.<br>

**Edge locations** — точки сети доставки контента (CDN), кэшируют контент ближе к пользователям для меньшей задержки; обычно в крупных городах по всему миру.
</b></details>

#### IAM в AWS

<details>
<summary>Что такое IAM? Какие у него возможности?</summary><br><b>

Полное описание: [AWS IAM](https://aws.amazon.com/iam)  
Кратко: управление **пользователями**, **группами**, **политиками** доступа и **ролями** (в т.ч. для сервисов и федерации).
</b></details>

<details>
<summary>Верно или нет? Конфигурация IAM глобальная, а не привязанная к региону</summary><br><b>

Верно. IAM — глобальный сервис в пределах аккаунта.
</b></details>

<details>
<summary>Верно или нет? При создании аккаунта AWS по умолчанию создаётся root; это рекомендуемая учётная запись для повседневной работы и «шаринга» в организации</summary><br><b>

Неверно. Root использовать только для редких админ-операций; для работы создают IAM-пользователей/роли и принцип наименьших привилегий.
</b></details>

<details>
<summary>Верно или нет? Группы в IAM могут содержать только пользователей, но не другие группы</summary><br><b>

Верно. Вложенных групп в IAM нет.
</b></details>

<details>
<summary>Верно или нет? Пользователь IAM может состоять только в одной группе</summary><br><b>

Неверно. Пользователь может входить в **несколько** групп; эффективные права складываются из политик всех групп и прикреплённых к пользователю политик.
</b></details>

<details>
<summary>Что такое роли (Roles)?</summary><br><b>

Способ **делегировать** права сервису или субъекту без долгоживущих ключей на ресурсе: роль **прикрепляют** к EC2, Lambda, ECS и т.д., а в политике роли разрешают, например, чтение/запись в **S3**.
</b></details>

<details>
<summary>Что такое политики (Policies)?</summary><br><b>

Документы (обычно **JSON**), описывающие, **какие действия** с какими ресурсами разрешены или запрещены для пользователя, группы или роли.
</b></details>

<details>
<summary>Пользователь не может обратиться к бакету S3. В чём может быть причина?</summary><br><b>

Типичные причины: нет нужной **IAM-политики** (или есть **Deny**), конфликт с **bucket policy**, **ACL** (если используются), блокировки публичного доступа, неверный **ключ объекта**, запрет **VPC endpoint**/сети, **KMS** отказывает в расшифровке. Админ проверяет эффективные разрешения (IAM + bucket policy) и исправляет политику.
</b></details>

<details>
<summary>Чем воспользоваться, чтобы:

  * выдать доступ **между сервисами/ресурсами**?
  * выдать **пользователю** доступ к ресурсам/сервисам?</summary><br><b>

  * **Роль** (часто для сервис-к-сервису и EC2/Lambda)
  * **Политика** (прямо к пользователю/группе или к роли)
</b></details>

<details>
<summary>Какие права у только что созданного пользователя IAM?</summary><br><b>

По умолчанию — **нет** прав на API ресурсов; может быть только возможность **войти в консоль** (если задан пароль) до прикрепления политик.
</b></details>


#### Сеть в AWS

<details>
<summary>Что такое VPC?</summary><br><b>

«Логически изолированный участок облака AWS, в котором вы запускаете ресурсы в **определяемой вами** виртуальной сети».  
Подробнее: [Amazon VPC](https://aws.amazon.com/vpc).
</b></details>

<details>
<summary>Верно или нет? Одна VPC охватывает несколько регионов</summary><br><b>

Неверно. VPC привязана к **одному** региону.
</b></details>

<details>
<summary>Верно или нет? Подсети одной VPC могут находиться в разных зонах доступности</summary><br><b>

Верно. При этом **одна** подсеть целиком лежит в **одной** AZ.
</b></details>

<details>
<summary>Что такое Internet Gateway?</summary><br><b>

Компонент, обеспечивающий **двустороннюю** связь инстансов в VPC с **интернетом** (маршрутизация 0.0.0.0/0 → IGW).  
Документация: [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
</b></details>

<details>
<summary>Верно или нет? NACL разрешают или запрещают трафик на уровне подсети</summary><br><b>

Верно. Списки ACL — **stateless**, порядок правил и явные разрешения/запреты по подсети.
</b></details>

<details>
<summary>Верно или нет? К одной VPC можно подключить несколько Internet Gateway</summary><br><b>

Неверно. К VPC обычно подключают **один** Internet Gateway (на VPC).
</b></details>

<details>
<summary>Верно или нет? Таблицы маршрутизации служат для разрешения или запрета трафика из интернета к инстансам AWS</summary><br><b>

Неверно. Route tables задают **куда** направлять пакеты (IGW, NAT, VPC peering, TGW и т.д.). Разрешение/запрет трафика к инстансу — это **security groups** и **NACL**.
</b></details>

<details>
<summary>Объясните Security Groups и Network ACL</summary><br><b>

* **NACL** — контроль на уровне **подсети**, stateless, нумерованные правила.  
* **Security Group** — виртуальный **файрвол на уровне ENI/ресурса**, stateful, только разрешающие правила (явный deny через NACL или политики).

Подробнее: [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html), [NACL](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
</b></details>

<details>
<summary>Что такое AWS Direct Connect?</summary><br><b>

Выделенное или партнёрское **приватное** соединение между вашей корпоративной сетью и AWS (ниже джиттер/стабильнее, чем чистый интернет-VPN для больших объёмов).
</b></details>

#### Вычисления в AWS

<details>
<summary>Что такое EC2?</summary><br><b>

«Веб-сервис, предоставляющий **безопасные, изменяемые по размеру** вычислительные мощности в облаке».  
Подробнее: [Amazon EC2](https://aws.amazon.com/ec2)
</b></details>

<details>
<summary>Верно или нет? EC2 — региональный сервис</summary><br><b>

Верно. Ресурсы EC2 и AMI привязаны к региону (в отличие от IAM, который глобален в аккаунте).
</b></details>

<details>
<summary>Что такое AMI?</summary><br><b>

**Amazon Machine Image** — образ с ОС, ПО и настройками, по которому **запускают** инстанс EC2.  
Документация: [AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
</b></details>

<details>
<summary>Какие бывают источники AMI?</summary><br><b>

* **Свои AMI** — созданные вами  
* **AWS Marketplace** — платные/лицензированные образы с ПО  
* **Community AMI** — общедоступные образы сообщества
</b></details>

<details>
<summary>Что такое тип инстанса (instance type)?</summary><br><b>

«Тип инстанса определяет **аппаратную конфигурацию** хоста (vCPU, память, сеть, локальные SSD и т.д.)».  
Справочник: [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
</b></details>

<details>
<summary>Верно или нет? Из перечисленных типы инстансов в AWS доступны пользователю:

  * вычислительно оптимизированные (compute optimized)
  * сетево оптимизированные (network optimized)
  * веб-оптимизированные (web optimized)</summary><br><b>

Неверно. Из списка как отдельное семейство в духе вопроса корректно **compute optimized**; «web optimized» как официального семейства нет; сетевые характеристики — у многих семейств (например network-intensive варианты).
</b></details>

<details>
<summary>Что такое EBS?</summary><br><b>

«**Блочные** тома хранения для EC2; ведут себя как сырые блочные устройства».  
Подробнее: [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
</b></details>

<details>
<summary>Какие модели оплаты за EC2 существуют?</summary><br><b>

**On-Demand** — почасовая/посекундная оплата без обязательств, гибко старт/стоп.  
**Reserved Instances / Savings Plans** — скидка за **обязательство** по использованию/типу.  
**Spot** — скидка за использование **избыточной** мощности; инстанс могут забрать при нехватке.  
**Dedicated Hosts** — выделенный **физический** сервер под ваши лицензии BYOL и изоляцию.
</b></details>

<details>
<summary>Что такое security groups?</summary><br><b>

«Виртуальный **файрвол** на уровне инстанса/ENI: разрешающие правила для входящего/исходящего трафика».  
Подробнее: [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
</b></details>

<details>
<summary>Что можно подключить к EC2 для хранения данных?</summary><br><b>

**Amazon EBS** (тома), при необходимости **instance store** (локальный эфемерный диск на хосте), **EFS** по NFS.
</b></details>

<details>
<summary>Какие типы Reserved Instances для EC2 бывают?</summary><br><b>

**Standard RI** — максимальная скидка при фиксированных атрибутах (семейство, регион, tenancy).  
**Convertible RI** — меньшая скидка, но можно **менять** атрибуты в рамках правил.  
**Scheduled RI** — резерв мощности в **заданных окнах** времени.

Подробнее: [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances)
</b></details>

#### Контейнеры в AWS

<details>
<summary>Что такое Amazon ECS?</summary><br><b>

«Полностью управляемая **оркестрация контейнеров** для запуска Docker на EC2 или Fargate с интеграцией в VPC, балансировщики и секреты».

Подробнее: [Amazon ECS](https://aws.amazon.com/ecs)
</b></details>

<details>
<summary>Что такое Amazon ECR?</summary><br><b>

«Управляемый **реестр образов** контейнеров с интеграцией в ECS/EKS и сканированием образов».

Подробнее: [Amazon ECR](https://aws.amazon.com/ecr)
</b></details>

<details>
<summary>Что такое AWS Fargate?</summary><br><b>

«**Бессерверный** движок запуска контейнеров для **ECS** и **EKS** без управления хостами EC2».

Подробнее: [AWS Fargate](https://aws.amazon.com/fargate)
</b></details>

#### Хранение в AWS

<details>
<summary>Что такое Amazon S3?</summary><br><b>

**S3** — Simple Storage Service: **объектное** хранилище с высокой масштабируемостью и долговечностью; объекты до **5 TiB** на ключ (в пределах лимитов сервиса).

Подробнее: [Amazon S3](https://aws.amazon.com/s3)
</b></details>

<details>
<summary>Что такое бакет (bucket)?</summary><br><b>

**Бакет** — контейнер верхнего уровня в регионе/конфигурации; внутри — **объекты** (данные + метаданные). Префиксы «как папки» — часть **ключа** объекта, отдельной иерархии папок S3 не создаёт.
</b></details>

<details>
<summary>Верно или нет? Имя бакета должно быть глобально уникальным</summary><br><b>

Верно (в пределах партиции DNS-имён S3; стандартный стиль — глобально уникальное DNS-совместимое имя).
</b></details>

<details>
<summary>«Папки» и объекты в контексте бакета</summary><br><b>

* **Префикс («папка»)** — логическое группирование по общему началу **ключа** объекта.  
* **Объект** — единица хранения: тело, метаданные, ключ, версия (если включено версионирование).
</b></details>

<details>
<summary>Объясните следующее:

  * жизненный цикл объектов (Lifecycle)
  * совместный доступ к объектам (Sharing)
  * версионирование объектов (Versioning)</summary><br><b>

  * **Lifecycle** — автоматические переходы между классами хранения, удаление по правилам времени/префикса.  
  * **Sharing** — выдача доступа через **подписанный URL** (presigned), политики бакета, CloudFront **OAC/OAI**.  
  * **Versioning** — хранение нескольких версий одного ключа; защита от перезаписи/удаления (в связке с MFA Delete и политиками).
</b></details>

<details>
<summary>Долговечность (Durability) и доступность (Availability) объекта в S3</summary><br><b>

**Долговечность** — насколько маловероятна **потеря** объекта за год (для Regional классов — крайне высокая, порядка **одиннадцати девяток** для Standard).  
**Доступность** — доля времени, когда сервис **отвечает** на запросы по SLA класса (для Standard-IA и др. — свои целевые проценты; см. актуальную документацию S3).
</b></details>

<details>
<summary>Что такое класс хранения? Какие классы бывают?</summary><br><b>

У каждого объекта есть **класс хранения** — влияет на **стоимость**, **SLA доступности** и **время/стоимость выборки** (для архивных).

Основные идеи (актуализируйте по документации AWS):
  * **S3 Standard** — частый доступ, максимальная доступность среди «горячих», высокая долговечность, класс по умолчанию.  
  * **Standard-IA** — редкий доступ, но при обращении нужна **мгновенная** выборка; ниже цена хранения, выше плата за retrieval.  
  * **One Zone-IA** — дешевле, данные в **одной** AZ (ниже устойчивость к катастрофе AZ).  
  * **Intelligent-Tiering** — автоматический перенос между тирами по паттерну доступа (плата за мониторинг тира).  
  * **Glacier Instant Retrieval / Flexible / Deep Archive** — архивные уровни с разными **окнами и ценой** восстановления.

Обзор классов: [S3 storage classes](https://aws.amazon.com/s3/storage-classes)

</b></details>

<details>
<summary>Клиент хочет перевести редко читаемые данные из Standard в **самый дешёвый** класс. Что выбрать из списка?

  * One Zone-IA
  * Glacier Deep Archive
  * Intelligent-Tiering</summary><br><b>

**S3 Glacier Deep Archive** — минимальная цена хранения при самых длинных/дорогих сценариях выборки среди перечисленных.
</b></details>

<details>
<summary>Какие режимы выборки (retrieval) бывают у Glacier?</summary><br><b>

**Expedited**, **Standard**, **Bulk** (для классических Glacier; у **Flexible/Deep Archive** — свои профили времени и цены — сверяйте с документацией).
</b></details>

<details>
<summary>Верно или нет? В аккаунте AWS жёсткий лимит 500 ПБ; сверх — плата удваивается</summary><br><b>

Неверно. Практически **без жёсткого потолка** по объёму; стоимость считается по тарифам, а не «удвоением после 500 ПБ».
</b></details>

<details>
<summary>Что такое AWS Storage Gateway?</summary><br><b>

«Гибридный сервис: **on-prem шлюз** к практически неограниченному облачному хранилищу (файлы, тома, лента)».  
Подробнее: [Storage Gateway](https://aws.amazon.com/storagegateway)
</b></details>

<details>
<summary>Типы развёртывания Storage Gateway

  * File Gateway
  * Volume Gateway
  * Tape Gateway</summary><br><b>

Кратко: **File** — NFS/SMB в S3; **Volume** — блочные тома iSCSI с бэкапом в облако (stored/cached); **Tape** — виртуальная лента в Glacier/Deep Archive.  
Подробнее: [Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs)
</b></details>

<details>
<summary>Чем stored volumes отличаются от cached volumes?</summary><br><b>

**Stored** — основной набор данных **on-prem**, в облако асинхронно снимаются снапшоты.  
**Cached** — полный набор в **облаке**, на площадке кэшируется «горячий» поднабор для быстрого локального доступа.
</b></details>

<details>
<summary>Что такое Amazon S3 Transfer Acceleration?</summary><br><b>

«Ускорение загрузки/скачивания в S3 за счёт входа в сеть CloudFront **ближе к клиенту** и дальнейшей доставки по магистрали AWS».

Документация: [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)
</b></details>

<details>
<summary>Что такое Amazon EFS?</summary><br><b>

«Управляемая **NFS** файловая система, растущая по мере записи; для Linux-инстансов, контейнеров и гибридных сценариев».

Подробнее: [Amazon EFS](https://aws.amazon.com/efs)
</b></details>

<details>
<summary>Что такое AWS Snowmobile?</summary><br><b>

«Перенос **эксабайтных** объёмов физическим **транспортом** (контейнер с хранилищем) в дата-центр AWS».

Подробнее: [AWS Snowmobile](https://aws.amazon.com/snowmobile)
</b></details>

##### Elastic Load Balancing (ELB)

<details>
<summary>Что такое ELB (Elastic Load Balancing)?</summary><br><b>

«Распределяет входящий трафик по целям: EC2, IP, Lambda, контейнеры в целевых группах».

Подробнее: [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing)
</b></details>

<details>
<summary>Что такое Auto Scaling?</summary><br><b>

«Сервисы масштабирования (в т.ч. **EC2 Auto Scaling** и **Application Auto Scaling**) подстраивают ёмкость по метрикам/расписанию, чтобы держать производительность и экономить».

Подробнее: [AWS Auto Scaling](https://aws.amazon.com/autoscaling)
</b></details>

<details>
<summary>Верно или нет? Auto Scaling только добавляет ресурсы, но никогда их не убирает</summary><br><b>

Неверно. Политики **scale-in** уменьшают число инстансов/единиц ёмкости при снижении нагрузки (если не запрещено защитой от сбоев/хуками).
</b></details>

<details>
<summary>Какие типы балансировщиков нагрузки поддерживаются и для чего они?</summary><br><b>

  * **Application Load Balancer** — HTTP/HTTPS, маршрутизация L7, WebSocket.  
  * **Network Load Balancer** — TCP/UDP, низкая задержка, высокая пропускная способность, **статические IP** на AZ.  
  * **Classic Load Balancer** — устаревший вариант L4/L7; для новых архитектур предпочтительны ALB/NLB.
</b></details>

#### DNS в AWS

<details>
<summary>Что такое Route 53?</summary><br><b>

«Высокодоступный масштабируемый **DNS** и регистрация доменов в AWS».  
Возможности: регистрация домена, публичные/приватные зоны, **маршрутизация** (latency, geo, weighted, failover), **проверки здоровья**.

Подробнее: [Route 53](https://aws.amazon.com/route53)
</b></details>

#### Amazon CloudFront

<details>
<summary>Что такое CloudFront?</summary><br><b>

«**CDN**: доставка статики, видео, API и приложений с **edge locations** с низкой задержкой».

Подробнее: [Amazon CloudFront](https://aws.amazon.com/cloudfront)
</b></details>

<details>
<summary>Объясните термины

  * Origin
  * Edge location
  * Distribution</summary><br><b>

* **Origin** — источник контента (S3, ALB/API Gateway, произвольный HTTP-сервер), откуда edge забирает объекты при промахе кэша.  
* **Edge location** — пограничная точка кэширования и TLS-ближе к пользователю.  
* **Distribution** — конфигурация CDN: источники, поведения (cache policy), сертификаты, WAF, цены/регионы edge.
</b></details>

#### Мониторинг и журналы

<details>
<summary>Что такое Amazon CloudWatch?</summary><br><b>

«**Метрики**, **алерты**, **логи** (CloudWatch Logs), дашборды и интеграции с сервисами для наблюдаемости».

Подробнее: [CloudWatch](https://aws.amazon.com/cloudwatch)
</b></details>

<details>
<summary>Что такое AWS CloudTrail?</summary><br><b>

«Журнал **API-вызовов** в аккаунте для аудита, расследований и соответствия требованиям».

Подробнее: [CloudTrail](https://aws.amazon.com/cloudtrail)
</b></details>

<details>
<summary>Что такое Amazon SNS (Simple Notification Service)?</summary><br><b>

«Надёжный управляемый **pub/sub**: темы, подписки на HTTP/S, email, SMS, SQS, Lambda и др. для развязки микросервисов».

Подробнее: [Amazon SNS](https://aws.amazon.com/sns)
</b></details>

<details>
<summary>Объясните в контексте SNS:

  * Topics
  * Subscribers
  * Publishers</summary><br><b>

  * **Topic** — именованный канал; в него публикуют сообщения, от него рассылают подписчикам.  
  * **Subscriber** — конечная точка подписки (очередь, Lambda, email и т.д.).  
  * **Publisher** — сервис или приложение, которое **публикует** событие в тему.
</b></details>

#### Безопасность в AWS

<details>
<summary>Что такое модель общей ответственности (shared responsibility)? За что отвечает AWS, а за что — клиент?</summary><br><b>

Модель разделяет зоны ответственности: **AWS** отвечает за **безопасность облака** (физика, виртуализация, сеть ЦОД, патчи гипервизора и т.д.), **клиент** — за **безопасность в облаке** (данные, IAM, шифрование, конфигурация VPC/SG, патчи гостевой ОС на EC2 и т.д.).

Подробнее: [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Верно или нет? По модели общей ответственности Amazon отвечает за физические CPU и за security groups на инстансах</summary><br><b>

Неверно. За **железо** в ЦОД и базовую инфраструктуру отвечает AWS; **security groups** создаёт и настраивает **клиент**.
</b></details>

<details>
<summary>Что такое «Shared Controls» в модели общей ответственности?</summary><br><b>

«Контроли применимы и к инфраструктуре AWS, и к слою клиента, но в **разных контекстах**: AWS задаёт требования к платформе, клиент реализует управление в своей конфигурации и использовании сервисов».

Подробнее: [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model)
</b></details>

<details>
<summary>Что такое программа соответствия AWS (compliance program)?</summary><br><b>

Совокупность **аттестаций, отчётов и аудитов** (ISO, PCI-DSS, HIPAA BAA, FedRAMP и др.), подтверждающих контроли на стороне AWS; клиент по-прежнему отвечает за соответствие **своей** архитектуры и данных при использовании сервисов.
</b></details>

<details>
<summary>Что такое AWS Artifact?</summary><br><b>

«Портал для **скачивания** отчётов о безопасности и соответствии (SOC, PCI и др.) и работы с соглашениями AWS».

Подробнее: [AWS Artifact](https://aws.amazon.com/artifact)
</b></details>

<details>
<summary>Что такое Amazon Inspector?</summary><br><b>

«Автоматическая **оценка уязвимостей** и отклонений от практик для **EC2, ECR-образов, Lambda** (в зависимости от поколения продукта)».

Подробнее: [Amazon Inspector](https://aws.amazon.com/inspector)
</b></details>

<details>
<summary>Что такое Amazon GuardDuty?</summary><br><b>

«Сервис **угроз-детекции** по логам CloudTrail, VPC Flow Logs, DNS и др.: аномалии, сканирование, скомпрометированные ключи и т.п.».

Подробнее: [Amazon GuardDuty](https://aws.amazon.com/guardduty)
</b></details>

<details>
<summary>Что такое AWS Shield?</summary><br><b>

«Управляемая защита от **DDoS**: **Standard** включена для всех, **Advanced** — расширенный сервис с поддержкой и интеграцией с WAF/Route 53».
</b></details>

<details>
<summary>Что такое AWS WAF? Пример использования и с чем интегрируется</summary><br><b>

**Web Application Firewall** на уровне L7: правила по IP, геолокации, rate-based, сигнатурам AWS Managed Rules. Подключается к **CloudFront**, **Application Load Balancer**, **API Gateway**. Пример: блокировать SQLi/XSS и ограничивать частоту запросов с одного IP на публичный ALB.
</b></details>

<details>
<summary>Для чего используется AWS VPN?</summary><br><b>

Шифрованный доступ **между** вашей сетью/VPC и on-prem или удалёнными клиентами без публикации сервисов в интернет «в открытую».
</b></details>

<details>
<summary>Чем отличается Site-to-Site VPN от Client VPN?</summary><br><b>

**Site-to-Site VPN** — постоянный **IPsec**-туннель между **маршрутизатором** on-prem и **Virtual Private Gateway / Transit Gateway** в AWS (сеть-сеть).  
**AWS Client VPN** — сервис **удалённого доступа** пользователей (OpenVPN) в VPC с выдачей маршрутов и MFA через IdP.
</b></details>

<details>
<summary>Что такое AWS CloudHSM?</summary><br><b>

«Выделенный **аппаратный** HSM в облаке для генерации и хранения ключей под вашим единоличным контролем (FIPS 140-2 Level 3)».

Подробнее: [AWS CloudHSM](https://aws.amazon.com/cloudhsm)
</b></details>

<details>
<summary>Верно или нет? Amazon Inspector может выполнять и сетевые, и хостовые оценки</summary><br><b>

Верно в духе продукта: **сетевой доступ** (reachability) и **хост/контейнер** (CVE, конфигурации) — по поддерживаемым типам целей и версии Inspector.
</b></details>

<details>
<summary>Что такое AWS Acceptable Use Policy (AUP)?</summary><br><b>

Документ о **запрещённых** способах использования сервисов AWS (спам, взлом, незаконный контент и т.д.).

Подробнее: [AWS AUP](https://aws.amazon.com/aup)
</b></details>

<details>
<summary>Что такое AWS Key Management Service (KMS)?</summary><br><b>

«Создание и управление **CMK**, политики использования ключей, интеграция с S3, EBS, RDS, Secrets Manager и приложениями».

Подробнее: [AWS KMS](https://aws.amazon.com/kms)
</b></details>

<details>
<summary>Верно или нет? Пользователю запрещено проводить penetration testing любых сервисов AWS</summary><br><b>

Неверно. Для ряда сервисов (например **EC2**, **RDS**, **CloudFront**) допустимы тесты **после** соблюдения [политики AWS по пен-тестам](https://aws.amazon.com/security/penetration-testing/) и без вреда третьим сторонам.
</b></details>

<details>
<summary>Верно или нет? DDoS-атака — пример разрешённого penetration testing</summary><br><b>

Неверно. Несанкционированный DDoS **запрещён** и не является легитимным пен-тестом.
</b></details>

<details>
<summary>Верно или нет? AWS Access Key — это тип MFA-устройства</summary><br><b>

Неверно. Access key — **долгоживущие** программные учётные данные; MFA — отдельный второй фактор (TOTP, **U2F/WebAuthn** и т.д.).
</b></details>

<details>
<summary>Что такое Amazon Cognito?</summary><br><b>

«Аутентификация и авторизация пользователей для веб- и мобильных приложений (пулы пользователей, федерация, hosted UI)».

Документация: [Amazon Cognito](https://docs.aws.amazon.com/cognito/index.html)
</b></details>

<details>
<summary>Что такое AWS Certificate Manager (ACM)?</summary><br><b>

«Выдача и **автообновление** публичных и приватных **TLS**-сертификатов для интеграции с ALB, CloudFront, API Gateway и др.».

Подробнее: [AWS Certificate Manager](https://aws.amazon.com/certificate-manager)
</b></details>

#### Базы данных в AWS

<details>
<summary>Что такое Amazon RDS?</summary><br><b>

Управляемые реляционные СУБД (выбор движка), Multi-AZ, бэкапы, патчи, реплики чтения, параметр-группы. Данные на **EBS**.

Документация: [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
</b></details>

<details>
<summary>Что такое Amazon DynamoDB?</summary><br><b>

Полностью управляемая **NoSQL** БД ключ–значение и документов с предсказуемой масштабируемостью и низкой задержкой; глобальные таблицы, потоки, DAX.
</b></details>

<details>
<summary>Что даёт Point-in-Time Recovery (PITR) в DynamoDB?</summary><br><b>

«Непрерывные бэкапы с восстановлением таблицы на произвольную секунду в окне хранения»; также доступны **on-demand** снимки.

Подробнее: [PITR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
</b></details>

<details>
<summary>Что такое Global Tables в DynamoDB?</summary><br><b>

«Набор **реплик** одной логической таблицы в нескольких регионах под одним аккаунтом с многонаправленной репликацией».

Подробнее: [Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
</b></details>

<details>
<summary>Что такое DynamoDB Accelerator (DAX)?</summary><br><b>

«In-memory кэш перед DynamoDB для снижения задержки чтения горячих ключей (микросекунды вместо миллисекунд)».

Подробнее: [Amazon DAX](https://aws.amazon.com/dynamodb/dax)
</b></details>

<details>
<summary>Чем Amazon Redshift отличается от RDS?</summary><br><b>

**Redshift** — **хранилище данных** (OLAP, колонночное) для аналитики на больших объёмах. **RDS** — транзакционные OLTP-сценарии приложений.
</b></details>

<details>
<summary>Что такое Amazon ElastiCache? Типичные сценарии</summary><br><b>

Управляемые **Redis** или **Memcached** в памяти: кэш второго уровня, сессии, rate limiting, снижение нагрузки на основную БД.
</b></details>

<details>
<summary>Что такое Amazon Aurora?</summary><br><b>

Совместимые с **MySQL** и **PostgreSQL** облачные движки с распределённым хранилищем, быстрыми failover и автоматическими бэкапами; часто предлагается при создании БД в RDS.
</b></details>

<details>
<summary>Что такое Amazon DocumentDB?</summary><br><b>

«Управляемая документная БД с **совместимостью с MongoDB** для JSON, индексов и запросов».

Подробнее: [Amazon DocumentDB](https://aws.amazon.com/documentdb)
</b></details>

<details>
<summary>Для чего нужен AWS Database Migration Service (DMS)?</summary><br><b>

Миграция и **репликация изменений** между гетерогенными источниками и целями (on-prem → AWS, смена движка) с минимизацией простоя при корректной архитектуре CDC.
</b></details>

<details>
<summary>Какое хранилище использует Amazon RDS под капотом?</summary><br><b>

**Amazon EBS** (тома в AZ инстанса).
</b></details>

<details>
<summary>Что такое Read Replicas в Amazon RDS?</summary><br><b>

«Реплики **чтения** снимают нагрузку чтения и масштабируют read-heavy нагрузку; могут использоваться в DR при промоуте по правилам движка».

Подробнее: [Read Replicas](https://aws.amazon.com/rds/features/read-replicas)
</b></details>

#### Бессерверные вычисления

<details>
<summary>Что такое AWS Lambda?</summary><br><b>

«Запуск кода без управления серверами; оплата за вызовы и время выполнения».

Подробнее: [AWS Lambda](https://aws.amazon.com/lambda)
</b></details>

<details>
<summary>Верно или нет? За Lambda платят, пока «существует» функция, даже если она не вызывается</summary><br><b>

Неверно. Оплата за **вызовы** и потреблённые **GB-секунды** (и связанные метрики); само существование функции не эквивалентно оплате «как за сервер 24/7».
</b></details>

<details>
<summary>Какой из наборов языков поддерживает Lambda?

  * R, Swift, Rust, Kotlin
  * Python, Ruby, Go
  * Python, Ruby, PHP</summary><br><b>

**Python, Ruby, Go** — из перечисленных это типичный «правильный» ответ в материалах курса; актуальный список рантаймов — в документации AWS.
</b></details>

#### Подберите сервис или инструмент

<details>
<summary>Чем автоматизировать выкладку кода на EC2/Fargate/Lambda/on-prem?</summary><br><b>

**AWS CodeDeploy**
</b></details>

<details>
<summary>Чем удобно создавать повторяемые однотипные стеки для разных заказчиков?</summary><br><b>

**AWS CloudFormation**
</b></details>

<details>
<summary>Какой сервис выбрать для простого сайта или небольшого веб-приложения?</summary><br><b>

**Amazon Lightsail** (в курсе; альтернатива — **Elastic Beanstalk**).
</b></details>

<details>
<summary>Какой инструмент помогает сравнивать стоимость Reserved и On-Demand?</summary><br><b>

**AWS Cost Explorer**
</b></details>

<details>
<summary>Как проверить число неассоциированных Elastic IP?</summary><br><b>

**AWS Trusted Advisor**
</b></details>

<details>
<summary>Какой сервис для переноса петабайт данных в/из AWS физическими устройствами?</summary><br><b>

**AWS Snowball** (семейство **Snow**)
</b></details>

<details>
<summary>Что даёт изолированную виртуальную сеть в аккаунте?</summary><br><b>

**Amazon VPC**
</b></details>

<details>
<summary>Что выбрать для приложения с MySQL и автоматическими бэкапами?</summary><br><b>

**Amazon Aurora** (через **Amazon RDS**)
</b></details>

<details>
<summary>Чем мигрировать on-prem БД в AWS?</summary><br><b>

**AWS Database Migration Service (DMS)**
</b></details>

<details>
<summary>Где смотреть, кто завершил инстансы EC2?</summary><br><b>

**AWS CloudTrail**
</b></details>

<details>
<summary>Какая управляемая SQL-база в ответе курса?</summary><br><b>

**Amazon RDS**
</b></details>

<details>
<summary>Какая управляемая NoSQL БД?</summary><br><b>

**Amazon DynamoDB**
</b></details>

<details>
<summary>Чем выполнять ad-hoc SQL по данным в S3?</summary><br><b>

**Amazon Athena**
</b></details>

<details>
<summary>Чем добавить анализ изображений и видео?</summary><br><b>

**Amazon Rekognition**
</b></details>

<details>
<summary>Чем трассировать и отлаживать распределённые приложения?</summary><br><b>

**AWS X-Ray**
</b></details>

<details>
<summary>Какой сервис для уведомлений (pub/sub)?</summary><br><b>

**Amazon SNS**
</b></details>

<details>
<summary>Кто ищет вредоносную активность по логам аккаунта?</summary><br><b>

**Amazon GuardDuty**
</b></details>

<details>
<summary>Как централизовать биллинг и политики для нескольких аккаунтов?</summary><br><b>

**AWS Organizations**
</b></details>

<details>
<summary>Чем защитить веб-приложение на уровне L7?</summary><br><b>

**AWS WAF**
</b></details>

<details>
<summary>Как мониторить метрики и алертиться по сервисам?</summary><br><b>

**Amazon CloudWatch**
</b></details>

<details>
<summary>Какой сервис для автоматической оценки уязвимостей?</summary><br><b>

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
<summary>Как добавить регистрацию и вход пользователей?</summary><br><b>

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
<summary>Как кэшировать горячие данные в памяти?</summary><br><b>

**Amazon ElastiCache**
</b></details>

<details>
<summary>Чем ускорить передачу файлов на большие расстояния в S3?</summary><br><b>

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

В основе — **оплата по факту использования**: платите за реально потребляемые ресурсы. В **S3** — объём и класс хранения, запросы, исходящий трафик; в **EC2** — модель закупки, тип инстанса, ОС, регион, EBS и т.д.

Обзор: [AWS Pricing](https://aws.amazon.com/pricing)
</b></details>

<details>
<summary>Как оценить стоимость AWS при сравнении с on-prem?</summary><br><b>

* **AWS Pricing Calculator** / **Migration Evaluator**  
* **TCO**-оценки для сопоставления с капексом/опексом  
* **Cost Explorer** и отчёты **Cost & Usage** после миграции
</b></details>

<details>
<summary>Что входит в Basic Support?</summary><br><b>

* Круглосуточный **Customer Service**  
* **AWS Personal Health Dashboard**  
* **Trusted Advisor** — ограниченный набор проверок (полный — на платных планах поддержки)
</b></details>

<details>
<summary>Как тарифицируются инстансы EC2?</summary><br><b>

Обычно **посекундно** (минимум 60 с за запуск в типичных On-Demand/Spot сценариях) за вычисление + отдельно **EBS**, лицензии, исходящий в публичный интернет трафик. **RI** и **Savings Plans** дают скидку за обязательство.
</b></details>

<details>
<summary>Для чего нужен AWS Pricing Calculator?</summary><br><b>

Оценка **месячной стоимости** набора сервисов до развёртывания: регионы, конфигурации, объёмы данных, экспорт сметы.
</b></details>

<details>
<summary>Что такое Amazon Connect?</summary><br><b>

«Облачный **омниканальный контакт-центр** (голос, чат) с интеграциями CRM».

Подробнее: [Amazon Connect](https://aws.amazon.com/connect)
</b></details>

<details>
<summary>Кто такие APN Consulting Partners?</summary><br><b>

«Партнёры-консультанты **AWS Partner Network**: проектирование, миграция и сопровождение нагрузок в AWS».

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

Верно. Тарифы зависят от **региона**.
</b></details>

<details>
<summary>Что такое AWS Infrastructure Event Management?</summary><br><b>

«Структурированная программа для **Enterprise Support** (и **Business** за доп. плату) по подготовке к крупным событиям: запуск продукта, миграция, маркетинговые пики».
</b></details>

#### Автоматизация в AWS

<details>
<summary>Что такое AWS CodeDeploy?</summary><br><b>

«Управляемое **развёртывание** на EC2, Lambda, ECS и on-prem агентах с канареечными/поэтапными стратегиями».

Подробнее: [AWS CodeDeploy](https://aws.amazon.com/codedeploy)
</b></details>

<details>
<summary>Что такое AWS CloudFormation?</summary><br><b>

**IaC**: шаблоны JSON/YAML описывают стек ресурсов; **Drift detection**, откаты, параметры; альтернатива — **AWS CDK**.
</b></details>

#### Прочие сервисы и инструменты AWS

<details>
<summary>Что такое Amazon Lightsail?</summary><br><b>

«Простая платформа с **фиксированной ценой в месяц** для сайтов и небольших приложений».
</b></details>

<details>
<summary>Что такое Amazon Rekognition?</summary><br><b>

«**Анализ изображений и видео** на управляемых ML-моделях без собственного обучения».

Подробнее: [Amazon Rekognition](https://aws.amazon.com/rekognition)
</b></details>

<details>
<summary>Для чего нужны AWS Resource Groups?</summary><br><b>

«**Группировка** ресурсов по тегам/запросам для операций, отчётов и автоматизации на больших парках».

Документация: [Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
</b></details>

<details>
<summary>Что такое AWS Global Accelerator?</summary><br><b>

«**Статические anycast IP** и маршрутизация трафика по глобальной сети AWS к ближайшим здоровым эндпоинтам».

Подробнее: [Global Accelerator](https://aws.amazon.com/global-accelerator)
</b></details>

<details>
<summary>Что такое AWS Config?</summary><br><b>

«**Инвентаризация и аудит** конфигураций ресурсов, правила соответствия, история изменений».

Подробнее: [AWS Config](https://aws.amazon.com/config)
</b></details>

<details>
<summary>Что такое AWS X-Ray?</summary><br><b>

«**Распределённая трассировка** для анализа задержек и ошибок в микросервисах».

Подробнее: [AWS X-Ray](https://aws.amazon.com/xray)
</b></details>

<details>
<summary>Что такое AWS OpsWorks?</summary><br><b>

«Управляемый **Chef/Puppet** для конфигурации стеков (legacy; для новых систем чаще SSM/контейнеры)».

Подробнее: [AWS OpsWorks](https://aws.amazon.com/opsworks)
</b></details>

<details>
<summary>Что такое AWS Service Catalog?</summary><br><b>

«Каталог **утверждённых** продуктов CloudFormation для self-service в рамках политик организации».

Подробнее: [Service Catalog](https://aws.amazon.com/servicecatalog)
</b></details>

<details>
<summary>Что такое AWS CAF?</summary><br><b>

«**Cloud Adoption Framework** — методология перспектив (бизнес, люди, говернанс, платформа, безопасность, операции) для миграции в облако».

Подробнее: [AWS CAF](https://aws.amazon.com/professional-services/CAF)
</b></details>

<details>
<summary>Что такое AWS Cloud9?</summary><br><b>

«Облачная **IDE** в браузере для разработки и отладки с совместной работой».
</b></details>

<details>
<summary>Что такое AWS Application Discovery Service?</summary><br><b>

«Сбор данных об **on-prem** серверах и зависимостях для планирования миграции в **Migration Hub**».

Подробнее: [Application Discovery](https://aws.amazon.com/application-discovery)
</b></details>

<details>
<summary>Что такое AWS Trusted Advisor?</summary><br><b>

Рекомендации по **безопасности**, **отказоустойчивости**, **лимитам**, **производительности** и **экономии**; полный набор — на **Business/Enterprise** поддержке.
</b></details>

<details>
<summary>Что такое AWS Well-Architected Framework и на каких столпах он основан?</summary><br><b>

«Пять столпов: **операционное совершенство, безопасность, надёжность, эффективность производительности, оптимизация затрат**» (в актуальных материалах добавлен столп **устойчивого развития** — Sustainability).

Подробнее: [Well-Architected](https://aws.amazon.com/architecture/well-architected)
</b></details>

<details>
<summary>Какие сервисы AWS считаются бессерверными (или имеют бессерверный режим)?</summary><br><b>

Примеры: **AWS Lambda**, **Amazon Athena**, **API Gateway**, **DynamoDB**, **S3**, **Step Functions**, **EventBridge**, **Fargate**.
</b></details>

<details>
<summary>Что такое Amazon EMR?</summary><br><b>

«Управляемый **big data** кластер: Spark, Hive, HBase, Flink, Presto и др.».

Подробнее: [Amazon EMR](https://aws.amazon.com/emr)
</b></details>

<details>
<summary>Что такое Amazon Athena?</summary><br><b>

«**SQL** поверх данных в **S3** через каталог **Glue Data Catalog**; оплата за объём просканированных данных».

Подробнее: [Amazon Athena](https://aws.amazon.com/athena)
</b></details>

<details>
<summary>Что такое Amazon Cloud Directory?</summary><br><b>

«Иерархическое **хранилище связей** и атрибутов для приложений (не замена корпоративному AD LDAP)».

Документация: [Cloud Directory](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html)
</b></details>

<details>
<summary>Что такое AWS Elastic Beanstalk?</summary><br><b>

«**PaaS**: загрузка артефакта — платформа поднимает EC2, балансировщик, автоскейлинг; доступ к «ножкам» EC2 сохраняется при необходимости».

Подробнее: [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk)
</b></details>

<details>
<summary>Что такое Amazon SWF?</summary><br><b>

«**Simple Workflow** — координация фоновых задач с состоянием (legacy; для новых систем чаще **Step Functions**)».

Подробнее: [Amazon SWF](https://aws.amazon.com/swf)
</b></details>

<details>
<summary>Что такое Amazon SQS?</summary><br><b>

«Управляемая **очередь сообщений** для развязки микросервисов и бессерверных сценариев».

Подробнее: [Amazon SQS](https://aws.amazon.com/sqs)
</b></details>

#### Аварийное восстановление (DR) в AWS

<details>
<summary>Что такое RTO и RPO в контексте DR?</summary><br><b>

**RTO** — допустимое время **простоя** сервиса после аварии.  
**RPO** — допустимый **интервал потери данных** между последней восстановимой точкой и инцидентом.
</b></details>

<details>
<summary>Какие типовые стратегии DR на AWS?</summary><br><b>

* **Backup & Restore** — периодические бэкапы, восстановление по требованию  
* **Pilot Light** — минимальный живой контур + быстрое масштабирование  
* **Warm Standby** — уменьшенная копия прод-среды  
* **Active-Active / Multi-Site** — параллельные площадки с трафиком
</b></details>

<details>
<summary>У какой стратегии DR обычно самый большой простой, а у какой — наименьший?</summary><br><b>

**Наименьший простой** — **Active-Active / Multi-Site**.  
**Наибольший** — **холодный** сценарий **backup & restore** без непрерывной репликации.
</b></details>

### Итог

Удачи на экзамене — у вас получится.
