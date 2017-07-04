n = int(input())

lst = []
for i in range(n):
    s = list(map(int, input().split()))
    s.sort()
    if s[0] == s[1] == s[2]:
        lst.append(10000 + s[0]*1000)
    elif s[0] == s[1] or s[1] == s[2]:
        lst.append(1000 + s[1] * 100)
    else:
        lst.append(s[2] * 100)

print(max(lst))