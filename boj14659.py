n = int(input())
lst = list(map(int, input().split()))

rst = 0
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if lst[i] >= lst[j]:
            cnt += 1
        else:
            rst = cnt if rst < cnt else rst
            cnt = 0
            break
    rst = cnt if rst < cnt else rst
    cnt = 0
    if rst == n - 1:
        break

print(rst)