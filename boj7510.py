n = int(input())

for i in range(1, n+1):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print("Scenario #" + str(i) + ":")
        print("yes")
        print()
    else:
        print("Scenario #" + str(i) + ":")
        print("no")
        print()