## Моя первая задача — решение

```yaml
- name: Create a new directory
  hosts: all
  tasks:
    - name: Ensure /tmp/new_directory exists
      ansible.builtin.file:
        path: /tmp/new_directory
        state: directory
```
