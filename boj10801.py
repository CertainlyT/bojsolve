a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_w = 0
b_w = 0
for i in range(10):
    if a[i] == b[i]:
        pass
    else:
        if a[i] > b[i]:
            a_w += 1
        else:
            b_w += 1

if a_w == b_w:
    print("D")
else:
    print("A" if a_w > b_w else "B")

