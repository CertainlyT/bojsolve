import sys
from operator import itemgetter
n = int(input())

lst = []

for i in range(n):
    lst.append(list(map(str, sys.stdin.readline().split())))

for i in range(n):
    lst[i][1] = int(lst[i][1])
    lst[i][2] = int(lst[i][2])
    lst[i][3] = int(lst[i][3])

lst.sort(key=itemgetter(0))
lst.sort(key=itemgetter(3), reverse=True)
lst.sort(key=itemgetter(2))
lst.sort(key=itemgetter(1), reverse=True)

for i in range(n):
    print(lst[i][0])

