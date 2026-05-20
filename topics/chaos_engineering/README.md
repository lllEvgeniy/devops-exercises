# Хаос-инжиниринг (chaos engineering)

- [Вопросы](#вопросы-по-chaos-engineering)
  - [Основы](#основы)

## Вопросы по chaos engineering

### Основы

<details>
<summary>Что такое chaos engineering?</summary><br><b>

[Википедия](https://en.wikipedia.org/wiki/Chaos_engineering): «Chaos engineering — дисциплина **экспериментов** на продакшн-подобной системе, чтобы заранее выявить слабые места и повысить устойчивость к сбоям».

[TechTarget](https://www.techtarget.com/searchitoperations/definition/chaos-engineering): «Процесс проверки распределённой системы на способность переживать **непредвиденные** отказы».

</b></details>

<details>
<summary>Каков типичный рабочий процесс chaos engineering?</summary><br><b>

По [Gremlin](https://www.gremlin.com/community/tutorials/what-is-chaos-engineering) и общей практике обычно выделяют шаги:

1. **Гипотеза и план** — что может сломаться и как мы это измерим (SLO, метрики, алерты).
2. **Минимальный blast radius** — эксперимент в **канареечной** зоне или на нерепрезентативной нагрузке.
3. **Анализ** — если система деградирует, **останавливаем** эксперимент, фиксируем причину, внедряем защиту; затем можно повторить или расширить область.

Цикл повторяют для новых сценариев отказов.

</b></details>

<details>
<summary>Назовите несколько инструментов для chaos / fault injection.</summary><br><b>

- **AWS FIS** — контролируемые сбои в сервисах AWS.
- **Azure Chaos Studio** — сценарии отказов в Azure.
- **Chaos Monkey** (Netflix / Simian Army) — классический пример отключения инстансов.
- **LitmusChaos** — фреймворк для Kubernetes.
- **Chaos Mesh** — chaos-платформа для Kubernetes.

Больше ссылок: [awesome-chaos-engineering](https://github.com/dastergon/awesome-chaos-engineering).

</b></details>
