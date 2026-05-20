## Обновление APT — решение

```yaml
- name: Update apt cache and upgrade packages
  hosts: all
  become: true
  tasks:
    - name: apt update and safe upgrade
      ansible.builtin.apt:
        update_cache: true
        upgrade: safe
```

При необходимости полного `dist-upgrade` используйте `upgrade: dist` (осознанно, это может подтянуть смену зависимостей).
