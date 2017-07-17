n, k = map(int, input().split())

if k == 0:
    print(1)
else:
    for i in range(n-1, n-k, -1):
        n *= i

    for i in range(1, k):
        k *= i

    print(n//k)