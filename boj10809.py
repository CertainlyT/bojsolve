string = list(input())
check_list = []

for i in range(97, 123):
    try:
        print(string.index(chr(i)), end=" ")
    except ValueError:
        print(-1, end=" ")