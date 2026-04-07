"""
Задача 31: Чётность (DSU с чётностью)

Есть скрытая последовательность из 0 и 1. Серия утверждений:
«в отрезке [l, r] чётное/нечётное число единиц».
Найти номер первого ложного утверждения.

Ключевое наблюдение — сведение к префиксным суммам:
  S[i] = сумма первых i элементов (mod 2).
  Сумма на [l, r] mod 2 = S[r] XOR S[l-1].
  «Чётное» = S[r] и S[l-1] одной чётности (XOR = 0).
  «Нечётное» = разной чётности (XOR = 1).

Используем DSU (Union-Find) с хранением чётности пути:
  - Каждый элемент хранит parity — чётность расстояния до корня.
  - find(x) — находит корень, сжимая путь и XOR-я чётности.
  - union(a, b, p) — если a и b уже в одном множестве, проверяем
    совпадает ли parity[a] XOR parity[b] с p. Если нет — противоречие.

Сложность: O(n * alpha(n)) ~ O(n) на практике.
"""


class DSU:
    """Система непересекающихся множеств с хранением чётности."""

    def __init__(self):
        self.parent = {}   # элемент -> родитель
        self.parity = {}   # элемент -> чётность пути до родителя (0 или 1)

    def find(self, i):
        """Находит корень множества с сжатием пути.
        Попутно XOR-ит чётности, чтобы parity[i] отражало
        чётность пути от i до корня."""
        if i not in self.parent:
            # Новый элемент — сам себе корень, чётность 0
            self.parent[i] = i
            self.parity[i] = 0
            return i

        if self.parent[i] == i:
            return i

        # Рекурсивно находим корень
        root = self.find(self.parent[i])
        # Обновляем чётность: XOR с чётностью пути родителя до корня
        self.parity[i] ^= self.parity[self.parent[i]]
        # Сжатие пути — подвешиваем напрямую к корню
        self.parent[i] = root
        return root

    def union(self, i, j, p):
        """Объединяет множества элементов i и j с ожидаемой чётностью p.

        Возвращает True, если всё непротиворечиво.
        Возвращает False, если новое утверждение противоречит накопленным."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            # Элементы уже в одном множестве — проверяем
            # Фактическая чётность: parity[i] XOR parity[j]
            # Ожидаемая: p
            return (self.parity[i] ^ self.parity[j]) == p

        # Объединяем: подвешиваем root_i к root_j
        self.parent[root_i] = root_j
        # Чётность ребра root_i -> root_j вычисляется так,
        # чтобы parity[i] XOR ... XOR parity[root_i->root_j] XOR ... XOR parity[j] == p
        self.parity[root_i] = self.parity[i] ^ self.parity[j] ^ p
        return True


def parity_check(length, queries):
    """Проверяет последовательность утверждений о чётности.

    Args:
        length: длина исходной последовательности.
        queries: список кортежей (left, right, "even"/"odd").

    Returns:
        Индекс первого противоречивого утверждения (0-based),
        или len(queries) если противоречий нет.
    """
    dsu = DSU()

    for idx, (left, right, parity_str) in enumerate(queries):
        p = 0 if parity_str == "even" else 1
        # Представляем отрезок [left, right] через префиксные суммы:
        # sum[left..right] = S[right] XOR S[left-1]
        if not dsu.union(left - 1, right, p):
            return idx  # противоречие найдено

    return len(queries)  # все утверждения непротиворечивы


if __name__ == "__main__":
    # Пример 1: нет противоречий
    queries = [(1, 2, "even"), (3, 4, "odd")]
    print(parity_check(10, queries))  # 2

    # Пример 2: немедленное противоречие
    queries = [(1, 2, "even"), (1, 2, "odd")]
    print(parity_check(10, queries))  # 1

    # Пример 3: цепочка без противоречий
    queries = [
        (1, 2, "odd"),
        (2, 3, "odd"),
        (1, 3, "even"),  # odd + odd = even — непротиворечиво
    ]
    print(parity_check(10, queries))  # 3
