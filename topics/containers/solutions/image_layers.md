## Слой за слоем

### Цель

Подробнее о слоях изображения

### Требования

Убедитесь, что Docker установлен в вашей системе и служба запущена.

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

### Инструкции

1. Напишите Dockerfile. Любой Dockerfile :) (главное — валидный синтаксис):

```dockerfile
FROM ubuntu
EXPOSE 212
ENV foo=bar
WORKDIR /tmp
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024

```

2. Создайте образ, используя написанный вами Dockerfile.

`docker image build -t super_cool_app:latest .`

3. Какие инструкции вы использовали, создавали новые слои и какие добавляли метаданные изображения?

```
FROM, RUN -> new layer
EXPOSE, ENV, WORKDIR -> metadata
```

4. Какими способами можно подтвердить свой ответ на последний вопрос?

Вы можете запустить `docker image history super_cool_app`. Он покажет вам каждую инструкцию и ее размер. Обычно инструкции по созданию новых слоев имеют ненулевой размер, но на это нельзя полагаться сам по себе, поскольку некоторые команды RUN могут иметь нулевой размер в выводе `docker image history` (например, `ls -l`).

Вы также можете использовать `docker image inspect super_cool_app` и посмотреть, есть ли в выводе в разделе RootFS количество слоев, соответствующее инструкциям, которые должны создавать новые слои.

5. Можете ли вы уменьшить размер созданного изображения?

да, например, используйте все инструкции RUN как одну инструкцию RUN следующим образом:

`RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024`

В этом случае изменение размера может быть не столь значительным, но в некоторых случаях оно окажет большое влияние на размер изображения.