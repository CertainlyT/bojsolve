for i in range(int(input())):
    n = int(input())
    print("#" * n)
    for j in range(n - 2):
        print("#" + "J" * (n - 2) + "#")
    if n != 1:
        print("#" * n)
    print()
