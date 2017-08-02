rst = 0
n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    if lst[i] != i + 1:
        rst += 1
print(rst)