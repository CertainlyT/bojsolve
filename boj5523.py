import sys
a_w = 0
b_w = 0
for i in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] > a[1]:
        a_w += 1
    elif a[0] < a[1]:
        b_w += 1
    else:
        pass

print(a_w, b_w)