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

```sh
# Создать каталог
mkdir my_first_run && cd my_first_run

# Создать файл main.tf
cat << EOT >>  main.tf
resource "local_file" "mario_local_file" {
    content  = "It's a me, Mario!"
    filename = "/tmp/who_is_it.txt"
}
EOT

# terraform init
terraform init
# ls -la покажет каталоги .terraform и .terraform.lock.hcl
# Скачаны и установлены провайдеры (здесь hashicorp/local)

# terraform plan
terraform plan
# Показывает, что будет сделано при terraform apply

<< terraform_plan_output
Terraform will perform the following actions:

  # local_file.mario_local_file will be created
  + resource "local_file" "mario_local_file" {
      + content              = "It's a me, Mario!"
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "/tmp/who_is_it.txt"
      + id                   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.
terraform_plan_output

# terraform apply (новичкам лучше без -auto-approve)
terraform apply -auto-approve

ls /tmp/who_is_it.txt
# /tmp/who_is_it.txt
```