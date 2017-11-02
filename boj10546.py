a = []
c = []

n = int(input())

for i in range(n):
    a.append(input())

for i in range(n - 1):
    c.append(input())

a.sort()
c.sort()

for i in range(n-1):
    if a[i] != c[i]:
        print(a[i])
        break
else:
    print(a[-1])
