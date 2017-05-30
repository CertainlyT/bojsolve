n = int(input())

yonsei_score = []
korea_score = []

for i in range(n):
    for j in range(9):
        y, k = map(int, input().split())
        yonsei_score.append(y)
        korea_score.append(k)
    yonsei_total = sum(yonsei_score)
    korea_total = sum(korea_score)
    if yonsei_total > korea_total:
        print("Yonsei")
    elif korea_total > yonsei_total:
        print("Korea")
    else:
        print("Draw")