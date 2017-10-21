for i in range(int(input())):
    print("Case #%d:" % (i + 1), end=" ")
    for j in input().split()[::-1]:
        print(j, end=" ")
    print()