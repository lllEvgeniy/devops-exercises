## AWS — запуск веб-экземпляра EC2

### Цели

Запустите один экземпляр EC2 со следующими требованиями:

1. Образ Amazon Linux 2
2. Тип инстанса: выберите тот, у которого есть 1 виртуальный ЦП и 1 ГиБ памяти.
3. Хранилище инстанса должно быть удалено при прекращении работы инстанса.
4. При запуске экземпляра он должен установить:
  1. Установите пакет httpd.
  2. Запустите службу httpd.
  3. Убедитесь, что содержимое /var/www/html/index.html гласит: «Я сделал это!» Это потрясающе!»
5. Он должен иметь тег: «Тип: web», а имя экземпляра должно быть «web-1».
6. HTTP-трафик (порт 80) должен приниматься откуда угодно.

### Решение

1. Выберите ближайший к вам регион 
2. Зайдите в сервис EC2.
3. Нажмите «Экземпляры» в меню и нажмите «Запустить экземпляры».
4. Выберите изображение: Amazon Linux 2.
5. Выберите тип экземпляра: t2.micro. 
6. Убедитесь, что в разделе хранилища установлен флажок «Удалить при прекращении».
7. В поле «Данные пользователя» указывается следующее:

```
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>I made it! This is is awesome!</h1>" > /var/www/html/index.html
```

8. Добавьте теги со следующими ключами и значениями:
  * ключ «Тип» и значение «web»
  * ключ «Имя» и значение «web-1»
9. В разделе группы безопасности добавьте правило для приема HTTP-трафика (TCP) на порту 80 из любой точки мира.
10. Нажмите «Просмотр», а затем после проверки нажмите «Запустить».
11. Если у вас нет пары ключей, создайте ее и загрузите.

### Решение с использованием Terraform

```terraform
provider "aws" {
  region = "us-east-1" // Or your desired region
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678" // Replace with the correct AMI for Amazon Linux 2
  instance_type = "t2.micro" // Or any instance type with 1 vCPU and 1 GiB memory

  tags = {
    Name = "web-1"
    Type = "web"
  }

  root_block_device {
    volume_size           = 8 // Or any desired size
    delete_on_termination = true
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo bash -c 'echo \"I made it! This is awesome!\" > /var/www/html/index.html'",
      "sudo systemctl enable httpd"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/your_private_key.pem") // Replace with the path to your private key
      host        = self.public_ip
    }
  }

  security_group_ids = [aws_security_group.web_sg.id]
}

resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Security group for web server"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```