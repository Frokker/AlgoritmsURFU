### Решение задач  1,5,9,12,15,16,18,22,26,31

# Решения задач 1, 5, 9, 12, 15, 16, 18, 22, 26, 31

Задача 1. Ближайший ноль. 

**Условие задачи:**
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. На каждом участке либо уже построен дом, либо участок пустой. Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого участка знать расстояние до ближайшего пустого участка. Пустые участки обозначены нулями. 

Формат входных данных: В первой строке дана длина улицы $n(1\le n\le10^{6})$. В следующей строке записаны п целых неотрицательных чисел. Для каждого из участков выведите расстояние до ближайшего нуля. 

**Решение на Python:**

```python
# Чтение входных данных
n = int(input())
houses = list(map(int, input().split()))

# Инициализация массива расстояний бесконечностью
distances = [float('inf')] * n

# Первый проход: слева направо
zero_pos = -float('inf')
for i in range(n):
    if houses[i] == 0:
        zero_pos = i
        distances[i] = 0
    else:
        # Расстояние до последнего встреченного нуля слева
        distances[i] = min(distances[i], i - zero_pos)

# Второй проход: справа налево
zero_pos = float('inf')
for i in range(n - 1, -1, -1):
    if houses[i] == 0:
        zero_pos = i
        distances[i] = 0
    else:
        # Минимум между нулем слева и нулем справа
        distances[i] = min(distances[i], zero_pos - i)

# Вывод результата
print(*distances)

```

---

Задача 5. Длинное сложение и вычитание 

**Условие задачи:**
На вход подается три строки. Первая содержит представление длинного десятичного числа (первый операнд), вторая представление операции, строки + и, третья представление второго операнда. Длина первой и третьей строки ограничены 1000 символами. Требуется исполнить операцию и вывести результат в десятичном представлении. 

**Решение на Python:**

```python
# Чтение входных данных
a = int(input().strip())
op = input().strip()
b = int(input().strip())

# В Python реализована встроенная поддержка длинной арифметики, 
# поэтому дополнительные структуры данных для больших чисел не требуются.
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)

```

---

Задача 9. Вырубка деревьев. 

**Условие задачи:**
Король Флатландии решил вырубить некоторые деревья, растущие перед его дворцом. Деревья перед дворцом короля посажены в ряд, всего там растет n деревьев, расстояния между соседними деревьями одинаковы. После вырубки перед дворцом должно остаться m деревьев, и расстояния между соседними деревьями должны быть одинаковыми. Требуется написать программу, которая по заданным числам n и m определит, сколько существует способов вырубки некоторых из n деревьев. 

**Решение на Python:**

```python
import sys

def main():
    # Чтение данных из входного потока
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    ways = 0
    
    # Обработка граничных случаев
    if m == 0:
        ways = 1  # Существует только 1 способ - вырубить все деревья
    elif m == 1:
        ways = n  # Существует n способов оставить ровно одно дерево
    else:
        # Перебор возможных шагов (расстояний) между оставленными деревьями
        # Максимальный шаг d возможен, если (m - 1) * d < n
        d = 1
        while (m - 1) * d < n:
            # Для конкретного шага d количество возможных стартовых позиций равно n - (m - 1) * d
            ways += n - (m - 1) * d
            d += 1

    # Вывод ответа
    print(ways)

if __name__ == '__main__':
    main()

```

---

Задача 12. Эффективная быстрая сортировка 

**Условие задачи:**
Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач.  При равенстве числа решенных задач первым идет участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке. Ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place"). 

**Решение на Python:**

```python
import sys

# Расширение лимита рекурсии для глубоких вызовов quick sort
sys.setrecursionlimit(20000)

def compare(a, b):
    # Сравнение двух участников (логин, задачи, штраф)
    if a[1] != b[1]:
        return a[1] > b[1]  # По убыванию количества решенных задач
    if a[2] != b[2]:
        return a[2] < b[2]  # По возрастанию штрафа
    return a[0] < b[0]      # Лексикографически по логину

def partition(arr, low, high):
    # Опорный элемент выбирается в середине
    pivot = arr[(low + high) // 2]
    i = low
    j = high
    while i <= j:
        # Движение указателей до нахождения элементов на неверной стороне
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
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p, high)

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
    n = int(lines[0])
    arr = []
    
    # Чтение данных участников
    idx = 1
    for _ in range(n):
        login = lines[idx]
        tasks = int(lines[idx+1])
        penalty = int(lines[idx+2])
        arr.append((login, tasks, penalty))
        idx += 3

    # Вызов in-place сортировки
    quick_sort_inplace(arr, 0, n - 1)

    # Вывод логинов в отсортированном порядке
    for item in arr:
        print(item[0])

if __name__ == '__main__':
    main()

```

---

Задача 15. Оболочка. 

**Условие задачи:**
Имеется массив из N целочисленных точек на плоскости. Требуется найти периметр наименьшего охватывающего многоугольника, содержащего все точки. Одно вещественное число периметр требуемого многоугольника с двумя знаками после запятой. 

**Решение на Python:**

```python
import math
import sys

def cross_product(o, a, b):
    # Вычисление векторного произведения для проверки направления поворота (левый/правый)
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    # Сортировка точек в лексикографическом порядке
    points = sorted(points)
    if len(points) <= 1:
        return points

    # Построение нижней части оболочки
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Построение верхней части оболочки
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Объединение нижнего и верхнего контуров (исключая дубликаты на краях)
    return lower[:-1] + upper[:-1]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    points = []
    
    idx = 1
    for _ in range(n):
        points.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    # Построение выпуклой оболочки (Алгоритм Грэхема/Монотонная цепь)
    hull = convex_hull(points)

    # Вычисление периметра
    perimeter = 0.0
    for i in range(len(hull)):
        perimeter += distance(hull[i], hull[(i + 1) % len(hull)])

    # Вывод результата с точностью до 2-х знаков
    print(f"{perimeter:.2f}")

if __name__ == '__main__':
    main()

```

---

Задача 16. Очень быстрая сортировка. 

**Условие задачи:**
Имеется рекуррентная последовательность А1, А2, ... AN, строящаяся по следующему правилу: $A1=K$, $Ai+1 = (Ai \times M) \pmod{2^{32}-1} \pmod L$. Требуется найти сумму всех нечетных по порядку элементов в отсортированной по неубыванию последовательности по модулю L. 

**Решение на Python:**

```python
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    L = int(input_data[3])

    # Инициализация массива 
    a = [0] * N
    a[0] = K
    MOD = 0xFFFFFFFF  # 2^32 - 1

    # Заполнение массива по формуле
    for i in range(N - 1):
        a[i+1] = ((a[i] * M) % MOD) % L

    # Быстрая сортировка (встроенный Timsort в Python высоко оптимизирован)
    a.sort()

    # Суммирование элементов, стоящих на нечетных местах по порядку 
    # (то есть с четными индексами: 0, 2, 4...) по модулю L.
    res = 0
    for i in range(0, N, 2):
        res = (res + a[i]) % L

    print(res)

if __name__ == '__main__':
    main()

```

---

Задача 18. Музей. 

**Условие задачи:**
В музее регистрируется в течение суток время прихода и ухода каждого посетителя. Требуется найти максимальное число посетителей, которые находились в музее одновременно. В каждой строке располагается отрезок времени посещения в формате «ЧЧ:ММ ЧЧ:ММ» $(00:00\le ЧЧ:ММ\le23:59)$. 

**Решение на Python:**

```python
import sys

def time_to_minutes(t_str):
    h, m = map(int, t_str.split(':'))
    return h * 60 + m

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    events = []

    idx = 1
    for _ in range(n):
        arrive = time_to_minutes(input_data[idx])
        depart = time_to_minutes(input_data[idx+1])
        
        # Создание событий. Для максимального перекрытия при совпадении времени 
        # событие "приход" (0) должно обрабатываться раньше события "уход" (1).
        events.append((arrive, 0, 1))   # 1 - увеличение количества посетителей
        events.append((depart, 1, -1))  # -1 - уменьшение количества посетителей
        idx += 2

    # Сортировка событий по времени, а затем по типу события
    events.sort()

    current_visitors = 0
    max_visitors = 0

    # Обработка событий в хронологическом порядке (алгоритм заметающей прямой)
    for time, event_type, change in events:
        current_visitors += change
        if current_visitors > max_visitors:
            max_visitors = current_visitors

    print(max_visitors)

if __name__ == '__main__':
    main()

```

---

Задача 22. Миллиардеры 

**Условие задачи:**
Ваш работодатель просит посчитать, сколько дней в течение этого периода каждый из городов мира был первым по общей сумме денег миллиардеров, находящихся в нём. Вы можете считать, что миллиардеры путешествуют не чаще одного раза в день, и что они отбывают поздно вечером и прибывают в город назначения рано утром следующего дня. Города должны быть отсортированы по алфавиту. 

**Решение на Python:**

```python
import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1

    person_city = {}
    person_wealth = {}
    city_wealth = defaultdict(int)

    # Чтение данных о миллиардерах и инициализация состояния на первый день
    for _ in range(n):
        name = input_data[idx]
        city = input_data[idx+1]
        wealth = int(input_data[idx+2])
        person_city[name] = city
        person_wealth[name] = wealth
        city_wealth[city] += wealth
        idx += 3

    m = int(input_data[idx])
    k = int(input_data[idx+1])
    idx += 2

    # Сохранение перемещений, сгруппированных по дням
    movements = defaultdict(list)
    for _ in range(k):
        day = int(input_data[idx])
        name = input_data[idx+1]
        dest = input_data[idx+2]
        movements[day].append((name, dest))
        idx += 3

    # Поддержка словаря для быстрого поиска городов с максимальным капиталом
    wealth_cities = defaultdict(set)
    for city, w in city_wealth.items():
        if w > 0:
            wealth_cities[w].add(city)

    max_wealth = max(wealth_cities.keys()) if wealth_cities else 0
    days_led = defaultdict(int)

    # Симуляция изменения состояний по дням
    for day in range(1, m + 1):
        # Начисление баллов (дней лидерства) текущим лидерам
        if max_wealth > 0:
            for city in wealth_cities[max_wealth]:
                days_led[city] += 1

        # Обновление дислокаций миллиардеров вечером
        if day in movements:
            for name, new_city in movements[day]:
                old_city = person_city[name]
                if old_city == new_city:
                    continue

                w = person_wealth[name]

                # Вычитание из капитала старого города
                old_w = city_wealth[old_city]
                wealth_cities[old_w].remove(old_city)
                if not wealth_cities[old_w]:
                    del wealth_cities[old_w]
                
                city_wealth[old_city] -= w
                if city_wealth[old_city] > 0:
                    wealth_cities[city_wealth[old_city]].add(old_city)

                # Добавление к капиталу нового города
                new_w = city_wealth[new_city]
                if new_city in wealth_cities.get(new_w, set()):
                    wealth_cities[new_w].remove(new_city)
                    if not wealth_cities[new_w]:
                        del wealth_cities[new_w]
                        
                city_wealth[new_city] += w
                wealth_cities[city_wealth[new_city]].add(new_city)
                person_city[name] = new_city

            # Пересчет значения максимального капитала среди всех городов
            max_wealth = max(wealth_cities.keys()) if wealth_cities else 0

    # Вывод результатов в алфавитном порядке
    for city in sorted(days_led.keys()):
        print(f"{city} {days_led[city]}")

if __name__ == '__main__':
    main()

```

---

Задача 26. Очередь с приоритетами 

**Условие задачи:**
Реализуйте очередь с приоритетами. Ваша очередь должна поддерживать следующие операции: добавить элемент, извлечь минимальный элемент, уменьшить элемент, добавленный во время одной из операций. В первой строке входного файла содержится число n - число операций с очередью. 

**Решение на Python:**

```python
import sys

class PriorityQueue:
    def __init__(self):
        # Очередь реализуется на основе массива (Min-Heap)
        self.heap = []
        # Словарь для отслеживания позиции элемента в куче по ID операции
        self.id_to_idx = {}

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.id_to_idx[self.heap[i][1]] = i
        self.id_to_idx[self.heap[j][1]] = j

    def sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] < self.heap[p][0]:
                self.swap(i, p)
                i = p
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < n and self.heap[right][0] < self.heap[left][0]:
                j = right
            if self.heap[i][0] <= self.heap[j][0]:
                break
            self.swap(i, j)
            i = j

    def push(self, val, op_id):
        self.heap.append((val, op_id))
        idx = len(self.heap) - 1
        self.id_to_idx[op_id] = idx
        self.sift_up(idx)

    def extract_min(self):
        if not self.heap:
            return '*'
        
        min_val = self.heap[0][0]
        op_id = self.heap[0][1]
        del self.id_to_idx[op_id]

        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.id_to_idx[last[1]] = 0
            self.sift_down(0)
            
        return min_val

    def decrease_key(self, op_id, new_val):
        if op_id in self.id_to_idx:
            idx = self.id_to_idx[op_id]
            self.heap[idx] = (new_val, op_id)
            self.sift_up(idx)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    op_id = 1
    pq = PriorityQueue()
    output = []

    # Обработка операций
    while idx < len(input_data):
        cmd = input_data[idx]
        if cmd == 'A':
            val = int(input_data[idx+1])
            pq.push(val, op_id)
            idx += 2
        elif cmd == 'X':
            output.append(str(pq.extract_min()))
            idx += 1
        elif cmd == 'D':
            x = int(input_data[idx+1])
            y = int(input_data[idx+2])
            pq.decrease_key(x, y)
            idx += 3
        op_id += 1  # ID инкрементируется с каждой операцией, как и строки в условии

    print('\n'.join(output))

if __name__ == '__main__':
    main()

```

---

Задача 31. Четность 

**Условие задачи:**
Ваш друг записывает последовательность, состоящую из нулей и единиц. Вы выбираете непрерывную подпоследовательность и спрашиваете его, чётное или нечётное количество единиц содержит эта подпоследовательность. Ваша задача найти первый ответ, который гарантированно неверен. Каждая строка содержит один вопрос и ответ на этот вопрос: два целых числа и одно слово "even" или "odd". 

**Решение на Python:**

```python
import sys

# Структура Система Непересекающихся Множеств с поддержкой четности расстояний (DSU)
class DSU:
    def __init__(self):
        self.parent = {}
        self.parity = {}

    def find(self, i):
        # Инициализация нового элемента
        if i not in self.parent:
            self.parent[i] = i
            self.parity[i] = 0
            return i
        
        if self.parent[i] == i:
            return i

        # Сжатие пути с пересчетом четности по отношению к корню
        root = self.find(self.parent[i])
        self.parity[i] ^= self.parity[self.parent[i]]
        self.parent[i] = root
        return root

    def union(self, i, j, p):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            # Если элементы уже связаны, проверяем не противоречит ли текущая четность сохраненной
            return (self.parity[i] ^ self.parity[j]) == p

        # Объединение деревьев и обновление четности корня
        self.parent[root_i] = root_j
        self.parity[root_i] = self.parity[i] ^ self.parity[j] ^ p
        return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        length_str = input_data[idx]
        if length_str == '-1':
            break
            
        idx += 1
        queries_count = int(input_data[idx])
        idx += 1

        dsu = DSU()
        consistent_count = queries_count
        contradiction_found = False

        for q in range(queries_count):
            # Конвертация интервалов в индексы для префиксных сумм
            left = int(input_data[idx]) - 1
            right = int(input_data[idx+1])
            parity_str = input_data[idx+2]
            idx += 3

            if contradiction_found:
                continue

            p = 0 if parity_str == "even" else 1

            # Поиск противоречия
            if not dsu.union(left, right, p):
                consistent_count = q
                contradiction_found = True

        print(consistent_count)

if __name__ == '__main__':
    main()

```

