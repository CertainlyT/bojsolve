lst = ["0", "0", "0", "0"]
temp = ["0", "0", "0", "0"]


def fill(lst1, lst2):
    for each in range(4):
        if lst2[each] == "0":
            lst2[each] = lst1[each]


def left_turn(s1, s2, direc, idx):
    if s1[6] != s2[2]:
        # clockwise == 1
        if direc == 1:
            temp[idx] = lst[idx][1:] + lst[idx][0]
        else:
            temp[idx] = lst[idx][7] + lst[idx][:7]
        return 1
    else:
        temp[idx] = lst[idx]
        return 0


def right_turn(s1, s2, direc, idx):
    if s1[2] != s2[6]:
        if direc == 1:
            temp[idx] = lst[idx][1:] + lst[idx][0]
        else:
            temp[idx] = lst[idx][7] + lst[idx][:7]
        return 1
    else:
        temp[idx] = lst[idx]
        return 0


for i in range(4):
    lst[i] = input()

for j in range(int(input())):
    a, b = map(int, input().split())
    if b < 0:
        for i in range(abs(b)):
            temp[a - 1] = lst[a - 1][1:] + lst[a - 1][0]
            direction = 0
            check = (a - 1) % 2
            temp_idx = a - 1
            while temp_idx < 3:
                if check != temp_idx % 2:
                    c = right_turn(lst[temp_idx], lst[temp_idx + 1], 1, temp_idx + 1)
                    temp_idx += 1
                    if c == 0:
                        break
                else:
                    c = right_turn(lst[temp_idx], lst[temp_idx + 1], 0, temp_idx + 1)
                    temp_idx += 1
                    if c == 0:
                        break

            temp_idx = a - 1
            while temp_idx > 0:
                if check != temp_idx % 2:
                    c = left_turn(lst[temp_idx], lst[temp_idx - 1], 1, temp_idx - 1)
                    temp_idx -= 1
                    if c == 0:
                        break
                else:
                    c = left_turn(lst[temp_idx], lst[temp_idx - 1], 0, temp_idx - 1)
                    temp_idx -= 1
                    if c == 0:
                        break
            fill(lst, temp)
            lst = temp
            temp = ["0", "0", "0", "0"]

    else:
        for i in range(abs(b)):
            temp[a - 1] = lst[a - 1][7] + lst[a - 1][:7]
            direction = 1
            check = (a - 1) % 2
            temp_idx = a - 1
            while temp_idx < 3:
                if check != temp_idx % 2:
                    c = right_turn(lst[temp_idx], lst[temp_idx + 1], 0, temp_idx + 1)
                    temp_idx += 1
                    if c == 0:
                        break
                else:
                    c = right_turn(lst[temp_idx], lst[temp_idx + 1], 1, temp_idx + 1)
                    temp_idx += 1
                    if c == 0:
                        break

            temp_idx = a - 1
            while temp_idx > 0:
                if check != temp_idx % 2:
                    c = left_turn(lst[temp_idx], lst[temp_idx - 1], 0, temp_idx - 1)
                    temp_idx -= 1
                    if c == 0:
                        break
                else:
                    c = left_turn(lst[temp_idx], lst[temp_idx - 1], 1, temp_idx - 1)
                    temp_idx -= 1
                    if c == 0:
                        break
            fill(lst, temp)
            lst = temp
            temp = ["0", "0", "0", "0"]

print(int(lst[0][0]) + int(lst[1][0]) * 2 + int(lst[2][0]) * 4 + int(lst[3][0]) * 8)