a = int(input())
while True:
    b = int(input())
    if b == 0:
        break
    if b % a == 0:
        print(b, "is a multiple of", str(a)+".")
    else:
        print(b, "is NOT a multiple of", str(a) + ".")