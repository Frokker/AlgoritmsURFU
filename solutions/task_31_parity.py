# Задача 31: Чётность (Parity)
#
# Ваш друг записывает последовательность из нулей и единиц.
# Вы выбираете непрерывную подпоследовательность и спрашиваете,
# чётное или нечётное количество единиц она содержит.
# Задача — найти номер первого ответа, который гарантированно неверен.
#
# Вход:
#   length — длина последовательности
#   queries — список кортежей (left, right, "even"/"odd")
# Выход:
#   номер первого противоречивого ответа (0-based индекс предыдущего),
#   или len(queries), если противоречий нет.
#
# Алгоритм: DSU (система непересекающихся множеств) с хранением чётности
# пути от элемента до корня.


class DSU:
    def __init__(self):
        self.parent = {}
        self.parity = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.parity[i] = 0
            return i

        if self.parent[i] == i:
            return i

        root = self.find(self.parent[i])
        self.parity[i] ^= self.parity[self.parent[i]]
        self.parent[i] = root
        return root

    def union(self, i, j, p):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return (self.parity[i] ^ self.parity[j]) == p

        self.parent[root_i] = root_j
        self.parity[root_i] = self.parity[i] ^ self.parity[j] ^ p
        return True


def parity_check(length, queries):
    dsu = DSU()

    for idx, (left, right, parity_str) in enumerate(queries):
        p = 0 if parity_str == "even" else 1
        # Используем left-1 и right, чтобы представить отрезок [left, right]
        # через разность префиксных сумм: sum[left..right] = prefix[right] - prefix[left-1]
        if not dsu.union(left - 1, right, p):
            return idx

    return len(queries)


if __name__ == "__main__":
    # Пример 1: нет противоречий
    queries = [(1, 2, "even"), (3, 4, "odd")]
    print(parity_check(10, queries))  # 2

    # Пример 2: немедленное противоречие
    queries = [(1, 2, "even"), (1, 2, "odd")]
    print(parity_check(10, queries))  # 1

    # Пример 3: противоречие на третьем запросе
    queries = [
        (1, 3, "even"),
        (1, 2, "even"),
        (2, 3, "odd"),  # противоречие: 1-3 even, 1-2 even => 2-3 должно быть even
    ]
    print(parity_check(10, queries))  # 2
