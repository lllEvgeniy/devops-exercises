# CircleCI

## Вопросы по CircleCI

### CircleCI 101

<details>
<summary>Что такое CircleCI?</summary><br><b>

[CircleCI](https://circleci.com): «CircleCI — платформа **непрерывной интеграции и доставки** для практик DevOps».

</b></details>

<details>
<summary>Какие у CircleCI сильные стороны?</summary><br><b>

По [документации CircleCI](https://circleci.com/docs/about-circleci), среди возможностей:

- SSH к job для отладки сборок;
- параллелизм в `.circleci/config.yml`;
- кэширование между job;
- собственные runners;
- образы Docker, **orbs** (переиспользуемые фрагменты конфигурации);
- API и CLI;
- аналитика нестабильных тестов.

</b></details>

<details>
<summary>Объясните термины: pipeline, workflow, job, step.</summary><br><b>

- **Pipeline** — один прогон CI/CD для коммита/тега (вся конфигурация из `.circleci/config.yml`).
- **Workflow** — граф **job**: порядок, условия, параллельность.
- **Job** — среда (Docker / machine / executor) и последовательность **steps**.
- **Step** — конкретная команда или встроенное действие (checkout, run и т.д.).

</b></details>

<details>
<summary>Что такое orb?</summary><br><b>

[Orbs](https://circleci.com/developer/orbs) — **переиспользуемые пакеты** YAML для CircleCI: команды, executors, примеры интеграций.

Orbs бывают публичными в реестре или приватными в организации.

</b></details>

### CircleCI: практика

<details>
<summary>Где в репозитории лежит конфигурация CircleCI?</summary><br><b>

`.circleci/config.yml`

</b></details>

<details>
<summary>Разберите пример конфигурации.</summary><br><b>

```yaml
version: 2.1

jobs:
  hello:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: Say hello
          command: echo "Hello, World!"

workflows:
  hello-workflow:
    jobs:
      - hello
```

Один **job** в образе `cimg/base:stable`: checkout репозитория и `echo Hello, World!`. **Workflow** запускает этот job.

</b></details>
