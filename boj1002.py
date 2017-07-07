from math import sqrt

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            result = -1
        else:
            result = 0

    else:
        min_num = abs(r1 - r2)
        dis = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if min_num < dis < r1 + r2:
            result = 2
        elif dis == r1 + r2 or dis == min_num:
            result = 1
        else:
            result = 0

    print(result)
