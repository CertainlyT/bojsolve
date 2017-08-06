while True:
    a = 0
    b = 0
    c = 0
    d = 0
    s = input()
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            a += 1
        elif 65 <= ord(s[i]) <= 90:
            b += 1
        elif ord(s[i]) == 32:
            d += 1
        else:
            c += 1
    print(a, b, c, d)