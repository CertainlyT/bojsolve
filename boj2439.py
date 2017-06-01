n = int(input())

for i in range(1, n+1):
    space = n - i
    star = i
    for j in range(space):
        print(" ", end="")
    for k in range(star):
        print("*", end="")
    print()