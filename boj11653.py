n = int(input())

num_list = []
a = 2
while n != 1:
    if n % a == 0:
        n = n // a
        num_list.append(a)
        a = 2
    else:
        a += 1

for i in range(len(num_list)):
    print(num_list[i])