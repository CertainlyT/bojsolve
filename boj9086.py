n = int(input())
str_list = []

for i in range(n):
    n = list(input())
    str_list.append(n)

for j in range(len(str_list)):
    a = 0
    b = len(str_list[j]) - 1
    print(str_list[j][a] + str_list[j][b])
