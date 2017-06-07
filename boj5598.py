n = list(input())

for i in range(len(n)):
    if 67 < ord(n[i]):
        a = ord(n[i]) - 3
        n[i] = chr(a)
    else:
        if ord(n[i]) == 65:
            n[i] = chr(88)
        elif ord(n[i]) == 66:
            n[i] = chr(89)
        else:
            n[i] = chr(90)

for j in range(len(n)):
    print(n[j], end="")