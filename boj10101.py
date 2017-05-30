num_list = []

for i in range(3):
    n = int(input())
    num_list.append(n)

num_list.sort()

if sum(num_list) != 180:
    print("Error")
elif num_list[0] == num_list[1] == num_list[2] == 60:
    print("Equilateral")
elif num_list[0] != num_list[1] != num_list[2]:
    print("Scalene")
else:
    print("Isosceles")