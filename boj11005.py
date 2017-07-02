def change(a, r):
    STR = ""
    while a != 0:
        a, n = divmod(a, r)
        if n > 9:
            n = chr(ord("A") + n - 10)
        STR = str(n) + STR
    return STR

a, r = map(int, input().split())
print(change(a, r))
