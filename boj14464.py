import sys


def lower_bound(a):
    left = 0
    right = len(chicken) - 1
    while right - left > 0:
        mid = (left + right) // 2
        if chicken[mid] < a:
            left = mid + 1
        else:
            right = mid
    return right


c, n = map(int, sys.stdin.readline().split())

chicken = []
cow = []

for i in range(c):
    chicken.append(int(sys.stdin.readline()))

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cow.append((b, a))

cow.sort()
chicken.sort()

total = 0

for i in range(n):
    if len(chicken) == 0:
        break
    s = lower_bound(cow[i][1])
    if cow[i][1] <= chicken[s] <= cow[i][0]:
        total += 1
        chicken.remove(chicken[s])


print(total)