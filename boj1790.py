n, k = map(int, input().split())

nine = 9
length = 1
ten = 1

while n - nine * ten >= 0:
    n -= nine * ten
    ten *= 10
    k -= length * nine * ten
    length += 1

print(n, k)
print(length)