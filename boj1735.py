from math import gcd

result = []
n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())

gcd1 = gcd(m1, m2)
result.append((m1 // gcd1) * (m2 // gcd1) * gcd1)
result.append(n1 * (result[0] // m1) + n2 * (result[0] // m2))

if gcd(result[0], result[1]) == 1:
    print(result[1], result[0])
else:
    print(result[1] // gcd(result[0], result[1]), result[0] // gcd(result[0], result[1]))
