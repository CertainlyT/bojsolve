length = 0

lst = ["@"] * 5

for i in range(5):
    lst[i] = list(map(str, input()))
    length = len(lst[i]) if length < len(lst[i]) else length

string = ""
for i in range(length):
    for j in range(5):
        try:
            string += lst[j][i]
        except IndexError:
            pass

print(string)