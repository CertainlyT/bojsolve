import sys

n, k = map(int, input().split())

lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

answer = 0
for i in range(n - k // 2 - 1):
    temp = sorted(lst[i:i+k])
    length = len(temp)
    answer += temp[length // 2]

print(answer)