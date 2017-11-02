from operator import itemgetter

robot_list = []
n = int(input())
for i in range(n):
    temp = list(map(int, input().split()))
    dis = ((temp[0] ** 2 + temp[1] ** 2) ** 0.5) / temp[2]
    robot_list.append(temp + [i + 1] + [dis])

robot_list.sort(key=itemgetter(4))

for i in range(n):
    print(robot_list[i][3])