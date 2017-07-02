n = input()

n = "0o" + n

n = int(n, 8)

print(str(bin(n))[2:])
