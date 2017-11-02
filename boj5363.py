for i in range(int(input())):
    lst = input().split()
    for j in range(2, len(lst)):
        print(lst[j], end=" ")
    for j in range(2):
        print(lst[j], end=" ")
    print()