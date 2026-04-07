"""
Задача 22: Миллиардеры

Миллиардеры перемещаются между городами. Для каждого дня
определить, какой город лидирует по суммарному капиталу,
и вывести количество дней лидерства для каждого города.

Алгоритм: симуляция по дням.
  Структуры данных:
    person_city[имя]   — в каком городе сейчас
    person_wealth[имя] — капитал (не меняется)
    city_wealth[город] — суммарный капитал города
    moves_by_day[день] — список перемещений за день

  Для каждого дня:
    1. Находим город с максимальным капиталом → +1 день лидерства.
    2. Применяем перемещения в конце дня:
       вычитаем капитал из старого города, прибавляем к новому.

Сложность: O(m * k), где k — число перемещений в день.
"""

from collections import defaultdict


def billionaires(n, billionaires_data, m, movements):
    # --- Инициализация ---
    person_city = {}     # имя → текущий город
    person_wealth = {}   # имя → капитал
    city_wealth = defaultdict(int)  # город → суммарный капитал

    for name, city, wealth in billionaires_data:
        person_city[name] = city
        person_wealth[name] = wealth
        city_wealth[city] += wealth

    # Группируем перемещения по дням для быстрого доступа
    moves_by_day = defaultdict(list)
    for day, name, dest in movements:
        moves_by_day[day].append((name, dest))

    days_led = defaultdict(int)  # город → сколько дней лидировал

    # --- Симуляция по дням ---
    for day in range(1, m + 1):
        # Определяем лидера — город с максимальным капиталом
        if city_wealth:
            max_w = max(city_wealth.values())
            if max_w > 0:
                for city, w in city_wealth.items():
                    if w == max_w:
                        days_led[city] += 1

        # Применяем перемещения в конце дня
        if day in moves_by_day:
            for name, new_city in moves_by_day[day]:
                old_city = person_city[name]
                if old_city == new_city:
                    continue
                w = person_wealth[name]
                # Переносим капитал из старого города в новый
                city_wealth[old_city] -= w
                if city_wealth[old_city] == 0:
                    del city_wealth[old_city]
                city_wealth[new_city] += w
                person_city[name] = new_city

    # Возвращаем отсортированный по алфавиту словарь
    return dict(sorted(days_led.items()))


if __name__ == '__main__':
    # Пример: один миллиардер переезжает на 2-й день
    data = [("Bill", "Seattle", 100)]
    movs = [(1, "Bill", "London")]
    result = billionaires(1, data, 3, movs)
    print(result)  # {'London': 2, 'Seattle': 1}
