n = int(input())
candy_list = []

for i in range(2, n - 3, 2):
    less = n - i
    b = 1
    while True:
        c = less - b
        if c < b + 2:
            break
        candy_list.append([i, b, c])
        b += 1

print(len(candy_list))
