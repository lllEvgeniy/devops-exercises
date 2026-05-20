#!/usr/bin/env python

import random
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Сортировка слиянием: O(n log n) по времени в худшем случае."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Сливает два отсортированных списка в один отсортированный."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def generate_random_list(size: int = 10, lower: int = 1, upper: int = 100) -> List[int]:
    return [random.randint(lower, upper) for _ in range(size)]


def main():
    """
    Запуск сортировки слиянием на случайно сгенерированном списке.
    Сложность по времени: O(n log n).
    """
    rand_num_li = generate_random_list()
    print(f"До сортировки: {rand_num_li}")
    sorted_list = merge_sort(rand_num_li)
    print(f"После сортировки: {sorted_list}")


if __name__ == '__main__':
    main()
