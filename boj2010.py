import sys
n = int(sys.stdin.readline())

a = int(sys.stdin.readline())

for i in range(n-1):
    a += int(sys.stdin.readline())

print(a - (n - 1))