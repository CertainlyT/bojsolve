while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    c = a // b
    d = a % b
    print(c, d, "/", b)
