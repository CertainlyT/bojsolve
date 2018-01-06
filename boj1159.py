answer = []
dic = {}

for i in range(int(input())):
    n = input()
    if n[0] in dic:
        dic[n[0]] += 1
    else:
        dic[n[0]] = 1

for each in dic:
    if dic[each] >= 5:
        answer += each

if len(answer) == 0:
    print("PREDAJA")
else:
    for each in sorted(answer):
        print(each, end="")
    print()