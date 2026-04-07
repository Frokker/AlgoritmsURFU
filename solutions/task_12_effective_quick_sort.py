'''
Задача 12: Эффективная быстрая сортировка (in-place quicksort)

Тимофей решил сортировать таблицу результатов следующим образом:
при сравнении двух участников выше будет идти тот, у которого
решено больше задач. При равенстве числа решенных задач первым
идет участник с меньшим штрафом. Если же и штрафы совпадают,
то первым будет тот, у которого логин идёт раньше
в алфавитном (лексикографическом) порядке.
Ваша реализация сортировки не может потреблять O(n)
дополнительной памяти для промежуточных данных
(такая модификация быстрой сортировки называется "in-place").

Формат входных данных:
В первой строке задано число участников n.
В каждой из следующих n строк записано: логин, количество
решенных задач и штраф.

Формат выходных данных:
Логины участников в отсортированном порядке, по одному на строку.
'''

import sys

sys.setrecursionlimit(20000)


def compare(a, b):
    """Возвращает True, если участник a должен быть выше участника b."""
    if a[1] != b[1]:
        return a[1] > b[1]
    if a[2] != b[2]:
        return a[2] < b[2]
    return a[0] < b[0]


def partition(arr, low, high):
    """Разбиение Хоара с pivot в середине."""
    pivot = arr[(low + high) // 2]
    i = low
    j = high
    while i <= j:
        while compare(arr[i], pivot):
            i += 1
        while compare(pivot, arr[j]):
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i


def quick_sort_inplace(arr, low, high):
    """In-place быстрая сортировка."""
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p, high)


def efficient_quick_sort(participants):
    """Сортирует участников и возвращает список логинов."""
    arr = list(participants)
    if len(arr) <= 1:
        return [p[0] for p in arr]
    quick_sort_inplace(arr, 0, len(arr) - 1)
    return [p[0] for p in arr]


def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
    n = int(lines[0])
    arr = []

    idx = 1
    for _ in range(n):
        login = lines[idx]
        tasks = int(lines[idx + 1])
        penalty = int(lines[idx + 2])
        arr.append((login, tasks, penalty))
        idx += 3

    quick_sort_inplace(arr, 0, n - 1)

    for item in arr:
        print(item[0])


if __name__ == '__main__':
    # Пример: запуск с тестовыми данными
    participants = [
        ("alice", 5, 10),
        ("bob", 3, 20),
        ("charlie", 5, 10),
    ]
    result = efficient_quick_sort(participants)
    print(result)
    # Ожидаемый вывод: ['alice', 'charlie', 'bob']
