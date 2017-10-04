n = int(input())

lst = list(map(int, input().split()))

lst.sort()

print(max(lst[0] * lst[1] * lst[len(lst) - 1], lst[0] * lst[1], lst[len(lst) - 1] * lst[len(lst) - 2], lst[len(lst) - 1] * lst[len(lst) - 2] * lst[len(lst) - 3]))