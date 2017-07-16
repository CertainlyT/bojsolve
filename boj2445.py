n = int(input())

if n == 1:
    print("**")
else:
    for i in range(1, n):
        for j in range(i):
            print("*", end="")
        for k in range((2*n)-i*2):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()

    for i in range(2*n):
        print("*", end="")
    print()

    for i in range(n-1, 0, -1):
        for j in range(i):
            print("*", end="")
        for k in range((2*n)-i*2):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()