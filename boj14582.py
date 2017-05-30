score1 = list(map(int, input().split()))
score2 = list(map(int, input().split()))

score1_total = 0
score2_total = 0

check_score = []
check_score1 = []
check_score2 = []

for i in range(9):
    score1_total += score1[i]
    if score1_total > score2_total:
        check_score1.append(1)
        check_score2.append(-1)
    else:
        check_score1.append(-1)
        check_score2.append(1)
    score2_total += score2[i]
    if score2_total > score1_total:
        check_score2[i] = 1
if score2_total > score1_total:
    check_score2[8] = 1

for i in range(9):
    check_score.append(check_score1[i] + check_score2[i])

if 2 in check_score and check_score2[8] == 1:
    print("Yes")
else:
    print("No")
