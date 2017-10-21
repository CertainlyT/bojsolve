lst = []
string = input()
for i in range(len(string)):
    lst.append(string[i:len(string)])

for each in sorted(lst):
    print(each)