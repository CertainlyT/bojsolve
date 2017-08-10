a, b = map(int, input().split())

if a == 0 and b < 45:
    print(23, 60 - (45 - b))
else:
    c = a * 60 + b - 45

    h = 0

    while c >= 60:
        c -= 60
        h += 1

    print(h, c)