import random

num_list = []
for i in range(9):
    num_list.append(int(input()))

while True:
    random.shuffle(num_list)
    if sum(num_list[0:7]) == 100:
        output_list = num_list[0:7]
        output_list.sort()
        for i in range(7):
            print(output_list[i])
        break

