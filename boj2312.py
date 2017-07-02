def get_prime(number):
    prime_list = [2]
    num = 3

    while num <= number:
        for x in prime_list:
            if num % x == 0:
                break
            elif x == prime_list[-1]:
                prime_list.append(num)
                break
        num += 1

    return prime_list

n = int(input())
print(get_prime(n))
