for i in range(int(input())):
    case = input().split()
    while True:
        test = input().split()
        if test == "what does the fox say?".split():
            for j in range(len(case)):
                print(case[j], end=" ")
            break

        removed_list = []
        for j in range(len(case)):
            if case[j] != test[2]:
                removed_list.append(case[j])
        case = removed_list
