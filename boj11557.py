from operator import itemgetter
a = int(input())

for i in range(a):
    b = int(input())
    lst = []
    for j in range(b):
        c = list(input().split())
        lst.append(c)
    for j in range(b):
        lst[j][1] = int(lst[j][1])
    lst.sort(key=itemgetter(1), reverse=True)
    print(lst[0][0])

