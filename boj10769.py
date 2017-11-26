n = input()

a = n.count(":-)")
b = n.count(":-(")

if a == 0 and b == 0:
    print("none")
elif a == b:
    print("unsure")
elif a > b:
    print("happy")
else:
    print("sad")