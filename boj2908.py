a, b = map(str, input().split())

c = []
d = []
for i in range(2, -1, -1):
    c.append(a[i])
    d.append(b[i])

if c[0] > d[0]:
    for j in range(3):
        print(c[j], end="")
elif c[0] == d[0] and c[1] > d[1]:
    for j in range(3):
        print(c[j], end="")
elif c[0] == d[0] and c[1] == d[1] and c[2] > d[2]:
    for j in range(3):
        print(c[j], end="")
else:
    for j in range(3):
        print(d[j], end="")