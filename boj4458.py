for i in range(int(input())):
    s = list(input())
    if 97 <= ord(s[0]) <= 122:
        s[0] = chr(ord(s[0]) - 32)
    for j in range(len(s)):
        print(s[j], end="")
    print()