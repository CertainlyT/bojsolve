for i in range(int(input())):
    a = [0, 1]
    b = [1, 0]
    n = int(input())
    if n <= 1:
        print(b[n], a[n])
    else:
        for j in range(1, n):
            a.append(a[j-1] + a[j])
            b.append(b[j-1] + b[j])
        print(b[n], a[n])
