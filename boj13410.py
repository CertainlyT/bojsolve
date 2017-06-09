a, b = map(int, input().split())
num_list = []

for i in range(1, b+1):
    c = a * i
    num_list.append(c)

for j in range(len(num_list)):
    if num_list[j] < 10:
        pass
    elif 10 <= num_list[j] < 100:
        num_list[j] = int(str(num_list[j] % 10) + str(num_list[j] // 10))
    elif 100 <= num_list[j] < 1000:
        num_list[j] = int(str(num_list[j] % 10) + str(num_list[j] % 100 // 10) + str(num_list[j] // 100))
    elif 1000 <= num_list[j] < 10000:
        num_list[j] = int(str(num_list[j] % 10) + str(num_list[j] % 100 // 10) + str(num_list[j] % 1000 // 100)
                          + str(num_list[j] // 1000))
    elif 10000 <= num_list[j] < 100000:
        num_list[j] = int(str(num_list[j] % 10) + str(num_list[j] % 100 // 10) + str(num_list[j] % 1000 // 100)
                          + str(num_list[j] % 10000 // 1000) + str(num_list[j] % 100000 // 10000))
    elif num_list[j] == 1000000:
        num_list[j] = 1
    else:
        num_list[j] = int(str(num_list[j] % 10) + str(num_list[j] % 100 // 10) + str(num_list[j] % 1000 // 100)
                          + str(num_list[j] % 10000 // 1000) + str(num_list[j] % 100000 // 10000)
                          + str(num_list[j] % 1000000 // 100000))

print(max(num_list))
