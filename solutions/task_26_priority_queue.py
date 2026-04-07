# Задача 26: Очередь с приоритетами
#
# Реализуйте очередь с приоритетами.
# Очередь должна поддерживать следующие операции:
# - A x — добавить элемент x в очередь
# - X — извлечь минимальный элемент (вывести его значение или "*", если очередь пуста)
# - D x y — уменьшить элемент, добавленный операцией x, до значения y
#
# Вход: список операций в виде кортежей, например:
#   [("A", 10), ("A", 20), ("D", 2, 5), ("X",)]
# Выход: список результатов операций X (числа или "*")


class PriorityQueue:
    def __init__(self):
        self.heap = []
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
            return "*"

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


def priority_queue(operations):
    pq = PriorityQueue()
    result = []
    op_id = 0

    for op in operations:
        op_id += 1
        if op[0] == "A":
            pq.push(op[1], op_id)
        elif op[0] == "X":
            result.append(pq.extract_min())
        elif op[0] == "D":
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
