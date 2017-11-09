cnt = 0
total = 0
solve_dic = {}
while True:
    string = input().split()
    if string[0] == '-1':
        break
    if string[2] == 'right':
        cnt += 1
        if string[1] in solve_dic:
            total += int(string[0]) + 20 * solve_dic[string[1]]
        else:
            total += int(string[0])
    elif string[2] == 'wrong':
        if string[1] in solve_dic:
            solve_dic[string[1]] += 1
        else:
            solve_dic[string[1]] = 1

print(cnt, total)
