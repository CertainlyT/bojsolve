flag1 = False
flag2 = False
flag3 = False
for i in range(int(input())):
    a = list(map(int, input().split()))
    if sorted(a) == [1, 3]:
        flag1 = True
    elif sorted(a) == [1, 4]:
        flag2 = True
    elif sorted(a) == [3, 4]:
        flag3 = True
    else:
        print("Woof-meow-tweet-squeek")
        break
else:
    if flag1 and flag2 and flag3:
        print("Wa-pa-pa-pa-pa-pa-pow!")
    else:
        print("Woof-meow-tweet-squeek")