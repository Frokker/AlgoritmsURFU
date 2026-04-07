import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import zipfile

    solutions = {
        "task_01_nearest_zero.py": """# Чтение входных данных
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
    """,

        "task_05_long_arithmetic.py": """# Чтение входных данных
    a = int(input().strip())
    op = input().strip()
    b = int(input().strip())

    # В Python реализована встроенная поддержка длинной арифметики
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    """,

        "task_09_tree_cutting.py": """import sys

    def main():
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        n = int(input_data[0])
        m = int(input_data[1])

        ways = 0
    
        if m == 0:
            ways = 1
        elif m == 1:
            ways = n
        else:
            d = 1
            while (m - 1) * d < n:
                ways += n - (m - 1) * d
                d += 1

        print(ways)

    if __name__ == '__main__':
        main()
    """,

        "task_12_effective_quick_sort.py": """import sys

    sys.setrecursionlimit(20000)

    def compare(a, b):
        if a[1] != b[1]:
            return a[1] > b[1]
        if a[2] != b[2]:
            return a[2] < b[2]
        return a[0] < b[0]

    def partition(arr, low, high):
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
    
        idx = 1
        for _ in range(n):
            login = lines[idx]
            tasks = int(lines[idx+1])
            penalty = int(lines[idx+2])
            arr.append((login, tasks, penalty))
            idx += 3

        quick_sort_inplace(arr, 0, n - 1)

        for item in arr:
            print(item[0])

    if __name__ == '__main__':
        main()
    """,

        "task_15_convex_hull.py": """import math
    import sys

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def convex_hull(points):
        points = sorted(points)
        if len(points) <= 1:
            return points

        lower = []
        for p in points:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

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

        hull = convex_hull(points)

        perimeter = 0.0
        for i in range(len(hull)):
            perimeter += distance(hull[i], hull[(i + 1) % len(hull)])

        print(f"{perimeter:.2f}")

    if __name__ == '__main__':
        main()
    """,

        "task_16_very_fast_sort.py": """import sys

    def main():
        input_data = sys.stdin.read().split()
        if not input_data:
            return
    
        N = int(input_data[0])
        K = int(input_data[1])
        M = int(input_data[2])
        L = int(input_data[3])

        a = [0] * N
        a[0] = K
        MOD = 0xFFFFFFFF

        for i in range(N - 1):
            a[i+1] = ((a[i] * M) % MOD) % L

        a.sort()

        res = 0
        for i in range(0, N, 2):
            res = (res + a[i]) % L

        print(res)

    if __name__ == '__main__':
        main()
    """,

        "task_18_museum.py": """import sys

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
        
            events.append((arrive, 0, 1))
            events.append((depart, 1, -1))
            idx += 2

        events.sort()

        current_visitors = 0
        max_visitors = 0

        for time, event_type, change in events:
            current_visitors += change
            if current_visitors > max_visitors:
                max_visitors = current_visitors

        print(max_visitors)

    if __name__ == '__main__':
        main()
    """,

        "task_22_billionaires.py": """import sys
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

        movements = defaultdict(list)
        for _ in range(k):
            day = int(input_data[idx])
            name = input_data[idx+1]
            dest = input_data[idx+2]
            movements[day].append((name, dest))
            idx += 3

        wealth_cities = defaultdict(set)
        for city, w in city_wealth.items():
            if w > 0:
                wealth_cities[w].add(city)

        max_wealth = max(wealth_cities.keys()) if wealth_cities else 0
        days_led = defaultdict(int)

        for day in range(1, m + 1):
            if max_wealth > 0:
                for city in wealth_cities[max_wealth]:
                    days_led[city] += 1

            if day in movements:
                for name, new_city in movements[day]:
                    old_city = person_city[name]
                    if old_city == new_city:
                        continue

                    w = person_wealth[name]

                    old_w = city_wealth[old_city]
                    wealth_cities[old_w].remove(old_city)
                    if not wealth_cities[old_w]:
                        del wealth_cities[old_w]
                
                    city_wealth[old_city] -= w
                    if city_wealth[old_city] > 0:
                        wealth_cities[city_wealth[old_city]].add(old_city)

                    new_w = city_wealth[new_city]
                    if new_city in wealth_cities.get(new_w, set()):
                        wealth_cities[new_w].remove(new_city)
                        if not wealth_cities[new_w]:
                            del wealth_cities[new_w]
                        
                    city_wealth[new_city] += w
                    wealth_cities[city_wealth[new_city]].add(new_city)
                    person_city[name] = new_city

                max_wealth = max(wealth_cities.keys()) if wealth_cities else 0

        for city in sorted(days_led.keys()):
            print(f"{city} {days_led[city]}")

    if __name__ == '__main__':
        main()
    """,

        "task_26_priority_queue.py": """import sys

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
            op_id += 1  

        print('\\n'.join(output))

    if __name__ == '__main__':
        main()
    """,

        "task_31_parity.py": """import sys

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
                left = int(input_data[idx]) - 1
                right = int(input_data[idx+1])
                parity_str = input_data[idx+2]
                idx += 3

                if contradiction_found:
                    continue

                p = 0 if parity_str == "even" else 1

                if not dsu.union(left, right, p):
                    consistent_count = q
                    contradiction_found = True

            print(consistent_count)

    if __name__ == '__main__':
        main()
    """
    }

    archive_name = 'solutions.zip'

    # Создание zip-архива и запись в него файлов
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename, code in solutions.items():
            zipf.writestr(filename, code.strip() + '\n')

    print(f"Готово! Архив '{archive_name}' успешно создан в текущей директории.")
    return


if __name__ == "__main__":
    app.run()
