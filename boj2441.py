n = int(input())

for i in range(n+1):
    space = i
    star = n - i
    for j in range(space):
        print(" ", end="")
    for k in range(star):
        print("*", end="")
    print()

