import sys
n, k = map(int, input().split())

a = sys.stdin.readline().split()
a = list(map(int, a))
a.sort()
print(a[k-1])