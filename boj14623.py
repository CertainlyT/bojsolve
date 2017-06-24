a = input()
b = input()

b1 = "0b" + a
b2 = "0b" + b

b1 = int(b1, 2)
b2 = int(b2, 2)

result = str(bin(b1 * b2))

for i in range(2, len(result)):
    print(result[i], end="")