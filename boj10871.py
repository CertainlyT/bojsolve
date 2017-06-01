n, x = map(int, input().split())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] >= x:
        num_list[i] = 0

for j in range(len(num_list)):
    if num_list[j] != 0:
        print(num_list[j], end=" ")