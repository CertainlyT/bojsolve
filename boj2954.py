s = list(input())

for i in range(len(s)-2):
    if s[i] == "a":
        s[i+1] = "0"
        s[i+2] = "0"
    elif s[i] == "e":
        s[i+1] = "0"
        s[i+2] = "0"
    elif s[i] == "i":
        s[i + 1] = "0"
        s[i + 2] = "0"
    elif s[i] == "o":
        s[i+1] = "0"
        s[i+2] = "0"
    elif s[i] == "u":
        s[i+1] = "0"
        s[i+2] = "0"

for i in range(len(s)):
    if s[i] != "0":
        print(s[i], end="")