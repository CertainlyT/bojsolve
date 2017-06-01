lst = []
line = int(input())
for i in range(0, line) :
    tLine = list(input())
    lst.append(tLine)

count = 0
total_score = 0
for j in range(len(lst)):
    for k in range(len(lst[j])):
        if k == 0:
            if lst[j][k] == "O":
                count += 1
                total_score += count
        else:
            if lst[j][k] == "O" and lst[j][k-1] == "O":
                count += 1
                total_score += count
            if lst[j][k] == "X":
                count = 0
            if lst[j][k] == "O" and lst[j][k-1] == "X":
                count += 1
                total_score += count
    print(total_score)
    count = 0
    total_score = 0
print()