# Переименование сегмента S3

## Требования

* Существующая корзина S3, отслеживаемая Terraform.
Если у вас его нет, вы можете использовать следующий блок и запустить terraform apply:

```terraform
resource "aws_s3_bucket" "some_bucket" {
    bucket = "some-old-bucket"
}
```

**Внимание:** имена S3 bucket глобально уникальны.

## Решение

```sh
# Имя bucket в AWS неизменяемо — создаём новый bucket
aws s3 mb s3://some-new-bucket-123

# Синхронизация данных из старого bucket в новый
aws s3 sync s3://some-old-bucket s3://some-new-bucket-123

# Вариант 1 (удалить из state и import)

## Удалить старый bucket из state Terraform
terraform state rm aws_s3_bucket.some_bucket

## Импортировать новый bucket в state
terraform import aws_s3_bucket.some_bucket some-new-bucket-123

: '
aws_s3_bucket.some_bucket: Refreshing state... [id=some-new-bucket-123]

Import successful!
The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
'

# Вариант 2 (state mv)

## Переименовать ресурс в state
terraform state mv aws_s3_bucket.some_bucket some-new-bucket-123

: '
Move "aws_s3_bucket.some_bucket" to "aws_s3_bucket.some-new-bucket-123"
Successfully moved 1 object(s).
'

# Обновить main.tf

# В определении ресурса указать новое имя:
# resource "aws_s3_bucket" "some_bucket" {
#    bucket = "some-new-bucket-123"
# }

# Удалить старый bucket в AWS
aws s3 rm s3://some-old-bucket --recursive
aws s3 rb s3://some-old-bucket
```
