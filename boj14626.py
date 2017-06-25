isbn = list(input())
check_list = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
isbn_check = []
for i in range(len(isbn) - 1):
    try:
        isbn_check.append(int(isbn[i]) * check_list[i])
    except ValueError:
        check_num = i
        pass

if check_num % 2 == 0:
    for i in range(0, 10):
        if (sum(isbn_check) + i + int(isbn[12])) % 10 == 0:
            print(i)
            break
else:
    for i in range(0, 10):
        if (sum(isbn_check) + i * 3 + int(isbn[12])) % 10 == 0:
            print(i)
            break

