import math

m = int(input())
n = int(input())

if m > n:
    m, n = n, m

a = int(math.sqrt(m))
b = int(math.sqrt(n))+1

num_list = []
for i in range(a, b+1):
    c = i ** 2
    if m <= c <= n:
        num_list.append(c)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))

