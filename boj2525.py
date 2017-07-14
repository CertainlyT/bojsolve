h, m = map(int, input().split())
p = int(input())

total_minute = h*60 + m + p

r_h = 0

while total_minute >= 60:
    total_minute -= 60
    r_h += 1

while r_h >= 24:
    r_h -= 24

r_m = total_minute
print(r_h, r_m)