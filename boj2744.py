n = list(input())

for i in range(len(n)):
    if 65 <= ord(n[i]) <= 90:
        n[i] = chr(ord(n[i]) + 32)
    else:
        n[i] = chr(ord(n[i]) - 32)

for i in range(len(n)):
    print(n[i], end="")
