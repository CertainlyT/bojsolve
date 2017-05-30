string = input()
n = len(string)
a = n // 10
b = n % 10
if a == 0:
    for i in range(b):
        print(string[i], end="")
else:
    for i in range(1, a+1):
        for j in range(10*(i-1), 10*i):
            print(string[j], end="")
        print()
    else:
        for i in range(10*a, 10*a+b):
            print(string[i], end="")
        print()