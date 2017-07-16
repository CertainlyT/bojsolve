n, k = map(int, input().split())

lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

try:
    print(lst[k-1])
except IndexError:
    print(0)