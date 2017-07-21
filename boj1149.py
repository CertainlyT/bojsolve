n = int(input())

r = list(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))

a = [r, g, b]
if n <= 2:
    if n == 1:
        c = min(a)
        print(c[0])
    else:
        rst = [a[0][0]+a[1][1], a[0][0]+a[2][1], a[1][0]+a[0][1], a[1][0]+a[2][1], a[2][0]+a[0][1], a[2][0]+a[1][1]]
        print(min(rst))
else:
    rst = [[0 for cow in range(n)] for row in range(3)]
    rst[0][0] = a[0][0]
    rst[0][1] = a[0][1]
    rst[0][2] = a[0][2]

    for i in range(1, n):
        for j in range(3):
            rst[i][0] = min(rst[i - 1][1], rst[i - 1][2]) + a[i][0]
            rst[i][1] = min(rst[i - 1][0], rst[i - 1][2]) + a[i][1]
            rst[i][2] = min(rst[i - 1][0], rst[i - 1][1]) + a[i][2]

    print(min(rst[n-1][0], min(rst[n-1][1], rst[n-1][2])))
