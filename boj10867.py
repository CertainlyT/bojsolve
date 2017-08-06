n = int(input())
lst = list(map(int, input().split()))
lst = set(lst)
lst = list(lst)
lst.sort()
for i in range(len(lst)):
    print(lst[i], end=" ")