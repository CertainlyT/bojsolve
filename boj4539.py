for i in range(int(input())):
    n = input()
    lst = []
    result = ""
    for j in range(len(n)):
        lst.append(int(n[j]))

    for j in range(len(n) - 1, 1, -1):
        if lst[j] >= 5:
            lst[j] = 0
            lst[j - 1] += 1
            if lst[j - 1] == 10:
                lst[j - 2] += 1
                lst[j - 1] = 0
        else:
            lst[j] = 0
    for j in range(2, len(n)):
        result += str(lst[j])

    if len(n) == 1:
        print(n)
    else:

        if lst[1] >= 5:
            lst[0] += 1
            lst[1] = 0
            if lst[0] == 10:
                result = "100" + result
            else:
                result = str(lst[0]) + str(lst[1]) + result
        else:
            lst[1] = 0
            result = str(lst[0]) + str(lst[1]) + result

        print(result)