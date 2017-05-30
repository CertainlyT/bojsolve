n = int(input())
num_list = []
cnt5 = n // 5
cnt3 = 0
less = n % 5

while cnt5 >= 0:
    if less % 3 == 0:
        cnt3 = less // 3
        num_list.append(cnt5 + cnt3)
    cnt5 -= 1
    less += 5
if len(num_list) != 0:
    print(min(num_list))
else:
    print("-1")
