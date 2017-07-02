n = int(input())

num_list = list(map(int, input().split()))

check_list = []

for i in range(n):
    if i == 0:
        check_list.append(num_list[i])
    else:
        if num_list[i] < min(check_list):
            check_list.append(num_list[i])
        else:
            len_check = len(check_list)
            if check_list[len_check - 2] > num_list[i] > check_list[len_check-1]:
                check_list[len_check-1] = num_list[i]
            else:
                if len(check_list) == 1:
                    if num_list[i] > check_list[0]:
                        check_list[0] = num_list[i]
                else:
                    for j in range(len(check_list)-1):
                        if j == 0:
                            if num_list[i] > check_list[j]:
                                check_list[j] = num_list[i]
                        else:
                            if check_list[j-1] > num_list[i] > check_list[j]:
                                check_list[j] = num_list[i]

print(len(check_list))