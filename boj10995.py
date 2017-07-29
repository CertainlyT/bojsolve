n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print("* ", end="")
        print()
    else:
        for j in range(n):
            print(" *", end="")
        print()
