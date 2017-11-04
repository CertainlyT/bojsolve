for i in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    if (b - a + 1) % 2 == 0:
        check = (b - a + 1) // 2
        print("Scenario #%d:\n%d\n" % (i, (a + b) * check))
    else:
        check = (b - a + 1) // 2
        plus = (b + a) // 2
        print("Scenario #%d:\n%d\n" % (i, (a + b) * check + plus))