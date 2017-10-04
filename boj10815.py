def binsearch(left, right, lst, search):
    mid = (left + right) // 2
    if left > right:
        return 0
    elif lst[mid] == search:
        return 1
    elif lst[mid] > search:
        return binsearch(left, mid - 1, lst, search)
    else:
        return binsearch(mid + 1, right, lst, search)


n = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()
m = int(input())
lst2 = list(map(int, input().split()))

for i in range(m):
    print(binsearch(0, len(lst1) - 1, lst1, lst2[i]), end=" ")
print()