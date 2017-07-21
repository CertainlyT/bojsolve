import sys

m = 10000
p = [0]*(m+1)

t = int(sys.stdin.readline())

for i in range(t):
    p[int(sys.stdin.readline())] += 1

for i in range(m+1):
    for j in range(p[i]):
        print(i)