st = input()

i = 0
lst = []

while i < len(st):
    if len(st) == 1:
        lst.append(st[i])
        i += 1
    else:
        if st[i] == "c":
            try:
                if st[i+1] == "=":
                    lst.append(st[i]+st[i+1])
                    i += 2
                elif st[i+1] == "-":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        elif st[i] == "d":
            try:
                if st[i+1] == "z":
                    if st[i+2] == "=":
                        lst.append(st[i]+st[i+1]+st[i+2])
                        i += 3
                    else:
                        lst.append(st[i])
                        i += 1
                elif st[i+1] == "-":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        elif st[i] == "l":
            try:
                if st[i+1] == "j":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        elif st[i] == "n":
            try:
                if st[i+1] == "j":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        elif st[i] == "s":
            try:
                if st[i+1] == "=":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        elif st[i] == "z":
            try:
                if st[i+1] == "=":
                    lst.append(st[i]+st[i+1])
                    i += 2
                else:
                    lst.append(st[i])
                    i += 1
            except IndexError:
                lst.append(st[i])
                i += 1
        else:
            lst.append(st[i])
            i += 1

print(len(lst))