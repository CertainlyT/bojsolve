def binsearch(left, right, lst, search):
    if left > right:
        return 0

    mid = (left + right) // 2
    if lst[mid] == search:
        return 1
    elif search < lst[mid]:
        return binsearch(left, mid - 1, lst, search)
    else:
        return binsearch(mid + 1, right, lst, search)


a = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()

b = int(input())
lst2 = list(map(int, input().split()))

for i in range(b):
    print(binsearch(0, len(lst1) - 1, lst1, lst2[i]))