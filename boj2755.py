score_list = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7,
        "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
n = int(input())

score_point = 0
score = 0
for i in range(n):
    lst = list(input().split())
    score_point += int(lst[1])
    score += int(lst[1]) * score_list[lst[2]]

if (score / score_point) * 1000 % 10 == 5:
    score += 0.1
print("%.2f" % (score / score_point))


