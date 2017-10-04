for i in range(int(input())):
    string = input()
    answer = ""
    for j in range(len(string)):
        if string[j] != "Z":
            answer += chr(ord(string[j]) + 1)
        else:
            answer += "A"
    print("String #%d" % (i + 1))
    print(answer)
    print()