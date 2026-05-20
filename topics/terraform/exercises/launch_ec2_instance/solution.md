# Запуск экземпляра EC2

## Требования

* Аккаунт AWS

## Цели

1. Напишите конфигурацию Terraform для запуска экземпляра EC2.
2. Запустите команды, чтобы применить конфигурацию и создать экземпляр EC2.
3. Что произойдет, если вы снова запустите terraform apply?
4. Уничтожьте созданный вами экземпляр с помощью Terraform.

## Решение

```
mkdir exercise

cat << EOT >> main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
EOT

terraform init
terraform validate
terraform plan

# В конце plan: Plan: 1 to add, 0 to change, 0 to destroy

terraform apply -auto-approve

# Пример вывода apply:
# aws_instance.app_server: Creation complete after 49s [id=i-004651a9d4427d236]

# Повторный terraform apply не меняет инфраструктуру:
# Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

# Удаление ресурсов
terraform destroy -auto-approve

# Destroy complete! Resources: 1 destroyed.
```