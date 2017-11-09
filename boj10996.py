n = int(input())

a = 0
b = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        a += 1
    else:
        b += 1

for i in range(n):
    print("* " * a)
    print(" *" * b)