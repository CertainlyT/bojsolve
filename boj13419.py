n = int(input())

for i in range(n):
    st = input()
    a = ""
    b = ""
    if len(st) % 2 == 0:
        for j in range(0, len(st)-1, 2):
            a += st[j]
            b += st[j+1]
    else:
        st += st
        for j in range(0, len(st)-1, 2):
            a += st[j]
            b += st[j+1]

    print(a)
    print(b)