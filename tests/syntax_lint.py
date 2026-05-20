"""
Проверка Markdown с вопросами в формате `<details>` / `<summary>`.

Изначально: https://github.com/bregman-arie/devops-interview-questions (surister).

`check_details_tag` и `check_summary_tag` похожи по идее, но разнесены для читаемости.

Запуск:
    python tests/syntax_lint.py <путь_к_файлу.md>
"""

import sys

p = sys.argv[1]


errors = []


def count_details(file_list):
    """
    Считает вхождения `<details>` и `</details>` (должны совпадать).

    В основном для отладки.
    """
    details_final_count = 0
    details_count = 0

    for line_number, line in enumerate(file_list):
        if b"<details>" in line:
            details_count += 1
        if b"</details>" in line:
            details_final_count += 1

    return details_count == details_final_count


def count_summary(file_list):
    """
    Считает вхождения `<summary>` и `</summary>` (должны совпадать).

    В основном для отладки.
    """
    details_final_count = 0
    details_count = 0

    for line_number, line in enumerate(file_list):
        if b"<summary>" in line:
            details_count += 1
        if b"</summary>" in line:
            details_final_count += 1

    return details_count == details_final_count


def check_details_tag(file_list):
    """
    Проверяет последовательность тегов `<details>` … `</details>`.
    При нарушении дописывает сообщение в глобальный список `errors`.
    """

    after_detail = False
    error = False
    err_message = ""
    for line_number, line in enumerate(file_list):
        if b"<details>" in line and b"</details>" in line:
            pass
        else:
            if b"<details>" in line and after_detail:
                err_message = f"Не хватает закрывающего </details> около строки {line_number - 1}"
                error = True
            if b"</details>" in line and not after_detail:
                err_message = f"Не хватает открывающего <details> около строки {line_number - 1}"
                error = True

            if b"<details>" in line:
                after_detail = True

            if b"</details>" in line and after_detail:
                after_detail = False

            if error:
                errors.append(err_message)

        error = False


def check_summary_tag(file_list):
    """
    Проверяет последовательность тегов `<summary>` … `</summary>`.
    При нарушении дописывает сообщение в `errors`.
    """

    after_summary = False
    error = False
    err_message = ""
    for idx, line in enumerate(file_list):
        line_number = idx + 1
        if b"<summary>" in line and b"</summary>" in line:
            if after_summary:
                err_message = f"Не хватает закрывающего </summary> около строки {line_number}"
                error = True

        else:
            if b"<summary>" in line and after_summary:
                err_message = f"Не хватает закрывающего </summary> около строки {line_number}"
                error = True
            if b"</summary>" in line and not after_summary:
                err_message = f"Не хватает открывающего <summary> около строки {line_number}"
                error = True

            if b"<summary>" in line:
                after_summary = True

            if b"</summary>" in line and after_summary:
                after_summary = False

        if error:
            errors.append(err_message)

        error = False


def check_md_file(file_name):
    with open(p, "rb") as f:
        file_list = [line.rstrip() for line in f.readlines()]
    check_details_tag(file_list)
    check_summary_tag(file_list)


if __name__ == "__main__":
    print(f"..........Проверка {p}..........")
    check_md_file(p)
    if errors:
        print(f"{p}: ошибки", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        exit(1)

    print("Проверки пройдены.")
