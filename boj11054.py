def lower_bound(a, b):
    global right
    left = 0
    right = len(b) - 1
    while right - left > 0:
        mid = (left + right) // 2
        if b[mid] < a:
            left = mid + 1
        else:
            right = mid
    return right

ans = 0

n = int(input())

lst = list(map(int, input().split()))
rst = lst[::-1]


for j in range(n):
    res = []
    res2 = []
    res.append(lst[0])
    res2.append(rst[0])
    for i in range(1, j+1):
        if res[-1] < lst[i]:
            res.append(lst[i])
        else:
            lower_bound(lst[i], res)
            res[right] = lst[i]
    for i in range(1, n-j):
        if res2[-1] < rst[i]:
            res2.append(rst[i])
        else:
            lower_bound(rst[i], res2)
            res2[right] = rst[i]
    ans = len(res) + len(res2) - 1 if len(res) + len(res2) - 1 > ans else ans

print(ans)