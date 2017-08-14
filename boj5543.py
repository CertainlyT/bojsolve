burger = []
beverage = []

for i in range(3):
    burger.append(int(input()))

for i in range(2):
    beverage.append(int(input()))

print(min(burger) + min(beverage) - 50)