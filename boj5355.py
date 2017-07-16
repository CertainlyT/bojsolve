n = int(input())
lst = []

for i in range(n):
    lst.append(list(input().split()))

for i in range(n):
    a = float(lst[i][0])
    for j in range(1, len(lst[i])):
        if lst[i][j] == "@":
            a *= 3
        elif lst[i][j] == "%":
            a += 5
        else:
            a -= 7
    print("%.2f" % a)
