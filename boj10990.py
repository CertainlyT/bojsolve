n = int(input())

if n == 1:
    print("*")
else:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        print("*", end="")
        for j in range(2 * (i - 1) - 1):
            print(" ", end="")
        if i != 1:
            print("*", end="")
        print()