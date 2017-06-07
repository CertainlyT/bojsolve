n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    d = a
    e = b

    while b != 0:
        c = a
        a = b
        b = c % b

    print(int(d * e / a))
