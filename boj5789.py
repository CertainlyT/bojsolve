n = int(input())
for i in range(n):
    num_list = input()
    check = int(len(num_list) / 2)
    if num_list[check] == num_list[check - 1]:
        print("Do-it")
    else:
        print("Do-it-Not")