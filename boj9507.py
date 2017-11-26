for j in range(int(input())):
    koong = [1, 1, 2, 4]
    n = int(input())
    if n < 2:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        for i in range(3, n + 1):
            koong.append(koong[i - 3] + koong[i - 2] + koong[i - 1] + koong[i])
        print(koong[n])