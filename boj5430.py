import sys

for i in range(int(input())):
    reverse_check = False
    command = str(sys.stdin.readline())
    n = int(input())
    lst = list(eval(sys.stdin.readline()))
    for each in command:
        if each == "R":
            reverse_check = not reverse_check
        elif each == "D":
            if len(lst) == 0:
                print("error")
                break
            if reverse_check:
                lst.pop(-1)
            else:
                lst.pop(0)
    else:
        if reverse_check:
            print(str(lst[::-1]).replace(" ", ""))
        else:
            print(str(lst).replace(" ", ""))