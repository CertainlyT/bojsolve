student_dic = {}
n, k = map(int, input().split())

room = 0
for i in range(n):
    s, g = map(int, input().split())
    key = str(s) + "_" + str(g)
    if key not in student_dic:
        student_dic[key] = 1
    else:
        student_dic[key] += 1

for each in student_dic:
    if student_dic[each] % k == 0:
        room += student_dic[each] // k
    else:
        room += student_dic[each] // k + 1

print(room)
