while True:
    n = list(input())
    if n[0] == "#":
        break
    if n[len(n)-1] == "e":
        if n.count("1") % 2 == 0:
            n[len(n)-1] = "0"
        else:
            n[len(n)-1] = "1"
    else:
        if n.count("1") % 2 == 0:
            n[len(n)-1] = "1"
        else:
            n[len(n)-1] = "0"
    for i in range(len(n)):
        print(n[i], end="")
    print()