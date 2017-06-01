fib_list = [0, 1]
n = int(input())

for i in range(0, n):
    fib_list.append(fib_list[i]+fib_list[i+1])

print(fib_list[n])