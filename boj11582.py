n = int(input())

lst = list(map(int, input().split()))

x = n // int(input())

lst2 = []
for i in range(0, len(lst), x):
    lst2 += sorted(lst[i:i+x])

for i in range(len(lst2)):
    print(lst2[i], end=" ")
print()