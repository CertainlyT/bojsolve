num_list = []
for i in range(5):
    n = int(input())
    num_list.append(n)

for j in range(len(num_list)):
    if num_list[j] < 40:
        num_list[j] = 40

total = 0
for k in range(len(num_list)):
    total += num_list[k]

avg = total / 5

print(int(avg))
