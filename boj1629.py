def f(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 1:
        half = f(x, n // 2, mod)
        return x * half * half % mod
    else:
        half = f(x, n//2, mod)
        return half * half % mod


a, b, c = map(int, input().split())

print(f(a, b, c))