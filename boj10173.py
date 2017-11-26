while True:
    s = input()
    n = ""
    for i in range(len(s)):
        n += s[i].lower()
    if n == "eoi":
        break
    a = n.find("nemo")
    if a == -1:
        print("Missing")
    else:
        print("Found")