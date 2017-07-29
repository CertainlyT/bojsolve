# my source

n, k, b = map(int, input().split())

a = [0] * n

for i in range(b):
    a[int(input()) - 1] = 1

b = sum(a[:k])

rst = b

for i in range(k, n):
    b += a[i] - a[i-k]
    rst = b if b < rst else rst

print(rst)