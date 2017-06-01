x, y = map(int, input().split())

months_day = 0

for i in range(1, x):
    if x == 1:
        continue
    if (i <= 7 and i % 2 == 1) or (i >= 8 and i % 2 == 0):
        months_day += 31
    elif i == 2:
        months_day += 28
    else:
        months_day += 30

days_day = y - 1

total_day = months_day + days_day

find_day_of_week = total_day % 7

day_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(day_of_week[find_day_of_week])