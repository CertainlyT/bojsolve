for i in range(int(input())):
    n = input()
    s = ""
    for j in range(len(n)):
        s += n[j].lower()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")
