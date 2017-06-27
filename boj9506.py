while True:
    n = int(input())
    if n == -1:
        break
    num_list = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            num_list.append(i)

    if sum(num_list) == n:
        print(n, "=", 1, end="")
        for i in range(1, len(num_list)):
            print(" +", num_list[i], end="")
        print()
    else:
        print(n, "is NOT perfect.")