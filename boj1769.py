def to_list(string):
    lst = []
    for i in range(len(string)):
        lst.append(int(string[i]))
    return lst


def to_sum(lst):
    num = 0
    for i in range(len(lst)):
        num += int(lst[i])
    return num


s = input()
cnt = 0
if int(s) < 10:
    cnt -= 1
while True:
    a = to_sum(s)
    cnt += 1
    if a < 10:
        break
    s = to_list(str(a))


print(cnt)
print("YES" if a % 3 == 0 else "NO")