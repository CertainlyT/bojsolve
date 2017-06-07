lst = []
price_list = [350.34, 230.90, 190.55, 125.30, 180.90]
n = int(input())
for i in range(n):
    num = input().split()
    lst.append(num)

for j in range(len(lst)):
    total = float(0)
    for k in range(len(lst[j])):
        total += float(lst[j][k]) * price_list[k]
    print("$" + "%.2f" % float(total))
