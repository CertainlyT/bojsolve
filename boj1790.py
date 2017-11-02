n, k = map(int, input().split())
total_length = 0
length = len(str(n))

while n != 0:
    temp = "1" + "0" * (len(str(n)) - 1)
    temp2 = n - int(temp) + 1
    total_length += temp2 * length
    n = n - temp2
    length -= 1

if total_length < k:
    print(-1)
else:
    temp_k = k
    num_length = 1
    nine = 9
    temp_result = 0
    while 1:
        if temp_k < num_length * nine:
            break
        temp_k -= num_length * nine
        num_length += 1
        nine *= 10
    ten = int("1" + "0" * (num_length - 1))
    temp_result = ten + temp_k // num_length - 1
    print(temp_result)
