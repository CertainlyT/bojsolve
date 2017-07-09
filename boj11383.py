a, b = map(int, input().split())

lst1 = []
lst2 = []
for i in range(a):
    lst1.append(input())

for j in range(a):
    lst2.append(input())

rst = []
for k in range(a):
    c = ""
    for l in range(b):
        c += lst1[k][l] * 2
    if c == lst2[k]:
        rst.append(0)
    else:
        rst.append(1)

if 1 not in rst:
    print("Eyfa")
else:
    print("Not Eyfa")