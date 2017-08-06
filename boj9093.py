for i in range(int(input())):
    a = list(map(str, input().split()))
    for j in range(len(a)):
        print(a[j][::-1], end=" ")
    print()