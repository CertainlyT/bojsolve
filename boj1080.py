def change(x, y):
    for k in range(x, x + 3):
        for l in range(y, y + 3):
            a[k][l] = 1 - a[k][l]

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input())))

b = []
for i in range(n):
    b.append(list(map(int, input())))

rst = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(i, j)
            rst += 1

cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            cnt += 1

if cnt == 0:
    print(rst)
else:
    print(-1)