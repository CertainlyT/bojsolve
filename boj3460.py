n = int(input())
for i in range(n):
    a = bin(int(input()))
    a = a[2:][::-1]
    for j in range(len(a)):
        if a[j] == "1":
            print(j, end=" ")