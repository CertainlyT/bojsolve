a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x_total = a * p
if p > c:
    y_total = b + (p - c) * d
else:
    y_total = b

if x_total >= y_total:
    print(y_total)
else:
    print(x_total)