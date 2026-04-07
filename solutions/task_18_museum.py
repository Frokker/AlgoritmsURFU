"""
Задача 18: Музей

В музее регистрируется в течение суток время прихода
и ухода каждого посетителя. Требуется найти максимальное
число посетителей, которые находились в музее одновременно.

Формат входных данных:
  n — количество посетителей.
  visits — список кортежей (время_прихода, время_ухода),
           каждый в формате "ЧЧ:ММ".

Формат выходных данных:
  Максимальное число посетителей, находившихся в музее одновременно.

Алгоритм: метод событий (sweep line).
Приход = +1, уход = -1. При одинаковом времени приход
обрабатывается раньше ухода (сортировка по типу события:
0 — приход, 1 — уход).
"""


def museum_max_visitors(n, visits):
    events = []

    for arrive_str, depart_str in visits:
        ah, am = map(int, arrive_str.split(':'))
        dh, dm = map(int, depart_str.split(':'))
        arrive = ah * 60 + am
        depart = dh * 60 + dm
        # (время, тип: 0=приход, 1=уход)
        events.append((arrive, 0))
        events.append((depart, 1))

    events.sort()

    current = 0
    max_visitors = 0

    for time, event_type in events:
        if event_type == 0:
            current += 1
        else:
            current -= 1
        if current > max_visitors:
            max_visitors = current

    return max_visitors


if __name__ == '__main__':
    # Пример: частичное пересечение
    visits = [("09:00", "11:00"), ("10:00", "12:00")]
    print(museum_max_visitors(2, visits))  # 2

    # Пример: без пересечения
    visits = [("09:00", "10:00"), ("11:00", "12:00")]
    print(museum_max_visitors(2, visits))  # 1

    # Пример: вложенные интервалы
    visits = [
        ("08:00", "18:00"),
        ("09:00", "17:00"),
        ("10:00", "16:00"),
        ("11:00", "15:00"),
    ]
    print(museum_max_visitors(4, visits))  # 4
