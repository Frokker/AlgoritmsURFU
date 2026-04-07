"""
Задача 12: Эффективная быстрая сортировка (in-place QuickSort)

Отсортировать участников по трём критериям:
  1. Больше решённых задач → выше.
  2. При равенстве задач — меньше штраф → выше.
  3. При равенстве штрафа — логин раньше по алфавиту → выше.

Ограничение: нельзя использовать O(n) дополнительной памяти
(MergeSort не подходит). Используем in-place QuickSort
с разбиением Хоара.

Алгоритм:
  1. Выбираем pivot (средний элемент).
  2. Два указателя i (слева) и j (справа).
  3. Двигаем i вправо, пока arr[i] < pivot;
     двигаем j влево, пока arr[j] > pivot.
  4. Если i <= j — меняем местами, сдвигаем оба.
  5. Рекурсивно сортируем левую и правую части.

Сложность: O(n log n) в среднем, O(1) доп. памяти.
"""

import sys

sys.setrecursionlimit(20000)


def compare(a, b):
    """Возвращает True, если участник a должен быть выше участника b.

    Порядок сравнения:
      1) Больше задач (a[1]) → выше
      2) Меньше штраф (a[2]) → выше
      3) Логин раньше по алфавиту (a[0]) → выше
    """
    if a[1] != b[1]:
        return a[1] > b[1]  # больше задач = лучше
    if a[2] != b[2]:
        return a[2] < b[2]  # меньше штраф = лучше
    return a[0] < b[0]       # раньше по алфавиту = лучше


def partition(arr, low, high):
    """Разбиение Хоара: выбираем pivot в середине,
    переставляем элементы так, чтобы слева были 'большие',
    справа 'меньшие' (по нашему компаратору)."""
    pivot = arr[(low + high) // 2]
    i = low
    j = high
    while i <= j:
        # Ищем элемент слева, который НЕ должен быть левее pivot
        while compare(arr[i], pivot):
            i += 1
        # Ищем элемент справа, который НЕ должен быть правее pivot
        while compare(pivot, arr[j]):
            j -= 1
        if i <= j:
            # Меняем местами "неправильные" элементы
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i  # граница разбиения


def quick_sort_inplace(arr, low, high):
    """Рекурсивная in-place сортировка."""
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)   # левая часть
        quick_sort_inplace(arr, p, high)       # правая часть


def efficient_quick_sort(participants):
    """Обёртка: сортирует участников и возвращает список логинов."""
    arr = list(participants)
    if len(arr) <= 1:
        return [p[0] for p in arr]
    quick_sort_inplace(arr, 0, len(arr) - 1)
    return [p[0] for p in arr]


if __name__ == '__main__':
    participants = [
        ("alice", 5, 10),
        ("bob", 3, 20),
        ("charlie", 5, 10),
    ]
    result = efficient_quick_sort(participants)
    print(result)  # ['alice', 'charlie', 'bob']
