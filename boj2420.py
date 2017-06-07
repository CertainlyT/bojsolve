m, n = map(int, input().split())

if m > n:
    m, n = n, m

print(n - m)
