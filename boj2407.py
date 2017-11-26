a, b = map(int, input().split())

n = 1
for i in range(a, a - b, -1):
    n *= i

m = 1
for i in range(1, b + 1):
    m *= i

print(n // m)