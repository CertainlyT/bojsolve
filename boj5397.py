for i in range(int(input())):
    string = input()
    current_idx = 0
    passwd = []
    for j in range(len(string)):
        if string[j] == "<":
            if current_idx != 0:
                current_idx -= 1
        elif string[j] == ">":
            if current_idx != len(passwd):
                current_idx += 1
        elif string[j] == "-":
            if current_idx != 0:
                passwd = passwd[:current_idx - 1] + passwd[current_idx:]
                current_idx -= 1
        else:
            if current_idx != len(passwd):
                passwd = passwd[:current_idx] + [string[j]] + passwd[current_idx:]
                current_idx += 1
            else:
                passwd.append(string[j])
                current_idx += 1
    for j in range(len(passwd)):
        print(passwd[j], end="")
    print()