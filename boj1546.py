n = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)

total_score = 0
for i in range(n):
    score_list[i] = (score_list[i] / max_score) * 100
    total_score += score_list[i]

print("%.2f" % float(total_score / n))
