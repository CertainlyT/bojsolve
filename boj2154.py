string = ""
n = int(input())
for i in range(1, n + 1):
    string += str(i)

print(string.find(str(n)) + 1)