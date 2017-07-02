while True:
    n = list(input().split())
    if n == ["0", "W", "0"]:
        break

    if n[1] == "W":
        if int(n[0]) - int(n[2]) >= -200:
            print(int(n[0]) - int(n[2]))
        else:
            print("Not allowed")
    else:
        print(int(n[0]) + int(n[2]))