num_list = []
count = 0
while True:
    n = int(input())
    num_list.append(n)
    count += 1
    if count == 10:
        break

total = 0
count = 0
for i in range(len(num_list)):
    total += num_list[i]
    count += 1
    if total >= 100:
        break
    else:
        pass

if total >= 100:
    if total - 100 > 100 - (total - num_list[count-1]):
        print(total - num_list[count-1])
    elif total - 100 == 100 - (total - num_list[count-1]):
        print(total)
    else:
        print(total)
else:
    print(total)