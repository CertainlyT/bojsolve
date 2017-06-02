num_list = []
total = 0
for i in range(4):
    a, b = map(int, input().split())
    total += b
    total -= a
    num_list.append(total)

print(max(num_list))
