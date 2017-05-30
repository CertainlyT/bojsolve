k, n, m = map(int, input().split())

price = k * n

money = price - m

if money > 0:
    print(money)
else:
    print(0)