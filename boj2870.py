n = int(input())
lst = []
for i in range(n):
    a = input()
    s = ""
    for j in range(len(a)):
        if 48 <= ord(a[j]) <= 57:
            s += a[j]
        else:
            if len(s) != 0:
                lst.append(int(s))
                s = ""
    if len(s) != 0:
        lst.append(int(s))
        s = ""

lst.sort()
for i in range(len(lst)):
    print(lst[i])
