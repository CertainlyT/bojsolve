n, k = map(int, input().split())

coin = []
coin_count = 0

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

while k > 0:
    for each in coin:
        if k - each >= 0:
            k -= each
            coin_count += 1
            break

print(coin_count)