import operator

dic = {}
total = 0
for i in range(10):
    a = int(input())
    total += a
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(total // 10)
print(sorted_dic[0][0])