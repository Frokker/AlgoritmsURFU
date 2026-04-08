# Семинарские задачи

---

## Практика 1 (10.02.2026, 11.02.2026)

### Задача
Сгенерировать массив из 10 элементов, 1000 элементов, 1 млн элементов, отсортировать с помощью **пузырьковой сортировки**, замерить время выполнения и память.

### Пояснение
Пузырьковая сортировка (Bubble Sort) — простейший алгоритм сортировки, который многократно проходит по массиву и меняет местами соседние элементы, если они стоят в неправильном порядке. Сложность — **O(n²)**, поэтому на больших массивах (1 млн элементов) работает крайне медленно.

Для замера времени используется `time.perf_counter()`, а для замера памяти — модуль `tracemalloc`, который делает снапшоты до и после выполнения функции и вычисляет разницу.

### Решение

```python
from random import randint

array_10 = [randint(1, 1000) for _ in range(10)]
array_1k = [randint(1, 1000) for _ in range(1_000)]
array_1kk = [randint(1, 1000) for _ in range(1_000_000)]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

---

## Практика 2 (17.02.2026, 18.02.2026)

### Задача 1 — Множество на основе массива
Реализовать множество с помощью массива: создать, добавить элементы, проверить наличие, удалить элементы.

### Пояснение
Множество (set) — структура данных, хранящая только уникальные элементы. Здесь оно реализовано через обычный список: при добавлении проверяется, есть ли элемент уже в массиве. Операции `add`, `contains`, `remove` имеют сложность **O(n)**, поскольку требуется линейный поиск по массиву.

### Решение

```python
class OwnSet:
    def __init__(self, items=None):
        self._array = []
        if items:
            for el in items:
                self.add(el)

    def add(self, item):
        if item not in self._array:
            self._array.append(item)

    def contains(self, item):
        return item in self._array

    def remove(self, item):
        if item in self._array:
            self._array.remove(item)

    def __repr__(self):
        return f"OwnSet({self._array})"
```

---

### Задача 2 — Умножение Карацубы
Реализовать умножение двух многозначных чисел (15-значных, 30-значных) обычным способом и с применением **алгоритма Карацубы**, замерить время.

### Пояснение
Алгоритм Карацубы — метод быстрого умножения больших чисел. Вместо 4 рекурсивных умножений (как при «школьном» разбиении числа на две половины) он использует всего 3, за счёт трюка: `(a+b)*(c+d) - ac - bd = ad + bc`. Сложность — **O(n^1.585)** вместо **O(n²)**.

Числа разбиваются на старшую и младшую половины через `divmod`. Рекурсия продолжается, пока числа не станут однозначными.

### Решение

```python
def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * (10 ** (2 * half)) + ad_bc * (10 ** half) + bd
```

---

### Задача 3 — Числа Фибоначчи
Реализовать числа Фибоначчи рекурсивным способом.

### Пояснение
Числа Фибоначчи — последовательность, где каждый элемент равен сумме двух предыдущих: `F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)`. Рекурсивная реализация проста, но имеет экспоненциальную сложность **O(2^n)**, так как одни и те же подзадачи вычисляются многократно.

### Решение

```python
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## Практика 3 (24.02.2026)

### Задача
Сгенерировать массив из миллиона элементов, реализовать **Merge Sort** и **Quick Sort**, замерить время и память.

### Пояснение

**Merge Sort** (сортировка слиянием) — алгоритм «разделяй и властвуй». Массив рекурсивно делится пополам, пока не останутся одиночные элементы, затем половины сливаются в отсортированном порядке. Сложность — **O(n log n)** всегда, но требует дополнительную память O(n).

**Quick Sort** (быстрая сортировка) — выбирается опорный элемент (pivot), массив разбивается на три части: меньше, равные и больше pivot. Затем рекурсивно сортируются левая и правая части. Средняя сложность — **O(n log n)**, худший случай — **O(n²)**.

### Решение

```python
def merge_sort(arr: list[int]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    arr_l, arr_r, arr_e = [], [], []
    for el in arr:
        if el < pivot:
            arr_l.append(el)
        elif el > pivot:
            arr_r.append(el)
        else:
            arr_e.append(el)

    return quick_sort(arr_l) + arr_e + quick_sort(arr_r)
```

---

## Практика 4 (03.03.2026, 04.03.2026)

### Задача 1 — Пирамидальная сортировка
Реализовать пирамидальную сортировку, используя бинарную кучу.

### Пояснение
Heap Sort использует структуру данных **бинарная куча** (max-heap). Сначала массив превращается в max-heap, где каждый родитель больше своих потомков. Затем максимальный элемент (корень) ставится в конец массива, размер кучи уменьшается, и heapify вызывается заново. Сложность — **O(n log n)**, сортировка выполняется **in-place** (без дополнительной памяти).

Функция `heapify` восстанавливает свойство кучи для поддерева с корнем в индексе `i`. Левый потомок — `2i+1`, правый — `2i+2`.

### Решение

```python
def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
```

---

### Задача 2 — Бинарное дерево поиска
Реализовать бинарное дерево поиска (вставка, удаление, поиск).

### Пояснение
**Бинарное дерево поиска (BST)** — структура, где для каждого узла все элементы в левом поддереве меньше, а в правом — больше. Это обеспечивает поиск, вставку и удаление за **O(h)**, где h — высота дерева (в лучшем случае O(log n), в худшем — O(n)).

- **Поиск** — итеративный спуск от корня: идём влево, если ключ меньше, вправо — если больше.
- **Вставка** — рекурсивный спуск до пустого места, где создаётся новый узел.
- **Удаление** — три случая: нет потомков (просто удаляем), один потомок (заменяем узел потомком), два потомка (находим inorder-преемника — минимум в правом поддереве — и заменяем значение).

### Решение

```python
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        current = self.root
        while current is not None and current.val != key:
            current = current.left if key < current.val else current.right
        return current

    def insert(self, val: int):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.val = successor.val
                node.right = self._delete(node.right, successor.val)
        return node
```

---

## Практика 5 (17.03.2026, 18.03.2026)

### Задача
Реализовать **красно-чёрное дерево** (вставка элемента, поиск, удаление).

### Пояснение
Красно-чёрное дерево — самобалансирующееся BST, где каждый узел окрашен в красный или чёрный цвет. Правила:
1. Корень — чёрный.
2. Красный узел не может иметь красного потомка.
3. Все пути от корня до листьев содержат одинаковое количество чёрных узлов.

Это гарантирует высоту **O(log n)** и, соответственно, все операции за **O(log n)**.

- **Вставка** — новый узел всегда красный. После вставки вызывается `_fix_insert`, который через перекраску и повороты (left/right rotate) восстанавливает свойства дерева.
- **Повороты** — локальные операции, меняющие структуру дерева без нарушения порядка BST.
- **Удаление** — находим узел, заменяем его преемником (transplant), при необходимости восстанавливаем баланс.

### Решение

```python
from enum import Enum

class ColorTree(Enum):
    Red = 'red'
    Black = 'black'

class Node:
    def __init__(self, val, left=None, right=None, parent=None, color=ColorTree.Red):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            self.root.color = ColorTree.Black
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, node: Node):
        while node.parent is not None and node.parent.color == ColorTree.Red:
            grandpa = node.parent.parent

            if node.parent == grandpa.left:
                uncle = grandpa.right
                if uncle is not None and uncle.color == ColorTree.Red:
                    node.parent.color = ColorTree.Black
                    uncle.color = ColorTree.Black
                    grandpa.color = ColorTree.Red
                    node = grandpa
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = ColorTree.Black
                    grandpa.color = ColorTree.Red
                    self._right_rotate(grandpa)
            else:
                uncle = grandpa.left
                if uncle is not None and uncle.color == ColorTree.Red:
                    node.parent.color = ColorTree.Black
                    uncle.color = ColorTree.Black
                    grandpa.color = ColorTree.Red
                    node = grandpa
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = ColorTree.Black
                    grandpa.color = ColorTree.Red
                    self._left_rotate(grandpa)

        self.root.color = ColorTree.Black

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            x.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            x.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            elif val >= current.val:
                current = current.right
        return None

    def delete(self, val):
        node = self.search(val)
        if node is None:
            return

        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.val = successor.val
            self._transplant(successor, successor.right)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
```

---

## Практика 6 (25.03.2026, 26.03.2026)

### Задача
Реализовать **хэш-таблицу** с двумя способами разрешения коллизий.

### Пояснение
Хэш-таблица — структура данных, обеспечивающая доступ к элементам по ключу за **O(1)** в среднем. Ключ преобразуется хэш-функцией в индекс массива (bucket). При совпадении индексов возникает **коллизия**.

Два способа разрешения коллизий:

1. **Метод цепочек (Chaining)** — каждая ячейка содержит список пар `[ключ, значение]`. При коллизии новая пара добавляется в список. Поиск — линейный проход по списку в ячейке.

2. **Открытая адресация (Open Addressing)** — при коллизии ищется следующая свободная ячейка (линейное пробирование). Вставка и поиск проходят по ячейкам, начиная с вычисленного индекса, пока не найдут нужный ключ или пустую ячейку.

### Решение

```python
class HashTable:
    def __init__(self, size=64):
        self.bucket = [None] * size
        self.size = size

    def put(self, key, value):
        indx = hash(key) % self.size
        self.bucket[indx] = [key, value]

    def get(self, key):
        indx = hash(key) % self.size
        if self.bucket[indx] is not None:
            return self.bucket[indx][1]
        return None

    def delete(self, key):
        indx = hash(key) % self.size
        self.bucket[indx] = None


class HashTableWithChaining(HashTable):
    def __init__(self, size=64):
        super().__init__(size)
        self.bucket = [[] for _ in range(size)]

    def put(self, key, value):
        indx = hash(key) % self.size
        for el in self.bucket[indx]:
            if el[0] == key:
                el[1] = value
                return
        self.bucket[indx].append([key, value])

    def get(self, key):
        indx = hash(key) % self.size
        if self.bucket[indx] == []:
            return None
        for el in self.bucket[indx]:
            if el[0] == key:
                return el[1]
        return None

    def delete(self, key):
        indx = hash(key) % self.size
        self.bucket[indx] = [el for el in self.bucket[indx] if el[0] != key]


class HashTableOpenAddressing(HashTable):
    def __init__(self, size=64):
        super().__init__(size)

    def put(self, key, value):
        indx = hash(key) % self.size
        for i in range(indx, 2 * self.size):
            i = i % self.size
            if self.bucket[i] is None:
                self.bucket[i] = [key, value]
                return

    def get(self, key):
        indx = hash(key) % self.size
        for i in range(indx, 2 * self.size):
            i = i % self.size
            if self.bucket[i] is None:
                return None
            elif self.bucket[i][0] == key:
                return self.bucket[i][1]

    def delete(self, key):
        indx = hash(key) % self.size
        for i in range(indx, 2 * self.size):
            i = i % self.size
            if self.bucket[i] is None:
                return None
            elif self.bucket[i][0] == key:
                self.bucket[i] = None
```

---

## Практика 7 (31.03.2026, 01.04.2026)

### Задача
Реализовать **алгоритм Хаффмана**.

### Пояснение
Алгоритм Хаффмана — метод сжатия данных без потерь. Он строит оптимальный префиксный код, где часто встречающиеся символы получают короткие коды, а редкие — длинные.

Алгоритм:
1. Подсчитать частоту каждого символа в строке.
2. Создать листовые узлы для каждого символа и поместить их в min-heap (приоритетная очередь по частоте).
3. Пока в куче больше одного элемента: извлечь два узла с наименьшей частотой, создать новый узел с их суммарной частотой и добавить обратно.
4. Оставшийся узел — корень дерева Хаффмана.
5. Обход дерева: влево — `0`, вправо — `1`. Путь от корня до листа — код символа.

**Декодирование** — проход по битовой строке с навигацией по дереву: `0` — влево, `1` — вправо, при достижении листа — записываем символ и возвращаемся к корню.

### Решение

```python
import heapq

class Node:
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.right = right
        self.left = left

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_codes(node: Node, current_code: str, codes_dict: dict):
    if node.symbol:
        codes_dict[node.symbol] = current_code
    else:
        build_codes(node.left, current_code + '0', codes_dict)
        build_codes(node.right, current_code + '1', codes_dict)

def HaffmanEncode(line: str):
    queque = list(line)
    freq_els = dict()
    for el in queque:
        freq_els[el] = freq_els.get(el, 0) + 1

    heap = []
    for symbol, frequency in freq_els.items():
        heapq.heappush(heap, Node(symbol, frequency))

    while len(heap) > 1:
        el_1, el_2 = heapq.heappop(heap), heapq.heappop(heap)
        new_el = Node(None, el_1.frequency + el_2.frequency, el_1, el_2)
        heapq.heappush(heap, new_el)

    root = heap[0]
    codes_dict = dict()
    build_codes(root, "", codes_dict)
    encoded = ""
    for char in line:
        encoded += codes_dict[char]

    return encoded, root

def HaffmanDecode(encoded: str, root: Node) -> str:
    decoded = ""
    current = root
    for bit in encoded:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.symbol is not None:
            decoded += current.symbol
            current = root

    return decoded
```
