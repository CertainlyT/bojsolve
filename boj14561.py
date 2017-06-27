def change(a, n):
    s = ""
    while a > 0:
        a, r = divmod(a, n)
        if r > 9:
            r = chr(ord("a") + r - 10)
        s = str(r) + s

    if str(s) == str(s)[::-1]:
        return 1
    else:
        return 0

n = int(input())
for i in range(n):
    a, n = map(int, input().split())
    print(change(a, n))


