n = input()

if n[0] == "0":
    if n[1] == "x":
        print(int(n, 16))
    else:
        n = n[0] + "o" + n[1:]
        print(int(n, 8))
else:
    print(int(n))