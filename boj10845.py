n = int(input())

lst = []

for i in range(n):
    a = input().split()
    if a[0] == "push":
        lst.append(int(a[1]))
    elif a[0] == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
            lst.remove(lst[0])
    elif a[0] == "size":
        print(len(lst))
    elif a[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    else:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])