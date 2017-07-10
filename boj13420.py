for i in range(int(input())):
    l = list(input().split())
    if l[1] == "+":
        if int(l[0]) + int(l[2]) == int(l[4]):
            print("correct")
        else:
            print("wrong answer")
    elif l[1] == "-":
        if int(l[0]) - int(l[2]) == int(l[4]):
            print("correct")
        else:
            print("wrong answer")
    elif l[1] == "*":
        if int(l[0]) * int(l[2]) == int(l[4]):
            print("correct")
        else:
            print("wrong answer")
    else:
        if int(l[0]) / int(l[2]) == int(l[4]):
            print("correct")
        else:
            print("wrong answer")