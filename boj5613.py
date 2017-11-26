result = ""
result += input()
result += input()
result += input()
result = str(int(eval(result)))

while True:
    n = input()
    if n == "=":
        break
    result += n
    result += input()
    result = str(int(eval(result)))

print(eval(result))

