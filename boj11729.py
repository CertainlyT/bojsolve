def hanoi(n, sp, ep):
    if n:
        hanoi(n-1, sp, 6-sp-ep)
        hanoi_list.append((sp, ep))
        hanoi(n-1, 6-sp-ep, ep)

hanoi_list = []
n = int(input())
hanoi(n, 1, 3)
print(len(hanoi_list))
for i in range(len(hanoi_list)):
    print(hanoi_list[i][0], hanoi_list[i][1])