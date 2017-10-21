n = int(input())
result = 0
length = len(str(n))

while n != 0:
    temp = "1" + "0" * (len(str(n)) - 1)
    temp2 = n - int(temp) + 1
    result += temp2 * length
    n = n - temp2
    length -= 1

print(result)