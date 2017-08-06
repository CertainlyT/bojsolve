a = input().split(":")
b = input().split(":")

a_time = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])
b_time = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])

if a_time < b_time:
    rst = b_time - a_time
    h = 0
    m = 0
    while rst >= 3600:
        h += 1
        rst -= 3600
    while rst >= 60:
        m += 1
        rst -= 60
    s = rst
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)
    print(str(h) + ":" + str(m) + ":" + str(s))
else:
    rst = 86400 - (a_time - b_time)
    h = 0
    m = 0
    while rst >= 3600:
        h += 1
        rst -= 3600
    while rst >= 60:
        m += 1
        rst -= 60
    s = rst
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)
    print(str(h) + ":" + str(m) + ":" + str(s))