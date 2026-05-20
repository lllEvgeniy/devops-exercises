## Мой первый playbook — решение

### 1. Playbook

Создайте файл `first_playbook.yml`:

```yaml
- name: Install zlib and create a file
  hosts: some_remote_host
  become: true
  tasks:
    - name: Install zlib
      ansible.builtin.package:
        name: zlib1g
        state: present

    - name: Create the file /tmp/some_file
      ansible.builtin.file:
        path: /tmp/some_file
        state: touch
```

Имя пакета `zlib1g` актуально для Debian/Ubuntu; для других семейств ОС замените на пакет, который даёт библиотеку zlib (или используйте `state: present` с переменной под дистрибутив).

### 2. Инвентарь и запуск

Укажите хост в инвентаре, например в `inventory.ini`:

```ini
[some_remote_host]
some.remote.host.example.com
```

Запуск:

```bash
ansible-playbook -i inventory.ini first_playbook.yml
```
