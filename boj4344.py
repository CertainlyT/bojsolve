lst = []
line = int(input())
for i in range(0, line) :
    tLine = input()
    stLine = tLine.split(" ")
    cnt = int(stLine[0])
    aline = []
    for j in range(0, cnt):
        aline.append(int(stLine[j+1]))
    lst.append(aline)

print_list = ["%"]
for j in range(line):
    n = sum(lst[j]) # Good
    len_lst = len(lst[j]) # Good
    avg = n / len_lst # Good
    for k in range(len_lst):
        if lst[j][k] <= avg:
            lst[j][k] = 0
    for k in range(len_lst):
        if 0 in lst[j]:
            lst[j].remove(0)
    len_lst2 = len(lst[j])
    print_list.insert(0, "%.3f" % float(len_lst2 / len_lst * 100))
    for l in range(2):
        print(print_list[l], end="")
    print()
    del print_list[0]
