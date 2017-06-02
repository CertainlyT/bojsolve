minguk_score = list(map(int, input().split()))
mansae_score = list(map(int, input().split()))

total_1 = sum(minguk_score)
total_2 = sum(mansae_score)

if total_1 == total_2:
    print(total_1)
elif total_1 > total_2:
    print(total_1)
else:
    print(total_2)