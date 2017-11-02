rice = input()

result = 10
for i in range(1, len(rice)):
    if rice[i] == rice[i - 1]:
        result += 5
    else:
        result += 10

print(result)