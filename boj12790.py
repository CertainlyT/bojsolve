def fight(lst):
    for i in range(4):
        lst[i] += lst[i+4]
    for i in range(3):
        if i == 0 or i == 1:
            if lst[i] < 1:
                lst[i] = 1
        else:
            if lst[i] < 0:
                lst[i] = 0
    print(lst[0] + 5 * lst[1] + 2 * lst[2] + 2 * lst[3])

for i in range(int(input())):
    fight(list(map(int, input().split())))