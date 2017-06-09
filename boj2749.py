import time
n = int(input())
a = 0
b = 1
start = time.time()
count = 0
while count != n:
    c = a + b
    a = b
    b = c
    count += 1

print(a % 1000000)
end = time.time()
print(end-start)