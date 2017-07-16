n = int(input())

for i in range(2*n-1, 0, -2):
    for j in range(((2*n - 1) - i)//2):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()