a, b, c = map(int, input().split())

for i in range(c):
    a ^= b

print(a)