n = int(input())
price_list = list(map(int, input().split()))

sum_price = sum(price_list)
min_price = 50000000

for i in range(1, n):
    price = sum_price - price_list[i]
    if min_price > price:
        min_price = price

print(min_price)
