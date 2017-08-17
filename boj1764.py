import sys

name1 = []
name2 = []

a, b = map(int, input().split())

for i in range(a):
    name1.append(str(sys.stdin.readline()))

for i in range(b):
    name2.append(str(sys.stdin.readline()))

name1 = set(name1)
name2 = set(name2)

rst = name1 & name2

rst = list(rst)
rst.sort()
print(len(rst))
for i in range(len(rst)):
    print(rst[i], end="")