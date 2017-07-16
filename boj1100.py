lst = []
for i in range(8):
    n = input()
    lst.append(n)

cnt = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if lst[i][j] == "F":
                    cnt += 1
    if i % 2 == 1:
        for j in range(8):
            if j % 2 == 1:
                if lst[i][j] == "F":
                    cnt += 1

print(cnt)