## Ansible

### Упражнения

| Название | Тема | Упражнение | Решение |
|----------|------|------------|---------|
| Моя первая задача | tasks | [Упражнение](my_first_task.md) | [Решение](solutions/my_first_task.md) |
| APT: update и upgrade | tasks | [Упражнение](update_upgrade_task.md) | [Решение](solutions/update_upgrade_task.md) |
| Мой первый playbook | playbooks | [Упражнение](my_first_playbook.md) | [Решение](solutions/my_first_playbook.md) |

### Самопроверка по Ansible

<details>
<summary>Опишите компоненты Ansible и связи между ними:

  * task (задача)
  * inventory (инвентарь)
  * module (модуль)
  * play (плей)
  * playbook
  * role (роль)</summary><br><b>

**Task** — один вызов модуля с параметрами (атомарная операция в playbook).

**Module** — код, который выполняется на управляемом хосте (копирование файла, пакетный менеджер, systemd и т.д.).

**Inventory** — список хостов и групп (INI, YAML, динамический инвентарь из облака и т.д.), на которых запускаются plays.

**Play** — сопоставление **набора хостов** из инвентаря с **последовательностью tasks** (и уровнем `become`, переменными и т.д.).

**Playbook** — YAML-файл с одним или несколькими plays.

**Role** — переиспользуемый набор tasks, handlers, шаблонов, файлов и переменных в стандартной раскладке каталогов; подключается из playbook через `roles:` или `import_role` / `include_role`.

</b></details>

<details>
<summary>Чем Ansible отличается от других систем автоматизации? (например, Chef, Puppet)</summary><br><b>

Кратко про Ansible:

* по умолчанию **без агента** на хосте (нужны SSH и Python);
* низкий порог входа, YAML-плейбуки;
* типичная модель **push** с control node (есть и pull-варианты);
* упор на идемпотентные модули и повторяемые прогоны.

</b></details>


<details>
<summary>Верно или нет? Ansible следует парадигме *immutable infrastructure* (неизменяемой инфраструктуры).</summary><br><b>

**Неверно** в классическом смысле: Ansible **изменяет** конфигурацию существующих хостов. Неизменяемая модель чаще подразумевает **замену** узлов (новый образ/инстанс) вместо правок на месте. При частых ручных изменениях возможен **дрейф конфигурации**, поэтому важны идемпотентность, тесты и дисциплина версионирования.

</b></details>

<details>
<summary>Верно или нет? Ansible описывает желаемое конечное состояние в декларативном стиле.</summary><br><b>

**В основном да, с оговоркой:** вы декларируете **желаемое состояние** в модулях (`state: present`, `copy` с содержимым и т.д.), а порядок **plays/tasks** по-прежнему задаётся **процедурно** (сверху вниз). В отличие от чистого imperative-скрипта, модули сами приводят ресурс к описанному состоянию.

</b></details>

<details>
<summary>Какую автоматизацию лучше не возлагать только на Ansible и почему?</summary><br><b>

Ansible по умолчанию **не ведёт полноценное состояние** облака как Terraform: повторный запуск task «создать 5 VM» без проверок может создать ещё пять. Для **провижининга** облачных ресурсов, сложных графов зависимостей и строгого state-файла часто используют Terraform/OpenTofu, Pulumi, облачные SDK — а Ansible оставляют для конфигурации ОС и приложений **поверх** уже созданных ресурсов.

</b></details>

<details>
<summary>Как получить список модулей и справку по конкретному модулю?</summary><br><b>

1. Официальная документация Ansible.
2. В CLI: `ansible-doc -l` — список модулей; `ansible-doc <имя_модуля>` — подробная справка.

</b></details>

#### Ansible — Инвентарь

<details>
<summary>Что такое файл инвентаризации и как его определить?</summary><br><b>

Файл инвентаризации определяет хосты и/или группы хостов, на которых выполняются задачи Ansible.

Пример файла инвентаризации:

```
192.168.1.2
192.168.1.3
192.168.1.4

[web_servers]
190.40.2.20
190.40.2.21
190.40.2.22
```

</b></details>

<details>
<summary>Что такое файл динамической инвентаризации? Когда вы его используете?</summary><br><b>

Динамический инвентарь получает список хостов из **внешнего источника** (облако, CMDB, оркестратор). Используйте его, когда состав хостов **часто меняется** (автоскейлинг, короткоживущие VM) и вручную поддерживать статический список неудобно.

</b></details>

#### Ansible — Переменные

<details>
<summary>Измените задачу так, чтобы имя пакета бралось из переменной `package_name`, а по умолчанию использовалось значение `zlib`.

Исходный фрагмент:

```yaml
- name: Install a package
  package:
    name: "zlib"
    state: present
```
</summary><br><b>

```yaml
- name: Install a package
  ansible.builtin.package:
    name: "{{ package_name | default('zlib') }}"
    state: present
```

</b></details>

<details>
<summary>Как сделать переменную `use_var` необязательной (не передавать ключ в модуль, если переменная не задана)?

Пример:

```yaml
- name: Install a package
  package:
    name: "zlib"
    state: present
    use: "{{ use_var }}"
```
</summary><br><b>

Используйте фильтр **`default(omit)`** (в паре с конструкцией, которую поддерживает модуль):

```yaml
- name: Install a package
  ansible.builtin.package:
    name: "zlib"
    state: present
    use: "{{ use_var | default(omit) }}"
```

Тогда при отсутствии `use_var` ключ `use` не попадёт в аргументы модуля.

</b></details>

<details>
<summary>Каким будет результат следующего play?</summary><br><b>

```yaml
---
- name: Print information about my host
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Print hostname
      ansible.builtin.debug:
        msg: "It's me, {{ ansible_hostname }}"
```

Ошибка / пустое значение: при `gather_facts: false` факт `ansible_hostname` **не** заполняется (если вы сами не задали его), подстановка в `msg` приведёт к проблемам на выполнении.

</b></details>

<details>
<summary>Когда в выражении `{{ lookup('env', 'BEST_YEAR') | default('2017', true) }}` подставится `2017`?</summary><br><b>

Когда переменная окружения **`BEST_YEAR`** не задана, **пустая** или считается **ложной** (`true` во втором аргументе `default` включает так называемый *boolean* режим).

</b></details>

<details>
<summary>Если переменная равна `1`, нужно вывести `one`, иначе `two`. Как записать в Jinja2?</summary><br><b>

```jinja2
{{ 'one' if my_var == 1 else 'two' }}
```

(или тернарный вид через `ternary`, если он доступен в вашей версии фильтров.)

</b></details>

<details>
<summary>Строка в переменной — `"True"`. Как привести к настоящему boolean для условий?</summary><br><b>

```jinja2
{{ some_string_var | bool }}
```

Учтите: `bool` трактует строки в духе YAML; для произвольных строк лучше явная проверка.

</b></details>

<details>
<summary>Вы хотите запускать Ansible playbook только на определенной второстепенной версии вашей ОС. Как бы вы этого достигли?</summary><br><b>

`when: ansible_distribution_major_version == "8"` (или `ansible_facts['distribution_version']`). В `hosts:` — limit по группе с нужной ОС; в dynamic inventory — фильтр по тегу/атрибуту.

</b></details>

<details>
<summary>Для чего используется директива «become»?</summary><br><b>

**Privilege escalation** — выполнение задачи от root (или другого пользователя): `become: true`, `become_user: root`, `become_method: sudo`. Аналог `sudo` для модулей, которым нужны права администратора.

</b></details>

<details>
<summary>Что такое факты? Как увидеть все факты об определенном хосте?</summary><br><b>

**Facts** — переменные, собранные модулем `setup` (ОС, сеть, память…). Просмотр: `ansible <host> -m setup` или play с `debug: var=ansible_facts`. Кастомные: `set_fact`, `ansible_local`.

</b></details>

<details>
<summary>Каков будет результат выполнения следующей задачи? Как это исправить?

```
- hosts: localhost
  tasks:
      - name: Install zlib
        package:
          name: zlib
          state: present
```

</summary><br><b>

В примере ключи на русском и опечатка `Zlib` — модуль не найдёт пакет. Нужны английские ключи YAML и имя пакета ОС (`zlib` / `zlib1g` на Debian). Исправленный фрагмент см. в summary.

</b></details>

<details>
<summary>Какие лучшие практики Ansible вам известны? Назовите не менее трех</summary><br><b>

Использовать **roles** и `ansible-galaxy`; idempotent **modules** вместо `shell`; **Vault** для секретов; `ansible-lint`/Molecule; теги и `check_mode`; inventory по средам; `--diff` в CI; явные `name` у tasks.

</b></details>

<details>
<summary>Объясните структуру каталогов роли Ansible.</summary><br><b>

`tasks/main.yml`, `handlers/main.yml`, `defaults/main.yml`, `vars/main.yml`, `files/`, `templates/`, `meta/main.yml`, `molecule/`. В playbook: `roles: [myrole]`.

</b></details>

<details>
<summary>Какие «блоки» используются в Ansible?</summary><br><b>

`block`/`rescue`/`always` (try/catch/finally), `block` с `delegate_to`, группировка tasks. Также логические блоки: `when`, `loop`, `tags`.

</b></details>

<details>
<summary>Как вы обрабатываете ошибки в Ansible?</summary><br><b>

`ignore_errors: true`, `failed_when`/`changed_when`, `block` + `rescue`/`always`, `any_errors_fatal`, `max_fail_percentage`. В CI — `ansible-playbook` exit code; callbacks для уведомлений.

</b></details>

<details>
<summary>Вы хотите запустить определенную команду в случае сбоя задачи. Как бы вы этого достигли?</summary><br><b>

`block` + `rescue`:

```yaml
- block:
    - name: risky task
      command: ...
  rescue:
    - name: on failure
      command: /usr/local/bin/rollback.sh
```

</b></details>

<details>
<summary>Напишите сценарий для установки zlib и vim на всех хостах, если в системе существует файл /tmp/mario.</summary><br><b>

```
---
- hosts: all
  vars:
      mario_file: /tmp/mario
      package_list:
          - 'zlib'
          - 'vim'
  tasks:
      - name: Check for mario file
        stat:
            path: "{{ mario_file }}"
        register: mario_f

      - name: Install zlib and vim if mario file exists
        become: "yes"
        package:
            name: "{{ item }}"
            state: present
        with_items: "{{ package_list }}"
        when: mario_f.stat.exists
```

</b></details>

<details>
<summary>Напишите одну задачу, которая проверяет, что все файлы в переменной files_list существуют на хосте.</summary><br><b>

```
- name: Ensure all files exist
  assert:
    that:
      - item.stat.exists
  loop: "{{ files_list }}"
```

</b></details>

<details>
<summary>Напишите сценарий для развертывания файла «/tmp/system_info» на всех хостах, кроме группы контроллеров, со следующим содержимым.</summary><br><b>

Шаблон `system_info.j2`:

```
I'm {{ ansible_hostname }} and my operating system is {{ ansible_distribution }}
```

Замените переменные Jinja2 фактическими facts (`ansible_hostname`, `ansible_distribution`).

Playbook:

```yaml
---
- name: Deploy /tmp/system_info file
  hosts: all:!controllers
  tasks:
      - name: Deploy /tmp/system_info
        template:
            src: system_info.j2
            dest: /tmp/system_info
```

</b></details>

<details>
<summary>Переменная whoami определена в следующих местах:

  * роли по умолчанию -> whoami: mario
  * дополнительные переменные (переменные, которые вы передаете в Ansible CLI с помощью -e) -> whoami: toad
  * факты о хосте -> whoami: Луиджи
  * переменные инвентаря (неважно какого типа) -> whoami: браузер

Какой из них будет использоваться в зависимости от приоритета переменных?</summary><br><b>

Правильный ответ — «жаба».

Приоритет переменных связан с тем, как переменные переопределяют друг друга, когда они установлены в разных местах. Если вы еще не испытали этого, я уверен, что в какой-то момент вы это сделаете, поэтому это полезная тема, о которой стоит знать.

В контексте нашего вопроса порядок будет следующим: дополнительные переменные (всегда переопределяют любую другую переменную) -> факты хоста -> переменные инвентаря -> роли по умолчанию (самые слабые).

Вот порядок приоритета от наименьшего к наибольшему (последние перечисленные переменные получают приоритет):

1. значения командной строки (например, «-u пользователь»)
2. роли по умолчанию [[1\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id15)
3. переменные файла инвентаризации или группы сценариев [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16)
4. инвентаризация group_vars/all [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
5. playbook group_vars/all [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
6. инвентаризация group_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
7. playbook group_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
8. переменные хоста файла инвентаризации или сценария [[2\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id16)
9. инвентаризация host_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
10. playbook host_vars/* [[3\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id17)
11. факты о хосте/кешированные set_facts [[4\]](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#id18)
12. играть в варсы
13. играть в vars_prompt
14. играть в vars_files
15. переменные роли (определены в role/vars/main.yml)
16. переменные блока (только для задач в блоке)
17. переменные задачи (только для задачи)
18. include_vars
19. set_facts/зарегистрированные переменные
20. Параметры роли (и include_role)
21. включить параметры
22. дополнительные переменные (всегда выигрывает приоритет)

Полный список можно найти по адресу [PlayBook Variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#ansible-variable-precedence). Также обратите внимание, что между Ansible 1.x и 2.x существует значительная разница.

</b></details>

<details>
<summary>Для каждого из следующих утверждений определите, истинно оно или ложно:

  * Модуль — это набор задач.
  * Лучше использовать оболочку или команду вместо конкретного модуля
  * Факты о хосте переопределяют игровые переменные.
  * Роль может включать в себя следующее: переменные, мета и обработчики.
  * Динамическая инвентаризация создается путем извлечения информации из внешних источников.
  * Лучше всего использовать отступ в 2 пробела вместо 4.
  * «notify» используется для запуска обработчиков
  * Это «hosts: all:!controllers» означает «запускать только на хостах группы контроллеров».</summary><br><b>

* **Неверно** — модуль ≠ набор задач (модуль — атомарное действие).<br>
* **Неверно** — предпочитайте специализированные модули, не `shell`.<br>
* **Неверно** — play vars обычно **переопределяют** facts (выше приоритет).<br>
* **Верно** — role: vars, meta, handlers, tasks, templates…<br>
* **Верно** — dynamic inventory из cloud/API.<br>
* **Верно** — в Ansible принят отступ 2 пробела.<br>
* **Верно** — `notify` → handlers.<br>
* **Неверно** — `all:!controllers` = все **кроме** controllers.

</b></details>

<details>
<summary>Объясните разницу между вилками и последовательным портом и дросселем.</summary><br><b>

«Последовательный» — это похоже на поочередный запуск плейбука для каждого хоста в ожидании завершения всей плейбука перед переходом к следующему хосту. `forks`=1 означает запуск первой задачи в игре на одном хосте перед запуском той же задачи на следующем хосте, поэтому первая задача будет запущена для каждого хоста до того, как будет затронута следующая задача. Вилка по умолчанию — 5 в ansible.

```
[defaults]
forks = 30
```

```
- hosts: webservers
  serial: 1
  tasks:
    - name: ...
```Ansible также поддерживает `throttle`. Это ключевое слово ограничивает количество рабочих процессов до максимального значения, установленного с помощью настроек вилки или последовательного порта. Это может быть полезно для ограничения задач, которые могут быть ресурсоемкими или взаимодействовать с API-интерфейсом, ограничивающим скорость.

```
tasks:
- command: /path/to/cpu_intensive_command
  throttle: 1
```

</b></details>

<details>
<summary>Что такое ansible-pull? Чем это отличается от того, как работает ansible-playbook?</summary><br><b>

**ansible-pull** — playbook на **целевом** хосте по cron/systemd (узел тянет конфиг с git). **push** (обычный) — control node SSH на множество хостов. Pull удобен для edge/без постоянного Ansible controller.

</b></details>

<details>
<summary>Что такое Ansible Vault?</summary><br><b>

Шифрование секретов в vars/files: `ansible-vault encrypt secrets.yml`, запуск с `--ask-vault-pass` или vault password file. В play: зашифрованные переменные; в CI — vault ID из secret store.

</b></details>

<details>
<summary>Продемонстрируйте каждое из следующих действий с помощью Ansible:

  * Условные обозначения
  * Циклы</summary><br><b>

```yaml
- name: Install if Debian
  apt:
    name: nginx
    state: present
  when: ansible_os_family == "Debian"

- name: Loop users
  user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
  loop:
    - { name: alice, groups: wheel }
    - { name: bob, groups: users }
```

</b></details>

<details>
<summary>Что такое фильтры? Есть ли у вас опыт написания фильтров?</summary><br><b>

**Jinja2 filters** в шаблонах/vars: `{{ name | upper }}`, `{{ list | join(',') }}`. Кастомные — Python plugin в `filter_plugins/`. Примеры: `default`, `map`, `combine`, `to_yaml`.

</b></details>

<details>
<summary>Напишите фильтр для капитализации строки</summary><br><b>

```
def cap(self, string):
    return string.capitalize()
```

</b></details>

<details>
<summary>Вы хотели бы запускать задачу только в том случае, если предыдущая задача что-либо изменила. Как бы вы этого достигли?</summary><br><b>

Зарегистрируйте результат: `register: result`, затем `when: result is changed` (или `result.changed` в старых версиях). Для handlers — `notify` при `changed`.

</b></details>

<details>
<summary>Что такое callback plugins? Чего вы можете достичь, используя callback plugins?</summary><br><b>

Плагины, реагирующие на события playbook (task ok/fail, stats): логирование в Slack/Splunk, профилирование, junit output для CI, агрегированные отчёты. Включаются в `ansible.cfg` (`callback_whitelist`).

</b></details>

<details>
<summary>В чем разница между include_task и import_task?</summary><br><b>

**import_tasks** — статический include на этапе парсинга (как copy-paste), теги применяются статически.<br>
**include_tasks** — динамический, может быть под `when`, loop; теги наследуются иначе. В Ansible 2.15+ предпочитают `import_playbook` / `include_tasks` по сценарию.

</b></details>

<details>
<summary>Файл «/tmp/exercision» содержит следующее содержимое.

```
Гоку = 9001
Вегета = 5200
Стволы = 6000
Готенкс = 32
```

С помощью одной задачи переключите контент на:

```
Гоку = 9001
Вегета = 250
Стволы = 40
Готенкс = 32
```

</summary><br><b>

```
- name: Change saiyans levels
  lineinfile:
    dest: /tmp/exercise
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
  with_items:
    - { regexp: '^Vegeta', line: 'Vegeta = 250' }
    - { regexp: '^Trunks', line: 'Trunks = 40' }
    ...

```
</b></details>

#### Ansible — выполнение и стратегия

<details>
<summary>Правда или ложь? По умолчанию Ansible выполнит все текущие задачи на одном хосте, прежде чем перейти к следующему хосту.</summary><br><b>

Неверно. Ansible выполнит одну задачу на всех хостах, прежде чем перейти к следующей задаче в игре. На сегодняшний день по умолчанию используется 5 форков.<br>
Такое поведение описывается в Ansible как «стратегия», и его можно настроить.

</b></details>

<details>
<summary>Что такое «стратегия» в Ansible? Какова стратегия по умолчанию?</summary><br><b>

Стратегия в Ansible описывает, как Ansible будет выполнять различные задачи на хостах. По умолчанию Ansible использует «Линейную стратегию», которая определяет, что каждая задача будет выполняться на всех хостах, прежде чем перейти к следующей задаче.

</b></details>

<details>
<summary>Какие стратегии в Ansible вам известны?</summary><br><b>

- Линейный: стратегия по умолчанию в Ansible. Прежде чем продолжить, запустите каждую задачу на всех хостах.
  - **Free** (`free`): на каждом хосте выполняются все задачи play до конца как можно быстрее (параллельно по хостам).
  - Отладка: запуск задач в интерактивном режиме.

</b></details>

<details>
<summary>Для чего используется ключевое слово <code>serial</code>?</summary><br><b>

Он используется для указания количества (или процента) хостов, на которых будет запущена полная игра, прежде чем переходить к следующему количеству хостов в группе.

Например:

```yaml
- name: Some play
  hosts: databases
  serial: 4
```

Если в вашей группе 8 хостов, play сначала полностью отработает на 4 хостах, затем на оставшихся 4.

</b></details>

#### Ansible-тестирование

<details>
<summary>Как вы тестируете свои проекты на основе Ansible?</summary><br><b>

**Molecule** (Docker/Podman instances), `ansible-lint`, `ansible-playbook --check` (dry-run), testinfra/Inspec после apply, CI matrix по ОС, `verify` step в Molecule, mock с `localhost` connection.

</b></details>

<details>
<summary>Что такое Молекула? Как это работает?</summary><br><b>

Он используется для быстрой разработки и тестирования ролей **Ansible**. Molecule можно использовать для одновременного тестирования ролей Ansible на различных дистрибутивах Linux. Эта возможность тестирования помогает вселить уверенность в автоматизацию сегодня и со временем, пока роль сохраняется.

</b></details>

<details>
<summary>Вы запускаете тесты Ansible и получаете сообщение «тест идемпотентности не пройден». Что это значит? Почему идемпотентность важна?</summary><br><b>

Повторный прогон того же play **изменил** состояние системы: ожидалось «ничего не делать» (0 изменений), а модули внесли правки. Идемпотентность важна, чтобы повторные деплои были **предсказуемыми** и не ломали среду «шумными» диффами.

</b></details>

#### Ansible — отладка

<details>
<summary>Как узнать тип данных определенной переменной в одном из плейбуков?</summary><br><b>

"{{ some_var | type_debug }}"

</b></details>

#### Ansible — Коллекции

<details>
<summary>Что такое коллекции в Ansible?</summary><br><b>

Коллекции Ansible — это способ упаковки и распространения модулей, ролей, плагинов и документации в структурированном формате. Они помогают эффективно организовывать и распространять код автоматизации, особенно в сложных средах.

</b></details>

<details>
<summary>Зачем использовать коллекции Ansible?</summary><br><b>

- Модульные и многоразовые компоненты.
  - Упрощает управление пользовательскими и сторонними модулями.
  - Обеспечивает стандартизированный способ распространения контента автоматизации.
  - Помогает в контроле версий и управлении зависимостями.

</b></details><!-- {% endraw %} -->