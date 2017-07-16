def f(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return x * f(x, n-1)
    else:
        half = f(x, n//2)
        return half * half

a, b, c = map(int, input().split())

print(f(a, b) % c)