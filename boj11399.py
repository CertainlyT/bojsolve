n = int(input())

total = 0

lst = list(map(int, input().split()))

lst.sort()

for i in range(n):
    total += sum(lst[0:i+1])
    
print(total)