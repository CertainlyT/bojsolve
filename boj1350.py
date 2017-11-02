n = int(input())
result = 0
lst = list(map(int, input().split()))
cluster = int(input())
for i in range(n):
    if lst[i] % cluster == 0:
        result += lst[i] // cluster
    else:
        result += lst[i] // cluster + 1

print(result * cluster)