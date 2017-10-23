while 1:
    n = input()
    if n == "0":
        break
    result = 0
    for i in range(len(n)):
        result += int(n[i])
    while result >= 10:
        temp = 0
        for i in range(len(str(result))):
            temp += int(str(result)[i])
        result = temp
    print(result)