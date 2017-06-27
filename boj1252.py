a, b = map(str, input().split())

a = "0b" + a
b = "0b" + b

total = int(a, 2) + int(b, 2)

total = bin(total)

print(total[2:len(total)])