for i in range(int(input())):
    c, p = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)." % divmod(c, p))