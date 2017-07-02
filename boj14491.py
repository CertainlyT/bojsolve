a = int(input())

string = ""
while a != 0:
    a, n = divmod(a, 9)
    string = str(n) + string

print(string)