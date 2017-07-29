# solution source
import sys
n, k, b = map(int, sys.stdin.readline().split())

a = []
for i in range(b):
    a.append(int(sys.stdin.readline()))

a.sort()

cnt = 0
while cnt < b and a[cnt] <= k:
    cnt += 1

result = cnt

for i in range(b):
    if a[i] + k > n:
        break
    while cnt < b and a[cnt] <= a[i] + k:
        cnt += 1
    result = min(result, cnt - i - 1)

print(result)