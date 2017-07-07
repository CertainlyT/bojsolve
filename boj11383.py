a, b = map(int, input().split())

lst1 = []
lst2 = []
for i in range(a):
    lst1.append(input())

for j in range(a):
    lst2.append(input())

rst = 0
for k in range(a):
    c = ""
    for l in range(b):
        c += lst1[k][l] * 2
    if c == lst2[k]:
        rst = 0
    else:
        rst = 1
        break

if rst == 0:
    print("Eyfa")
else:
    print("Not Eyfa")