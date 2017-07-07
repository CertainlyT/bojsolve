h, m, s = map(int, input().split())

s2 = int(input())

total = h * 3600 + m * 60 + s + s2

h1 = 0
m1 = 0
while total >= 3600:
    total -= 3600
    h1 += 1

while total >= 60:
    total -= 60
    m1 += 1

s1 = total

while m1 >= 60:
    m1 -= 60
    h1 += 1

while h1 >= 24:
    h1 -= 24

print(h1, m1, s1)

