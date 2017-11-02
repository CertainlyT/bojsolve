for i in range(int(input())):
    h, w, n = map(int, input().split())
    num = 1
    while n > h:
        n -= h
        num += 1
    print(n * 100 + num)