n = int(input())

count = 0
for i in range(1, n+1):
    if 1 <= i < 100:
        count += 1
    else:
        if 100 <= i < 1000:
            if (i // 100 - i % 100 // 10) == (i % 100 // 10 - i % 10):
                count += 1

print(count)