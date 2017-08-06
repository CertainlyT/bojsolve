n = int(input())
lst = []

for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[3]:
        lst.append(50000 + a[0] * 5000)
    elif a[0] == a[2] or a[1] == a[3]:
        lst.append(10000 + a[2] * 1000)
    elif a[0] == a[1] and a[2] == a[3]:
        lst.append(2000 + a[1] * 500 + a[2] * 500)
    elif a[0] == a[1]:
        lst.append(1000 + 100 * a[1])
    elif a[1] == a[2]:
        lst.append(1000 + 100 * a[1])
    elif a[2] == a[3]:
        lst.append(1000 + 100 * a[3])
    else:
        lst.append(max(a) * 100)

print(max(lst))