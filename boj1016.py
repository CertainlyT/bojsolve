def getPrimeList(num):
    global primes
    primes = []

    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes

a, b = map(int, input().split())
num = b - a + 1
getPrimeList(b)

for i in primes:
    num -= b // i ** 2

print(num)