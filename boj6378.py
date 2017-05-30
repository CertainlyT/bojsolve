str_list = []
num_list = []
less_num = []
while True:
    n = int(input())
    if n == 0:
        break
    num_list.append(n)

for i in range(len(num_list)):
    a = str(num_list[i])
    total_num = 0
    for j in range(len(a)):
        total_num += int(a[j])
        if total_num < 10:
            continue
        else:
            t = str(total_num)
            total_num = 0
            for o in range(len(t)):
                total_num += int(t[o])
    str_list.append(total_num)


for k in range(len(str_list)):
    print(str_list[k])

