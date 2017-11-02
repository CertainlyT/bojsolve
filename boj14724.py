lst = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

n = int(input())
score = []
for i in range(9):
    score.append(max(list(map(int, input().split()))))

print(lst[score.index(max(score))])