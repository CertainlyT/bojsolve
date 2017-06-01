lst = list(map(int, input().split()))

check_list = []
for i in range(1, len(lst)):
    if lst[i-1] > lst[i]:
        check_list.append(1)
    elif lst[i-1] < lst[i]:
        check_list.append(-1)
    else:
        check_list.append(0)

if 1 in check_list and 0 not in check_list and -1 not in check_list:
    print("descending")
elif 1 not in check_list and 0 not in check_list and -1 in check_list:
    print("ascending")
else:
    print("mixed")
