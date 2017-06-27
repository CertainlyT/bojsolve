a_count = [0, 1]
b_count = [1, 1]
n = int(input())

if n > 2:
    for i in range(1, n):
        a1 = a_count[i-1]
        a2 = a_count[i]
        b1 = b_count[i-1]
        b2 = b_count[i]
        a_count.append(a1 + a2)
        b_count.append(b1 + b2)
    print(a_count[n-1], b_count[n-1])
else:
    print(a_count[n-1], b_count[n-1])
