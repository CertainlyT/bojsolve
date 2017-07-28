def change(a, n):
    s = ""
    while a > 0:
        a, r = divmod(a, n)
        if r > 9:
            r = chr(ord("a") + r - 10)
        s = str(r) + s

    if str(s) == str(s)[::-1]:
        lst.append(1)
    else:
        lst.append(0)

for i in range(int(input())):
    lst = []
    num = int(input())
    for j in range(2, 65):
        change(num, j)
    if 1 not in lst:
        print(0)
    else:
        print(1)
