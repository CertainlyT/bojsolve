a = input()
lst = []
for i in range(65, 91):
    c = chr(i)
    b = [i for i, x in enumerate(a) if x == c]
    lst.append(b)

cnt = 0
for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i][0] < lst[j][0] < lst[i][1] < lst[j][1] or lst[j][0] < lst[i][0] < lst[j][1] < lst[i][1]:
            cnt += 1

print(cnt)