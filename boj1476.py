e, s, m = map(int, input().split())
e1, s1, m1, year = 1, 1, 1, 1
while 1:
    if e == e1 and s == s1 and m == m1:
        break
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 % 16 == 0:
        e1 //= 16
    if s1 % 29 == 0:
        s1 //= 29
    if m1 % 20 == 0:
        m1 //= 20
    year += 1

print(year)

