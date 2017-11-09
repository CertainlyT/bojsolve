while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0 and lst[3] == 0:
        break
    cnt = 0
    while 1:
        if lst[0] == lst[1] == lst[2] == lst[3]:
            print(0)
            break
        temp = [0, 0, 0, 0]
        temp[0] = abs(lst[0] - lst[1])
        temp[1] = abs(lst[1] - lst[2])
        temp[2] = abs(lst[2] - lst[3])
        temp[3] = abs(lst[3] - lst[0])
        cnt += 1
        lst = temp
        if temp[0] == temp[1] == temp[2] == temp[3]:
            print(cnt)
            break
