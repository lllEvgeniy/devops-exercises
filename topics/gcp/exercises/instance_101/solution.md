# Создание экземпляра VM

## Цели

См. [exercise.md](exercise.md).

## Решение

### Консоль GCP

1. **Compute Engine** → **VM instances** → **Create instance**.
2. Имя: `instance-1`, тип: **e2-micro**.
3. **Labels**: `app=web`, `env=dev` → **Create**.
4. Откройте VM → **Labels**: измените `app` на `db`, удалите `env`.

### gcloud

```bash
gcloud config set project <PROJECT_ID>
gcloud config set compute/region <REGION>
gcloud config set compute/zone <ZONE>

gcloud compute instances create instance-1 \
  --machine-type=e2-micro \
  --labels=app=web,env=dev

gcloud compute instances update instance-1 --update-labels=app=db
gcloud compute instances update instance-1 --remove-labels=env
```

### Terraform

См. [main.tf](main.tf).
