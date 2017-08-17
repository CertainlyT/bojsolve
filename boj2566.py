lst = [[]] * 9
for i in range(9):
    lst[i] = list(map(int, input().split()))

max_num = max(lst[0])
index_num = (0, lst[0].index(max(lst[0])))
for i in range(1, 9):
    if max(lst[i]) > max_num:
        max_num = max(lst[i])
        index_num = (i, lst[i].index(max(lst[i])))

print(max_num)
print(index_num[0] + 1, index_num[1] + 1)