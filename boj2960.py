n, k = map(int, input().split())
lst = list(range(n + 1))

cnt = 0
rst = 0
for i in range(2, n + 1):
    for j in range(i, n+1, i):
        if lst[j] != 0:
            rst = j
            cnt += 1
            lst[j] = 0
            if cnt == k:
                print(rst)
                break
        else:
            pass
