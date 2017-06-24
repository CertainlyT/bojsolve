n = int(input())
f = int(input())

num = n - n % 100

for i in range(num, num + 1000000000):
    if i % f == 0:
        if i % 100 < 10:
            print("0" + str(i % 100))
        else:
            print(i % 100)
        break
