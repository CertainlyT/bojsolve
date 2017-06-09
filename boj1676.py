n = int(input())

for i in range(n - 1, 0, -1):
    n *= i

n = list(str(n))
count = 0
for i in range(len(n) - 1, 0, -1):
    if n[i] == "0":
        count += 1
    else:
        break

print(count)