for i in range(int(input())):
    a, b = map(str, input().split())
    b = list(b)
    for j in range(len(b)):
        if j != int(a) - 1:
            print(b[j], end="")
    print()
