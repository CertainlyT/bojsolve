from math import gcd
n = int(input())
num_list = list(map(int, input().split()))

for i in range(1, n):
    a = gcd(num_list[0], num_list[i])
    print(str(num_list[0] // a) + "/" + str(num_list[i] // a))
