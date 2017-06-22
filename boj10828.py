num_list = []

n = int(input())

for i in range(n):
    input_list = list(map(str, input().split()))
    if input_list[0] == "push":
        num_list.insert(0, int(input_list[1]))
    elif input_list[0] == "pop":
        if len(num_list) != 0:
            print(num_list[0])
            num_list.remove(num_list[0])
        else:
            print(-1)
    elif input_list[0] == "size":
        print(len(num_list))
    elif input_list[0] == "empty":
        if len(num_list) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(num_list) != 0:
            print(num_list[0])
        else:
            print(-1)

