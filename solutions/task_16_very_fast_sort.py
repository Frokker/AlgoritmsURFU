'''
Задача 16: Очень быстрая сортировка (Fast Sort)

Имеется рекуррентная последовательность А1, А2, ... AN,
строящаяся по следующему правилу:
A1 = K, Ai+1 = (Ai * M) mod (2^32 - 1) mod L.
Требуется найти сумму всех нечетных по порядку элементов
в отсортированной по неубыванию последовательности по модулю L.

Формат входных данных:
Четыре целых числа: N, K, M, L.

Формат выходных данных:
Сумма нечетных по порядку элементов отсортированной
последовательности по модулю L.
'''

import sys


def fast_sort_sum(n, k, m, l):
    """Генерирует последовательность, сортирует и возвращает сумму
    элементов на нечётных позициях (1, 3, 5, ...) по модулю L."""
    a = [0] * n
    a[0] = k
    MOD = 0xFFFFFFFF

    for i in range(n - 1):
        a[i + 1] = ((a[i] * m) % MOD) % l

    a.sort()

    res = 0
    for i in range(0, n, 2):
        res = (res + a[i]) % l

    return res


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    L = int(input_data[3])

    print(fast_sort_sum(N, K, M, L))


if __name__ == '__main__':
    # Пример использования
    print(fast_sort_sum(3, 1, 2, 10))
    print(fast_sort_sum(1, 5, 3, 100))
    # Ожидаемый вывод: 5
