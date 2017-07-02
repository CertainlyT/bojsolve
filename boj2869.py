a, b, v = map(int, input().split())

if (v - a) % (a - b) == 0:
    print((v - a) // (a - b) + 1)
else:
    c, d = divmod(v-a, a-b)
    if (d + a) % a == 0:
        print(c + ((d + a) // a))
    else:
        print(c + ((d + a) // a) + 1)
