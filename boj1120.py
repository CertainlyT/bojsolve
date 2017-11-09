a, b = input().split()

diff = len(b) - len(a)

result = 50
for i in range(diff + 1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            temp += 1

    result = result if temp > result else temp

print(result)