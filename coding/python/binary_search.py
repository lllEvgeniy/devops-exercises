#!/usr/bin/env python

import random
from typing import List, Optional


def binary_search(arr: List[int], lb: int, ub: int, target: int) -> Optional[int]:
    """
    Бинарный поиск в отсортированном массиве: O(log n) по времени.
    Возвращает индекс элемента или -1, если значение не найдено.
    """
    while lb <= ub:
        mid = lb + (ub - lb) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1


def generate_random_list(size: int = 10, lower: int = 1, upper: int = 50) -> List[int]:
    return sorted(random.randint(lower, upper) for _ in range(size))


def find_target_in_list(target: int, lst: List[int]) -> int:
    return binary_search(lst, 0, len(lst) - 1, target)


def main():
    """
    Запуск бинарного поиска по случайно сгенерированному отсортированному списку.
    Сложность по времени: O(log n).
    """
    rand_num_li = generate_random_list()
    target = random.randint(1, 50)
    index = find_target_in_list(target, rand_num_li)
    print(f"Список: {rand_num_li}\nИскомое: {target}\nИндекс: {index}")


if __name__ == '__main__':
    main()
