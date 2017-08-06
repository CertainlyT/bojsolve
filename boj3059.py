for i in range(int(input())):
    a = list(map(str, input()))
    total = 2015
    a = set(a)
    a = list(a)
    for j in range(len(a)):
        total -= ord(a[j])
    print(total)