length, a, b = map(int, input().split())

length *= length

height = a * a
width = b * b

print(int((length * (height / (height + width))) ** 0.5), int((length * (width / (height + width))) ** 0.5))