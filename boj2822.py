lst = []
for i in range(1, 9):
    lst.append((int(input()), i))

lst.sort(reverse=True)

total = 0
line_lst = []
for i in range(5):
    total += lst[i][0]
    line_lst.append(lst[i][1])

print(total)
line_lst.sort()
for i in range(5):
    print(line_lst[i], end=" ")
print()