n = input()
lst = []
for i in range(len(n)):
    lst.append(int(n[i]))

if 0 in lst and sum(lst) % 3 == 0:
    result = ""
    for each in sorted(lst, reverse=True):
        result += str(each)
    print(result)
else:
    print(-1)