n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)

num_list.sort()
for j in range(len(num_list)):
    print(num_list[j])
