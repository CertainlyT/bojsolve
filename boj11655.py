string = input()
result = ""

for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        if ord(string[i]) + 13 > 90:
            result += chr(65 + 12 - (90 - ord(string[i])))
        else:
            result += chr(ord(string[i]) + 13)
    elif 97 <= ord(string[i]) <= 122:
        if ord(string[i]) + 13 > 122:
            result += chr(97 + 12 - (122 - ord(string[i])))
        else:
            result += chr(ord(string[i]) + 13)
    else:
        result += string[i]
print(result)