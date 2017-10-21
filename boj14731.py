def square(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    elif n % 2 == 0:
        temp = square(x, n // 2)
        return temp * temp % 1000000007
    else:
        temp = square(x, n // 2)
        return x * temp * temp % 1000000007


result = 0
for i in range(int(input())):
    n, m = map(int, input().split())
    if m != 0:
        result += n * m * square(2, m - 1) % 1000000007

print(result % 1000000007)