n = int(input())
num_list = [0, 1]
for i in range(n-1):
    num_list.append(num_list[i]+num_list[i+1])

print(num_list[n])