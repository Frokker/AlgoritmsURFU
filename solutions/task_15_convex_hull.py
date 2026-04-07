'''
Задача 15: Выпуклая оболочка (Convex Hull)

Имеется массив из N целочисленных точек на плоскости.
Требуется найти периметр наименьшего охватывающего
многоугольника, содержащего все точки.

Формат входных данных:
В первой строке задано число точек N.
В каждой из следующих N строк записаны координаты точки (x, y).

Формат выходных данных:
Одно вещественное число — периметр выпуклой оболочки
с двумя знаками после запятой.
'''

import math
import sys


def cross_product(o, a, b):
    """Векторное произведение OA x OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Построение выпуклой оболочки алгоритмом Эндрю (Andrew's monotone chain)."""
    points = sorted(points)
    if len(points) <= 1:
        return points

    # Нижняя оболочка
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Верхняя оболочка
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def distance(p1, p2):
    """Евклидово расстояние между двумя точками."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def convex_hull_perimeter(n, points):
    """Вычисляет периметр выпуклой оболочки."""
    if n <= 1:
        return 0.0

    hull = convex_hull(points)

    if len(hull) <= 1:
        return 0.0

    perimeter = 0.0
    for i in range(len(hull)):
        perimeter += distance(hull[i], hull[(i + 1) % len(hull)])

    return round(perimeter, 2)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    points = []

    idx = 1
    for _ in range(n):
        points.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2

    print(f"{convex_hull_perimeter(n, points):.2f}")


if __name__ == '__main__':
    # Пример: треугольник 3-4-5
    points = [(0, 0), (3, 0), (0, 4)]
    print(convex_hull_perimeter(3, points))
    # Ожидаемый вывод: 12.0

    # Пример: квадрат
    points2 = [(0, 0), (1, 0), (1, 1), (0, 1)]
    print(convex_hull_perimeter(4, points2))
    # Ожидаемый вывод: 4.0
