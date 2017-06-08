n = int(input())

score_list = list(map(int, input().split()))

count = 0
total_score = 0

for i in range(n):
    if i == 0:
        if score_list[0] == 1:
            count += 1
            total_score += count
    else:
        if score_list[i] == 1 and score_list[i-1] == 1:
            count += 1
            total_score += count
        elif score_list[i] == 0:
            count = 0
        else:
            count += 1
            total_score += count

print(total_score)