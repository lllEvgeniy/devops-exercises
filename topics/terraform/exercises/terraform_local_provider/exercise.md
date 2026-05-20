# Локальный провайдер

## Цели

Узнайте, как использовать и запускать основные команды Terraform.

1. Создайте каталог под названием «my_first_run».
2. Внутри каталога создайте файл «main.tf» со следующим содержимым.

```terraform
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
```

3. Запустите `terraform init`. Что он сделал?
4. Запустите `terraform plan`. Что будет делать Terraform?
5. Наконец, запустите `terraform apply` и убедитесь, что файл создан.

## Решение

Нажмите [здесь, чтобы просмотреть решение](solution.md)