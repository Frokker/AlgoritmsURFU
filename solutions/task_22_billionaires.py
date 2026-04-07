"""
Задача 22: Миллиардеры

Ваш работодатель просит посчитать, сколько дней в течение
периода наблюдения каждый из городов мира был первым по общей
сумме денег миллиардеров, находящихся в нём.

Миллиардеры путешествуют не чаще одного раза в день:
отбывают поздно вечером и прибывают в город назначения
рано утром следующего дня.

Формат входных данных:
  n — количество миллиардеров.
  billionaires_data — список кортежей (имя, город, состояние).
  m — количество дней наблюдения.
  movements — список кортежей (день, имя, город_назначения).

Формат выходных данных:
  Словарь {город: количество_дней_лидерства},
  отсортированный по алфавиту (по ключам).
"""

from collections import defaultdict


def billionaires(n, billionaires_data, m, movements):
    person_city = {}
    person_wealth = {}
    city_wealth = defaultdict(int)

    for name, city, wealth in billionaires_data:
        person_city[name] = city
        person_wealth[name] = wealth
        city_wealth[city] += wealth

    # Группируем перемещения по дням
    moves_by_day = defaultdict(list)
    for day, name, dest in movements:
        moves_by_day[day].append((name, dest))

    days_led = defaultdict(int)

    for day in range(1, m + 1):
        # Определяем город-лидер на этот день
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
                city_wealth[old_city] -= w
                if city_wealth[old_city] == 0:
                    del city_wealth[old_city]
                city_wealth[new_city] += w
                person_city[name] = new_city

    return dict(sorted(days_led.items()))


if __name__ == '__main__':
    # Пример: один миллиардер, одно перемещение
    data = [("Bill", "Seattle", 100)]
    movs = [(1, "Bill", "London")]
    result = billionaires(1, data, 3, movs)
    print(result)  # {'London': 2, 'Seattle': 1}

    # Пример: смена лидерства
    data = [("A", "NYC", 100), ("B", "London", 80)]
    movs = [(1, "A", "London")]
    result = billionaires(2, data, 3, movs)
    print(result)  # {'London': 2, 'NYC': 1}
