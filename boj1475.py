n = input().replace("9", "6")
num_list = []
for i in range(9):
    num_list.append(n.count(str(i)))

if num_list[6] % 2 == 1:
    num_list[6] = num_list[6] // 2 + 1
else:
    num_list[6] = num_list[6] // 2

print(max(num_list))
