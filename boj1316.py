def find_char(string):
    global cnt
    cnt = 0
    char_dic = {}
    for i in range(len(string)):
        if string[i] not in char_dic:
            char_dic[string[i]] = 1
        elif (string[i] in char_dic) and (string[i] == string[i-1]):
            pass
        else:
            cnt += 1
            break
    return cnt

n = int(input())
count = 0
for j in range(n):
    string = input()
    find_char(string)
    count += cnt

print(n - count)
