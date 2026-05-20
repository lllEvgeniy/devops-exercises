# Задание: Flask + контейнер + CI (вариант 2)

Нужно **доработать** приложение, **упаковать в контейнер** и настроить **CI**. Прочитайте инструкции целиком.

Если какой‑то шаг из коробки не работает — **исправьте** (это часть задания).

## Установка

1. `python3 -m venv Challenge_venv`
2. `source Challenge_venv/bin/activate` (на Windows — `Challenge_venv\Scripts\activate`)
3. `pip install -r requirements.txt`

## Запуск приложения

1. Каталог задания: `topics/flask_container_ci2` (или актуальный путь в монорепо).
2. `export FLASK_APP=app/main.py`
3. `flask run`
4. http://127.0.0.1:5000 — пример ответа:

```json
{
  "current_uri": "/",
  "example": "/matrix/123n456n789",
  "resources": {
    "column": "/columns/<matrix>/<column_number>",
    "matrix": "/matrix/<matrix>",
    "row": "/rows/<matrix>/<row_number>"
  }
}
```

5. Поведение API (матрица задаётся строкой с `n` как разделителем строк):

- `GET /matrix/<matrix>` — матрица построчно;
- `GET /columns/<matrix>/<column_number>` — столбец по номеру;
- `GET /rows/<matrix>/<row_number>` — строка по номеру.

## Контейнер

```bash
docker build -t app:latest -f /path/to/Dockerfile .
docker run -d -p 5000:5000 app:latest
```

1. Базовый образ — на выбор.
2. В образе — минимум для запуска.

## CI

Файл **`tests.py`** в корне содержит тесты.

1. CI запускает тесты (`python tests.py` или согласованный вами способ).
2. Есть проверка **Dockerfile**.
3. Добавьте ещё один тест (модульный или интеграционный).

### Рекомендации

- Можно менять структуру и стек; по желанию — **`notes.md`** с обоснованием.
- Конфигурация CI — **в репозитории**.
