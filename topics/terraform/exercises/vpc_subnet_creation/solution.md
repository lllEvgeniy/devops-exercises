# Создание пользовательских VPC и подсетей с помощью Terraform


## Цели
1. Создайте собственный VPC с указанным блоком CIDR.
    Например, вы можете использовать `10.0.0.0/16`.
2. Создайте две подсети в VPC, каждая со своим блоком CIDR.
    Например, вы можете использовать «10.0.0.0/20» для первой подсети и «10.0.16.0/20» для второй подсети.

    Обе подсети должны находиться в разных зонах доступности, чтобы обеспечить высокую доступность.
3. Убедитесь, что Terraform отслеживает VPC и подсети.


## Решение

```sh
# Каталог для конфигурации Terraform
mkdir vpc_subnet_creation && cd vpc_subnet_creation 
```

```sh
# Файл main.tf с VPC и подсетями
touch main.tf
```

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "your-region" # например ap-south-1
}

resource "aws_vpc" "my_custom_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my_custom_vpc_made_with_terraform"
  }
}

resource "aws_subnet" "Subnet_A" {
  cidr_block       = "10.0.0.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-a" # например ap-south-1a
  tags = {
    "Name" = "Subnet A"
  }
}
resource "aws_subnet" "Subnet_B" {
  cidr_block       = "10.0.16.0/20"
  vpc_id            = aws_vpc.my_custom_vpc.id
  availability_zone = "your-availability-zone-b" # например ap-south-1b
  tags = {
    "Name" = "Subnet B"
  }
}
```

```sh
# terraform init — загрузка провайдера AWS
terraform init
```

```sh
# terraform apply — создание VPC и подсетей
terraform apply -auto-approve
```


