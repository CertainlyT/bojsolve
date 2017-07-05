a, b = map(int, input().split())

lst = []
for i in range(a):
    n = input()
    lst.append(n)

cnt = 0
for j in range(b):
    c = input()
    if c in lst:
        cnt += 1

print(cnt)