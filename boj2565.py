import operator
n = int(input())
line_list = []
for i in range(n):
    line = tuple(map(int, input().split()))
    line_list.append(line)

line_list.sort(key=operator.itemgetter(0))

check_list = []

for i in range(n):
    if i == 0:
        check_list.append(line_list[i][1])
    else:
        if line_list[i][1] > max(check_list):
            check_list.append(line_list[i][1])
        else:
            len_check = len(check_list)
            if check_list[len_check - 2] < line_list[i][1] < check_list[len_check-1]:
                check_list[len_check-1] = line_list[i][1]
            else:
                if len(check_list) == 1:
                    if line_list[i][1] < check_list[0]:
                        check_list[0] = line_list[i][1]
                else:
                    for j in range(len(check_list)-1):
                        if j == 0:
                            if line_list[i][1] < check_list[j]:
                                check_list[j] = line_list[i][1]
                        else:
                            if check_list[j-1] < line_list[i][1] < check_list[j]:
                                check_list[j] = line_list[i][1]

print(n - len(check_list))
