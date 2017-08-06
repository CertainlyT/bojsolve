a = list(map(int, input().split()))
a.sort()

if a[0] == a[1] == a[2]:
    print(10000 + 1000 * a[1])
elif a[0] == a[1] or a[1] == a[2]:
    print(1000 + 100 * a[1])
else:
    print(max(a) * 100)