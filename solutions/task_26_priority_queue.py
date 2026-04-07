"""
Задача 26: Очередь с приоритетами

Реализовать очередь с приоритетами на основе бинарной кучи (min-heap).
Поддерживаемые операции:
  A x   — добавить элемент x в очередь.
  X     — извлечь минимальный элемент (или "*", если очередь пуста).
  D x y — уменьшить элемент, добавленный операцией x, до значения y.

Куча — это массив, организованный как дерево:
  Родитель i:      (i-1) // 2
  Левый потомок:   2*i + 1
  Правый потомок:  2*i + 2

Минимум всегда в корне (heap[0]).

Три ключевые операции:
  push:         добавить в конец → sift_up (всплытие наверх)
  extract_min:  забрать корень, поставить последний → sift_down (погружение)
  decrease_key: уменьшить значение → sift_up (элемент мог стать меньше родителя)

Словарь id_to_idx нужен для decrease_key: чтобы за O(1)
найти элемент в куче по номеру операции, а не искать за O(n).

Сложность: push, extract_min, decrease_key — всё O(log n).
"""


class PriorityQueue:
    def __init__(self):
        self.heap = []         # массив пар (значение, id_операции)
        self.id_to_idx = {}    # id_операции → индекс в heap

    def swap(self, i, j):
        """Меняет два элемента местами и обновляет словарь индексов."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.id_to_idx[self.heap[i][1]] = i
        self.id_to_idx[self.heap[j][1]] = j

    def sift_up(self, i):
        """Всплытие: пока элемент меньше родителя — меняем местами."""
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] < self.heap[p][0]:
                self.swap(i, p)
                i = p
            else:
                break

    def sift_down(self, i):
        """Погружение: пока элемент больше одного из потомков —
        меняем с МЕНЬШИМ потомком."""
        n = len(self.heap)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            # Выбираем меньшего из двух потомков
            j = left
            if right < n and self.heap[right][0] < self.heap[left][0]:
                j = right
            # Если текущий уже не больше — стоп
            if self.heap[i][0] <= self.heap[j][0]:
                break
            self.swap(i, j)
            i = j

    def push(self, val, op_id):
        """Добавляет элемент в конец кучи и всплывает его."""
        self.heap.append((val, op_id))
        idx = len(self.heap) - 1
        self.id_to_idx[op_id] = idx
        self.sift_up(idx)

    def extract_min(self):
        """Извлекает и возвращает минимальный элемент (корень).
        Если куча пуста — возвращает '*'."""
        if not self.heap:
            return "*"

        min_val = self.heap[0][0]
        op_id = self.heap[0][1]
        del self.id_to_idx[op_id]

        # Ставим последний элемент на место корня
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.id_to_idx[last[1]] = 0
            self.sift_down(0)  # погружаем его вниз

        return min_val

    def decrease_key(self, op_id, new_val):
        """Уменьшает значение элемента (по id операции) и всплывает его."""
        if op_id in self.id_to_idx:
            idx = self.id_to_idx[op_id]
            self.heap[idx] = (new_val, op_id)
            self.sift_up(idx)  # значение уменьшилось — может всплыть


def priority_queue(operations):
    """Обрабатывает список операций и возвращает результаты X-операций.

    Операции задаются кортежами:
      ("A", x)    — добавить x
      ("X",)      — извлечь минимум
      ("D", x, y) — уменьшить элемент операции x до y
    """
    pq = PriorityQueue()
    result = []
    op_id = 0  # счётчик операций (нумерация с 1)

    for op in operations:
        op_id += 1
        if op[0] == "A":
            pq.push(op[1], op_id)
        elif op[0] == "X":
            result.append(pq.extract_min())
        elif op[0] == "D":
            # op[1] = номер операции, op[2] = новое значение
            pq.decrease_key(op[1], op[2])

    return result


if __name__ == "__main__":
    # Пример 1: добавить и извлечь
    ops = [("A", 10), ("A", 5), ("X",)]
    print(priority_queue(ops))  # [5]

    # Пример 2: извлечение из пустой очереди
    ops = [("X",)]
    print(priority_queue(ops))  # ["*"]

    # Пример 3: уменьшение ключа
    ops = [("A", 10), ("A", 20), ("D", 2, 5), ("X",)]
    print(priority_queue(ops))  # [5]

    # Пример 4: несколько извлечений
    ops = [("A", 3), ("A", 1), ("A", 2), ("X",), ("X",), ("X",)]
    print(priority_queue(ops))  # [1, 2, 3]
