while True:
    count = 0
    n = list(input().split())
    if n[0] == "-1":
        break
    for i in range(len(n)):
        if n[i] == "0":
            pass
        else:
            if str((int(n[i]) * 2)) in n:
                count += 1
    print(count)

