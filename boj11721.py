string = input()

for i in range(0, len(string), 10):
    try:
        print(string[i:i+10])
    except IndexError:
        print(string[i:len(string)])