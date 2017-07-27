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

n = int(input())
lst = list(map(int, input().split()))
res = [lst[0]]
a = [0]
rst = []

for i in range(1, n):
    if res[-1] < lst[i]:
        res.append(lst[i])
        a.append(res.index(lst[i]))
    else:
        lower_bound(lst[i])
        res[right] = lst[i]
        a.append(right)

c = max(a)
d = len(a)-1
while d >= 0:
    if a[d] == c:
        rst.append(lst[d])
        c -= 1
        d -= 1
    else:
        d -= 1

rst.sort()
print(len(rst))
for i in range(len(rst)):
    print(rst[i], end=" ")
