n = input()

a = len(n)

if len(n) % 2 == 0:
    if n[0:(len(n)//2)] == n[(len(n)//2):len(n)][::-1]:
        print(1)
    else:
        print(0)
else:
    if n[0:(len(n)//2)] == n[(len(n)//2) + 1:len(n)][::-1]:
        print(1)
    else:
        print(0)