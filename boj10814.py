from operator import itemgetter
lst = []
n = int(input())
for i in range(n):
    b, c = map(str, input().split())
    a = [int(b), c, i]
    lst.append(a)

lst.sort(key=itemgetter(2))
lst.sort(key=itemgetter(0))
for i in range(n):
    print(lst[i][0], lst[i][1])
