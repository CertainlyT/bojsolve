a, b = map(int, input().split())

if a > b:
    a, b = b, a

c = (a + b) / 2

print(int(c * (b - a + 1)))