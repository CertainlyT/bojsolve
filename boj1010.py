for j in range(int(input())):
    n, k = map(int, input().split())

    if n == 0:
        print(1)
    else:
        for i in range(k-1, k-n, -1):
            k *= i

        for i in range(1, n):
            n *= i

        print(k//n)