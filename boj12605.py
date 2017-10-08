for i in range(int(input())):
    lst = list(map(str, input().split()))
    print("Case #%d:" % (i + 1), end=" ")
    for j in range(len(lst) - 1, -1, -1):
        print(lst[j], end=" ")
    print()