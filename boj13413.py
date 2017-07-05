n = int(input())

for i in range(n):
    lst = []
    a = int(input())
    b = input()
    c = input()
    for j in range(a):
        if b[j] == c[j]:
            pass
        else:
            lst.append((b[j], c[j]))

    d = lst.count(("B", "W"))
    e = lst.count(("W", "B"))
    cnt = 0
    while d > 0 and e > 0:
        d -= 1
        e -= 1
        cnt += 1
    cnt += d
    cnt += e

    print(cnt)