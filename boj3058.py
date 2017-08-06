for i in range(int(input())):
    lst = list(map(int, input().split()))
    lst2 = []
    for j in range(7):
        if lst[j] % 2 == 0:
            lst2.append(lst[j])
    print(sum(lst2), min(lst2))