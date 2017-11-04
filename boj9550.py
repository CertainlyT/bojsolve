for i in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    for j in range(n):
        result += lst[j] // k
    print(result)
