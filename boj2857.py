lst = []
k = 1
for i in range(5):
    n = input()
    if "FBI" in n:
        lst.append(k)
    else:
        pass
    k += 1

if len(lst) == 0:
    print("HE GOT AWAY!")
else:
    for i in range(len(lst)):
        print(lst[i], end=" ")

