import sys

lst = []

n = int(input())

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

for i in range(n):
    print(lst[i])