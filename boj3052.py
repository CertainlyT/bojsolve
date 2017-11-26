dic = {}

for i in range(10):
    n = int(input()) % 42
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

print(len(dic))