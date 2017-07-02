import operator
n = int(input())

num_list = []
for i in range(n):
    a = tuple(map(int, input().split()))
    num_list.append(a)

num_list.sort(key=operator.itemgetter(0))

total_time = 0
for i in range(n):
    if num_list[i][0] >= total_time:
        total_time = num_list[i][0]
        total_time += num_list[i][1]
    else:
        total_time += num_list[i][1]

print(total_time)
