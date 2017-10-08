n = input()

a = 0
b = 0
a_win = 0
b_win = 0
score_list = []
for i in range(len(n)):
    if n[i] == "A":
        a +=1
    else:
        b += 1

    if a == 21:
        a_win += 1
        score_list.append([a, b])
        a = 0
        b = 0
    elif b == 21:
        b_win += 1
        score_list.append([a, b])
        a = 0
        b = 0

for i in range(len(score_list)):
    print(str(score_list[i][0]) + "-" + str(score_list[i][1]))

print("A" if a_win == 2 else "B")