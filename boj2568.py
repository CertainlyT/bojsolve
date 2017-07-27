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

lst = []
n = int(input())
for i in range(n):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

lst.sort(key=itemgetter(1))

res = [lst[0][0]]
a = [0]
rst = []

for i in range(1, n):
    if res[-1] < lst[i][0]:
        res.append(lst[i][0])
        a.append(res.index(lst[i][0]))
    else:
        lower_bound(lst[i][0])
        res[right] = lst[i][0]
        a.append(right)

c = max(a)
d = len(a)-1
while d >= 0:
    if a[d] == c:
        rst.append(lst[d][0])
        c -= 1
        d -= 1
    else:
        d -= 1

rst.sort()
b = []
for i in range(n):
    b.append(lst[i][0])
b = set(b)
rst = set(rst)
e = b - rst
e = list(e)
print(n - len(rst))
for i in range(len(e)):
    print(e[i], end=" ")

