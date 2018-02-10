lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()

name_lst = []

for i in range(len(a)):
    name_lst.append(lst[ord(a[i]) - 65])
    name_lst.append(lst[ord(b[i]) - 65])

temp = []

while len(name_lst) != 2:
    for i in range(len(name_lst) - 1):
        temp.append((name_lst[i] + name_lst[i + 1]) % 10)
    name_lst = temp
    temp = []

print(str(name_lst[0]) + str(name_lst[1]))