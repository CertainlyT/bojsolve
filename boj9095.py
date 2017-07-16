lst = [1, 2, 4]

a = int(input())

for j in range(a):
    n = int(input())
    if n <= 3:
        print(lst[n-1])
    else:
        lst = [1, 2, 4]
        for i in range(n-3):
            lst.append(lst[i] + lst[i+1] + lst[i+2])
        print(lst[n-1])
