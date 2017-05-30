n = int(input())

a = n // 10
b = n % 10

d = 100
count = 0
while d != n:
    c = a + b
    d = b * 10 + c % 10
    a = d // 10
    b = d % 10
    count += 1

print(count)
    