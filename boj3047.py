lst = list(map(int, input().split()))
abc = input()

lst.sort()
temp = []
min_num = min(lst)
max_num = max(lst)
lst.remove(min_num)
lst.remove(max_num)
other = lst[0]
dic = {"A": min_num, "B": other, "C": max_num}
for i in range(3):
    print(dic[abc[i]], end=" ")
print()
