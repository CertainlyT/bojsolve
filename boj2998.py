n = input()

num_dic = {"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}
while len(n) % 3 != 0:
    n = "0" + n

num = ""
for i in range(0, len(n) - 2, 3):
    s = n[i] + n[i+1] + n[i+2]
    num += str(num_dic[s])

print(num)