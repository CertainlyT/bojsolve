def lower_bound(a):
    global right
    left = 0
    right = len(res) - 1
    while right - left > 0:
        mid = (left + right) // 2
        if res[mid] < a:
            left = mid + 1
        else:
            right = mid
    return right

res = []

n = int(input())

lst = list(map(int, input().split()))

res.append(lst[0])
for i in range(1, n):
    if res[-1] < lst[i]:
        res.append(lst[i])
    else:
        lower_bound(lst[i])
        res[right] = lst[i]

print(len(res))