import sys
lst = []
for i in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline())

lst = set(lst)
lst = list(lst)
lst.sort()
lst.sort(key=len)

for each in lst:
    print(each, end="")