c = int(input())

for i in range(c):
    cnt = 0
    a, b = map(int, input().split())
    MIN = b - a
    while a*2 <= b+3:
        N = 0
        a *= 2
        b += 3
        cnt += 1
        j = b - a
        l = cnt
        while l >= 0:
            N += int(j / (2**l))
            j %= 2**l
            l -= 1
        MIN = N + cnt if N + cnt < MIN else MIN

    print(MIN)
