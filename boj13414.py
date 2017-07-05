k, l = map(int, input().split())

lst = []
for i in range(l):
    n = input()
    if n not in lst:
        lst.append(n)
    else:
        lst.remove(n)
        lst.append(n)

for j in range(k):
    print(lst[j])