n = int(input())
num_list = []

for i in range(n):
    a = int(input())
    num_list.append(a)

for i in range(n):
    print(sorted(num_list)[i])