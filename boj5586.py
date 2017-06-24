n = input()

joi_count = 0
ioi_count = 0

for i in range(len(n)-2):
    if n[i] == "J":
        if n[i+1] == "O" and n[i+2] == "I":
            joi_count += 1
    elif n[i] == "I":
        if n[i + 1] == "O" and n[i + 2] == "I":
            ioi_count += 1

print(joi_count)
print(ioi_count)
