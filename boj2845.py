people_num = list(map(int, input().split()))
paper_num = list(map(int, input().split()))

people_num_total = people_num[0] * people_num[1]

for i in range(len(paper_num)):
    paper_num[i] -= people_num_total

for j in range(len(paper_num)):
    print(paper_num[j], end=" ")
