n = int(input())

num_list = [1, 1, 1]

for i in range(1, n+1):
    num_list.append(num_list[i-1] + num_list[i+1])

print(num_list[n-1])