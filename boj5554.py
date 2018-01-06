total = 0
for i in range(4):
    total += int(input())

print("%d\n%d" % divmod(total, 60))