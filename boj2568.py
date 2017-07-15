import sys
from operator import itemgetter


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
lst = []
dic = {}
c = []

n = int(sys.stdin.readline())

for i in range(n):
    a = tuple(map(int, sys.stdin.readline().split()))
    lst.append(a)
    c.append(a[1])
    dic[a[1]] = a[0]

lst.sort(key=itemgetter(0))
res.append(lst[0][1])
for i in range(1, n):
    if res[-1] < lst[i][1]:
        res.append(lst[i][1])
    else:
        lower_bound(lst[i][1])
        res[right] = lst[i][1]

print(lst)
print(res)
res = set(res)
c = set(c)
d = c - res
ans = []

for each in d:
    ans.append(dic[each])

ans.sort()

print(len(ans))
for each in ans:
    print(each)