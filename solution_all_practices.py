
import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import time
    import tracemalloc
    import gc  # Для очистки перед замером

    def profile_my_code(func):
        def wrapper(*args, **kwargs):
            # Очищаем перед замером 
            gc.collect()

            # Снапшот ДО выполнения
            tracemalloc.start(10)  # 10 фреймов для traceback
            snapshot_before = tracemalloc.take_snapshot()
            start_time = time.perf_counter()

            result = func(*args, **kwargs)  

            end_time = time.perf_counter()
            snapshot_after = tracemalloc.take_snapshot()
            tracemalloc.stop()

            # Diff памяти (пиковое потребление func)
            top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')
            peak_mem = sum(stat.size_diff for stat in top_stats if stat.size_diff > 0)

            print(f"Время выполнения: {end_time - start_time:.4f} сек")
            print(f"Пиковое потребление памяти: {peak_mem / 1024:.2f} КБ")
            return result  
        return wrapper


    return (profile_my_code,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Практика 1. 10.02.2026, 11.02.2026.
    ### Сгенерировать массив из 10 элементов, 1000 элементов, 1млн элементов, отсортировать с помощью пузырьковой сортировки, замерить время выполнения и память
    """)
    return


@app.cell
def _(profile_my_code):
    from random import randint

    array_10 = [randint(1, 1000) for _ in range(10)]
    array_1k = [randint(1, 1000) for _ in range(1_000)]
    array_1kk = [randint(1, 1000) for _ in range(1_000_000)]

    @profile_my_code
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                   arr[j], arr[j + 1] = arr[j + 1], arr[j] 
        return arr

    print(f'Массив из 10 элементов:')
    bubbleSort(array_10)
    print(f'\nМассив из 1_000 элементов:')
    # bubbleSort(array_1k)
    print(f'\nМассив из 1_000_000 элементов:')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Практика 2. 17.02.2026, 18.02.2026.

    ### Реализовать множество с помощью массива:
    ### 1.Создать.
    ### 2.Добавить элементы.
    ### 3.Проверить наличие элементов.
    ### 4.Удалить элементы.

    ### Реализовать умножение двух многозначных чисел (15-тизначных, 30-значных) сначала обычным способом, замерить время.
    ### Далее выполнить умножение с применением алгоритма Карацубы, замерить время выполнения.

    ### Реализовать числа Фибоначчи рекурсивным способом.
    """)
    return


@app.cell
def _():
    # Задача 1: Множество на основе массива
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

    s = OwnSet([1, 2, 3, 3, 2])
    print(s)              # OwnSet([1, 2, 3])
    s.add(4)
    print(s.contains(3))  # True
    s.remove(2)
    print(s)              # OwnSet([1, 3, 4])

    return


@app.cell
def _(profile_my_code):
    # Задача 2: Умножение Карацубы
    def karatsuba(x: int, y: int) -> int:
        if x < 10 or y < 10:
            return x * y

        n = max(len(str(x)), len(str(y)))
        half = n // 2

        # Разделяем числа на две половины
        power = 10 ** half
        a, b = divmod(x, power)  # x = a * 10^half + b
        c, d = divmod(y, power)  # y = c * 10^half + d

        # Три рекурсивных умножения вместо четырёх
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd

        return ac * (10 ** (2 * half)) + ad_bc * (10 ** half) + bd

    # Обычное умножение
    @profile_my_code
    def normal_multiply(x, y):
        return x * y

    # Умножение Карацубы
    @profile_my_code
    def karatsuba_multiply(x, y):
        return karatsuba(x, y)

    x_15 = 123456789012345
    y_15 = 987654321098765

    print("15-значные числа:")
    print("Обычное умножение:")
    normal_multiply(x_15, y_15)
    print("Карацуба:")
    karatsuba_multiply(x_15, y_15)

    return


@app.cell
def _():
    # Задача 3: Числа Фибоначчи рекурсивно
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(15):
        print(f"fib({i}) = {fibonacci(i)}")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Практика 3. 24.02.2026

    ### Сгенерировать массив из миллиона элементов, далее реализовать сортировки Merge Sort, Quick Sort, замерить время и память.
    """)
    return


@app.cell
def _():
    
    def merge_sort(arr:list[int]):
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
            
        
        
    
    
    
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Практика 4. 03.03.2026, 04.03.2026
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## № 1:
    ## Реализовать пирамидальную сортировку, используя бинарную кучу
    """)
    return


@app.cell
def _():
    def heapify(arr: list[int], n: int, i: int) -> None:
        largest = i

        l = 2*i + 1 
        r = 2*i + 2

        # Проверяем существует ли левый дочерний элемент больший, чем корень

        if l < n and arr[i] < arr[l]:
            largest = l

        # Проверяем существует ли правый дочерний элемент больший, чем корень

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:

            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)


    def heapSort(arr: list[int]) -> list[int]:
        n = len(arr)
        # корень a[i] - максимум
        for i in range(n, -1, -1):
            heapify(arr, n, i)


        # ставим максимальный эл. в конец и заново запускаем heapify для неотсортированного подмассива
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

        return arr


    return (heapSort,)


@app.cell
def _(heapSort):
    arr = [12, 11, 13, 5, 6, 7]
    print(heapSort(arr))

    for i in range(len(arr)):
        print ("%d" %arr[i]),
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## №2
    ## Реализовать бинарное дерево поиска (вставка, удаление, поиск)
    """)
    return


@app.cell
def _():
    class Node:
        def __init__ (self, val: int):
            self.val = val
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        # Итеративная версия (экономит память)
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
                # Нашли узел
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # находим преемника
                    successor = node.right
                    while successor.left is not None:
                        successor = successor.left
                    node.val = successor.val
                    node.right = self._delete(node.right, successor.val)
            return node


    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Практика 5. 17.03.2026, 18.03.2026


    ### Реализовать красно-черное дерево (вставка элемента, поиск, удаление)
    """)
    return


@app.cell
def _():
    from enum import Enum
    
    class ColorTree(Enum):
        Red='red'
        Black='black'
    
    class Node:
        def __init__(self, val, left=None, right=None, parent=None, color = ColorTree.Red):
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
                    
                    
        def _fix_insert(self, node:Node):
            
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
            x.left  = y.right
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
                # два дочерних узла есть
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
            

    return

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Практика 6. 25.03.2026, 26.03.2026


    ## Реализовать хэш-таблицу с двумя способами разрешения коллизий
    """)
    return


@app.cell
def _():
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




    class HashTableWithChaining (HashTable):
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
            for i in range(indx , 2 * self.size):
                i = i % self.size
                if self.bucket[i] is None:
                    self.bucket[i] = [key, value]
                    return

        def get(self, key):
            indx = hash(key) % self.size
            for i in range(indx , 2 * self.size):
                i = i % self.size
                if self.bucket[i] is None:
                    return None 
                elif self.bucket[i][0] == key:
                    return self.bucket[i][1]
       
                
        def delete(self, key):
            indx = hash(key) % self.size
            
            for i in range(indx , 2 * self.size):
                i = i % self.size
                if self.bucket[i] is None:
                    return None 
                elif self.bucket[i][0] == key:
                    self.bucket[i] = None

    return



@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Практика 7. 31.03.2026, 01.04.2026


    ### Реализовать алгоритм Хаффмана
    """)
    return


@app.cell
def _():
    import heapq

    class Node:
        def __init__(self, symbol, frequency, left=None, right=None):
            self.symbol = symbol
            self.frequency = frequency
            self.right = right
            self.left = left

        
        def __lt__(self, other):
            return self.frequency < other.frequency
            
    def build_codes(node: Node, current_code:str, codes_dict:dict):
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


    text = "aababbbbdddd"
    encoded, tree = HaffmanEncode(text)
    decoded = HaffmanDecode(encoded, tree)
    print(f"Исходная строка: {text}")
    print(f"Закодированная:  {encoded}")
    print(f"Раскодированная: {decoded}")
    
    return



if __name__ == "__main__":
    app.run()
