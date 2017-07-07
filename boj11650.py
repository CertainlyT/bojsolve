from operator import itemgetter
lst = []
a = int(input())
for i in range(a):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=itemgetter(1))
lst.sort(key=itemgetter(0))

for i in range(a):
    print(lst[i][0], lst[i][1])
