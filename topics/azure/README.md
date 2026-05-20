# Лазурь

- [Лазурь](#лазурь)
  - [Вопросы](#вопросов)
    - [Лазурный 101](#azure-101)
    - [Диспетчер ресурсов Azure](#azure-resource-manager)
    - [Вычислить](#вычислить)
    - [Сеть](#сеть)
    - [Хранилище](#хранилище)
    - [Безопасность](#security)

## Вопросы

### Лазурь 101

<details>
<summary>Что такое портал Azure?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): «Портал Azure — это унифицированная веб-консоль, предоставляющая альтернативу инструментам командной строки. С помощью портала Azure вы можете управлять своей подпиской Azure с помощью графического пользовательского интерфейса».

</b></details>

<details>
<summary>Что такое Azure Marketplace?</summary><br><b>

[Microsoft Docs](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): «Рынок Azure помогает пользователям связываться с партнерами Microsoft, независимыми поставщиками программного обеспечения и стартапами, которые предлагают свои решения и услуги, оптимизированные для работы в Azure».

</b></details>

<details>
<summary>Объяснение групп доступности и зон доступности.</summary><br><b>

Группа доступности — это логическая группа виртуальных машин, которая позволяет Azure понять, как создано ваше приложение для обеспечения избыточности и доступности. Рекомендуется создать две или более виртуальные машины в группе доступности, чтобы обеспечить высокодоступное приложение и соответствовать соглашению об уровне обслуживания Azure на 99,95 %.

</b></details>

<details>
<summary>Что такое политика Azure?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/policy/overview): «Политика Azure помогает обеспечить соблюдение организационных стандартов и оценить соответствие требованиям в масштабе. С помощью панели мониторинга соответствия она предоставляет агрегированное представление для оценки общего состояния среды с возможностью детализации по каждому ресурсу и по каждой политике. Это также помогает привести ваши ресурсы в соответствие с помощью массового исправления существующих ресурсов и автоматического исправления». для новых ресурсов».

</b></details>

<details>
<summary>Объяснение управляемых дисков Azure</summary><br><b>

**Managed Disks** — диски как ресурсы Azure (не VHD в storage account вручную). Типы: Premium SSD, Standard SSD/HDD, Ultra Disk. Снапшоты, шифрование, привязка к VM/VMSS, зоны доступности.

</b></details>

### Диспетчер ресурсов Azure

<details>
<summary>Объясните, что такое Azure Resource Manager.</summary><br><b>

Из [Azure docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview): «Azure Resource Manager — это служба развертывания и управления для Azure. Он предоставляет уровень управления, который позволяет создавать, обновлять и удалять ресурсы в вашей учетной записи Azure. Вы используете функции управления, такие как контроль доступа, блокировки и теги, для защиты и организации ваших ресурсов после развертывания».

</b></details>

<details>
<summary>Каковы разделы шаблона ARM?</summary><br><b>

[Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview): шаблон содержит следующие разделы:

Параметры. Во время развертывания укажите значения, позволяющие использовать один и тот же шаблон в разных средах.

Переменные. Определите значения, которые будут повторно использоваться в ваших шаблонах. Они могут быть построены на основе значений параметров.

Пользовательские функции. Создавайте собственные функции, которые упрощают ваш шаблон.

Ресурсы — укажите ресурсы для развертывания.

Выходы — возвращаемые значения из развернутых ресурсов.

</b></details>

<details>
<summary>Что такое группа ресурсов Azure?</summary><br><b>

Из [Azure docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal): «Группа ресурсов — это контейнер, в котором хранятся связанные ресурсы для решения Azure. Группа ресурсов может включать в себя все ресурсы решения или только те ресурсы, которыми вы хотите управлять как группой».

</b></details>

### Вычислить

<details>
<summary>Какие вычислительные службы Azure вы знаете?</summary><br><b>

* Виртуальные машины Azure.
  * Пакетная обработка Azure
  * Azure Service Fabric.
  * Экземпляры контейнеров Azure.
  * Масштабируемые наборы виртуальных машин Azure.

</b></details>

<details>
<summary>Для чего используется служба «Виртуальные машины Azure»?</summary><br><b>

Виртуальные машины Azure поддерживают ОС Windows и Linux. Их можно использовать для размещения веб-серверов, приложений, резервных копий и баз данных, их также можно использовать в качестве сервера перехода или автономного агента Azure для создания и развертывания приложений.

</b></details>

<details>
<summary>Для чего используется служба «Масштабируемые наборы виртуальных машин Azure»?</summary><br><b>

Масштабирование виртуальных машин Linux или Windows; он позволяет создавать группу виртуальных машин с балансировкой нагрузки и управлять ею. Количество экземпляров виртуальных машин может автоматически увеличиваться или уменьшаться в зависимости от спроса или определенного расписания.

</b></details>

<details>
<summary>Для чего используется служба «Функции Azure»?</summary><br><b>

Функции Azure — это служба бессерверных вычислений Azure.

</b></details>

<details>
<summary>Что такое «надежная функция Azure»?</summary><br><b>

[Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/what-is-microsoft-azure): **Durable Functions** — расширение Azure Functions для написания **отслеживаемых** (stateful) сценариев в бессерверной среде.

</b></details>

<details>
<summary>Для чего используется служба «Экземпляры контейнеров Azure»?</summary><br><b>

Запуск контейнерных приложений (без необходимости выделения виртуальных машин).

</b></details>

<details>
<summary>Для чего используется служба Azure Batch?</summary><br><b>

Запуск параллельных и высокопроизводительных вычислительных приложений

</b></details>

<details>
<summary>Для чего используется служба Azure Service Fabric?</summary><br><b>

Платформа для **микросервисов** с stateful/stateless сервисами, оркестрация на кластере Windows/Linux. Используется для legacy enterprise microservices; часто заменяется AKS для новых проектов.

</b></details>

<details>
<summary>Для чего используется Azure Kubernetes Service (AKS)?</summary><br><b>

**AKS** — управляемый Kubernetes: контейнерные приложения, autoscaling, ingress, Helm, GitOps. Microsoft управляет control plane; вы — node pools, networking, workloads.

</b></details>

### Сеть

<details>
<summary>Какие сетевые службы Azure вы знаете?</summary><br><b>

Virtual Network, Load Balancer, Application Gateway, Azure Firewall, VPN Gateway, ExpressRoute, DNS, CDN, Front Door, Private Link, NSG, NAT Gateway.

</b></details>
<details>
<summary>Объяснение пиринга виртуальной сети</summary><br><b>

Пиринг виртуальных сетей позволяет подключать виртуальные сети. Это означает, что вы можете маршрутизировать трафик между ресурсами подключенных виртуальных сетей в частном порядке через адреса IPv4. Соединение виртуальных сетей в одном регионе называется региональным пирингом виртуальных сетей, однако подключение виртуальных сетей в разных регионах Azure называется глобальным пирингом виртуальных сетей.

</b></details>

<details>
<summary>Что такое регион Azure?</summary><br><b>

Регион Azure — это набор центров обработки данных, развернутых в пределах определенного интервала и подключенных через выделенную региональную сеть с малой задержкой.

</b></details>

<details>
<summary>Что такое N-уровневая архитектура?</summary><br><b>

N-уровневая архитектура делит приложение на логические и физические уровни. Каждый уровень несет определенную ответственность. Уровни физически разделены и выполняются на разных машинах. N-уровневое приложение может иметь архитектуру закрытого уровня или архитектуру открытого уровня. N-уровневые архитектуры обычно реализуются как приложения «инфраструктура как услуга» (IaaS), при этом каждый уровень работает на отдельном наборе виртуальных машин.

</b></details>

### Хранилище

<details>
<summary>Какие службы хранения Azure вам известны?</summary><br><b>

**Blob** (object), **Files** (SMB), **Queue**, **Table**, **Disk** (managed/unmanaged), **Azure Data Lake Storage** (hierarchical namespace on blob).

</b></details>

<details>
<summary>Какие варианты хранения поддерживает Azure?</summary><br><b>

**LRS**, **ZRS**, **GRS**, **RA-GRS** (репликация внутри региона / между зонами / geo). Hot/Cool/Archive tiers для Blob. Premium vs Standard performance tiers.

</b></details>

### Безопасность

<details>
<summary>Что такое Центр безопасности Azure? Каковы некоторые из его особенностей?</summary><br><b>

Это служба мониторинга, обеспечивающая защиту от угроз для всех служб Azure.
Точнее, это:

* Предоставляет рекомендации по безопасности на основе вашего использования.
* Отслеживает настройки безопасности и постоянно все службы
* Анализирует и выявляет потенциальные входящие атаки.
* Обнаруживает и блокирует вредоносное ПО с помощью машинного обучения.

</b></details>

<details>
<summary>Что такое Azure Active Directory?</summary><br><b>

Azure AD — это облачная служба идентификации. Вы можете использовать его как отдельную службу или интегрировать с существующей службой Active Directory, которую вы уже используете.

</b></details>

<details>
<summary>Что такое Microsoft Defender for Cloud (ранее Azure Security Center)?</summary><br><b>

Единая платформа **CSPM + workload protection**: оценка secure score, рекомендации, threat detection для VM, SQL, storage, containers. Часть бывшего «Advanced Threat Protection» интегрирована в Defender.

</b></details>

<details>
<summary>Какие компоненты входят в Microsoft Defender for Identity (ранее Azure ATP)?</summary><br><b>

Sensors на DC, облачный сервис анализа, портал для алертов (lateral movement, brute force, suspicious Kerberos). Интеграция с Defender for Cloud и Sentinel.

</b></details>

<details>
<summary>Где хранятся журналы в Azure Monitor?</summary><br><b>

**Log Analytics workspace** (таблицы Kusto/KQL): `AzureDiagnostics`, `ContainerInsights`, custom logs. Метрики — отдельно в Metrics store. Долгосрочно — export в Storage или **Azure Data Explorer**.

</b></details>

<details>
<summary>Объяснение Azure Site Recovery</summary><br><b>

**DR-as-a-service**: репликация VM/физических серверов в другой регион/AZ, orchestrated failover/failback, RTO/RPO политики. Тестовый failover без простоя prod.

</b></details>

<details>
<summary>Объясните, что делает Azure Advisor</summary><br><b>

**Azure Advisor** — бесплатные рекомендации по **cost**, **security**, **reliability**, **performance**, **operational excellence** на основе телеметрии подписки. Не исправляет автоматически (в отличие от Policy remediate).

</b></details>

<details>
<summary>Какие протоколы доступны для настройки проверки работоспособности (health probe)?</summary><br><b>

Load Balancer / App Gateway: **TCP**, **HTTP**, **HTTPS**. Проверка порта или URL path, интервал, порог unhealthy. Application Gateway — host header, match status codes.

</b></details>

<details>
<summary>Объяснение Microsoft Entra ID (Azure AD)</summary><br><b>

Облачный **identity provider**: пользователи, группы, SSO (SAML/OIDC), MFA, conditional access, B2B guest, hybrid sync с on-prem AD. Основа RBAC в Azure (`role assignments`).

</b></details>

<details>
<summary>Что такое подписка? Какие типы подписок существуют?</summary><br><b>

**Subscription** — граница биллинга и RBAC (контейнер resource groups). Типы соглашений: **Pay-As-You-Go**, **Enterprise Agreement (EA)**, **CSP**, **Free trial**, **Dev/Test**. Management groups иерархия над subscriptions.

</b></details>

<details>
<summary>Объясните, что такое служба хранения BLOB-объектов (Azure Blob Storage).</summary><br><b>

**Object storage** для неструктурированных данных: контейнеры и blobs (block/page/append). Уровни Hot/Cool/Archive, versioning, lifecycle, static website, SFTP, integration с CDN. Account + replication options (LRS/ZRS/GRS).

</b></details>
