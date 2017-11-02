m, n = map(int, input().split())

result = []
i = 1
j = 1
while i <= n:
    for k in range(j):
        result.append(j)
        i += 1
    j += 1

print(sum(result[m-1:n]))