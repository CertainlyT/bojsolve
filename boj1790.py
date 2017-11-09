n, k = map(int, input().split())

result = 0
length = len(str(n))

while n != 0:
    temp = "1" + "0" * (len(str(n)) - 1)
    temp2 = n - int(temp) + 1
    result += temp2 * length
    n = n - temp2
    length -= 1

case = 9
num = 1
while result - (case * num * 1) > 0:
    result -= case * num
    num *= 10
    k -= case

a = k // len(str(num))

test_case = ""
for i in range(a):
    test_case += str(num)
    num += 1

print(test_case[k-1])