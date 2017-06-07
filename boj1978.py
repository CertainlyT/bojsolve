import math
num = int(input())

num_list = list(map(int, input().split()))

for i in range(2, int(math.sqrt(max(num_list))+1)):
    for j in range(i*2, max(num_list) + 1, i):
        if j in num_list:
            num_list.remove(j)

if 1 in num_list:
    num_list.remove(1)

print(len(num_list))