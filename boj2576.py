total = 0
min_num = 100

for i in range(7):
    a = int(input())
    if a % 2 == 1:
        total += a
        if a < min_num:
            min_num = a

if total == 0:
    print(-1)
else:
    print(total)
    print(min_num)