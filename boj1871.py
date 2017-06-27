n = int(input())

for i in range(n):
    alp, num = input().split("-")
    count = 0
    l = 2
    for j in range(3):
        count += (ord(alp[j]) - 65) * (26 ** l)
        l -= 1
    print("nice") if -100 <= count - int(num) <= 100 else print("not nice")