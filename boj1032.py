n = int(input())

lst = []
for i in range(n):
    lst.append(input())

rst = ""
for i in range(len(lst[0])):
    a = lst[0][i]
    for j in range(len(lst)):
        if lst[j][i] == a:
            pass
        else:
            rst += "?"
            break
    else:
        rst += a

print(rst)