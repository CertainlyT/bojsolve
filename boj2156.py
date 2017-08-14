n = int(input())

wine = [0]
dp = [0 for i in range(10001)]
for i in range(n):
    wine.append(int(input()))

if n < 3:
    print(sum(wine))
else:
    for i in range(1, 3):
        if i == 1:
            dp[i] = wine[i]
        else:
            dp[i] = wine[i] + wine[i-1]
    for i in range(3, n+1):
        rst = 0
        rst = max(wine[i] + dp[i-2], dp[i-1])
        rst = max(rst, wine[i] + wine[i-1] + dp[i-3])
        dp[i] = rst
    print(dp[n])