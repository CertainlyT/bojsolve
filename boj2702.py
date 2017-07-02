from math import gcd
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b) * (a // gcd(a, b)) * (b // gcd(a, b)), gcd(a, b))
