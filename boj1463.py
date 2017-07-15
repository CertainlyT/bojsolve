n = int(input())

lst = [0, 0, 1, 1]

for i in range(4, n+1):
    lst.append(lst[i-1] + 1)
    if i % 2 == 0:
        b = lst[i//2] + 1
        if b < lst[i]:
            lst[i] = b
    if i % 3 == 0:
        b = lst[i//3] + 1
        if b < lst[i]:
            lst[i] = b

print(lst[n])