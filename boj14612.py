import operator
lst = []
n, m = map(int, input().split())

for i in range(n):
    st = list(input().split())
    if st[0] == "order":
        lst.append((int(st[1]), int(st[2])))
        if len(lst) == 0:
            print("sleep")
        else:
            for j in range(len(lst)):
                print(lst[j][0], end=" ")
            print()

    elif st[0] == "sort":
        lst.sort(key=operator.itemgetter(0))
        lst.sort(key=operator.itemgetter(1))
        if len(lst) == 0:
            print("sleep")
        else:
            for j in range(len(lst)):
                print(lst[j][0], end=" ")
            print()

    elif st[0] == "complete":
        for j in range(len(lst)):
            if lst[j][0] == int(st[1]):
                lst.remove(lst[j])
                break
        if len(lst) != 0:
            for j in range(len(lst)):
                print(lst[j][0], end=" ")
            print()
        else:
            print("sleep")
