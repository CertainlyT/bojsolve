n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)

count_1 = lst.count(1)
count_0 = lst.count(0)

if count_1 > count_0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")