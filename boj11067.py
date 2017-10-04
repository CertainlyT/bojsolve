real_result = []
for i in range(int(input())):
    n = int(input())
    lst = []

    for j in range(n):
        a = list(map(int, input().split()))
        lst.append(a)

    lst.sort()

    result = [lst[0]]
    temp = []

    for j in range(1, n):
        if lst[j][0] == result[len(result) - 1][0]:
            result.append(lst[j])
            if len(temp) != 0:
                temp = temp[::-1]
                for k in range(len(temp)):
                    result.append(temp[k])
                temp = []
        elif lst[j][1] == result[len(result) - 1][1]:
            result.append(lst[j])
            if len(temp) != 0:
                temp = temp[::-1]
                for k in range(len(temp)):
                    result.append(temp[k])
                temp = []
        else:
            temp.append(lst[j])

    check = list(map(int, input().split()))

    for j in range(check[0]):
        print(result[check[j + 1] - 1][0], result[check[j + 1] - 1][1])

