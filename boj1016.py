a, b = map(int, input().split())

i = 2
num_list = {4}
while i**2 < b:
    num_list.add(i**2)
    i += 1

for i in sorted(num_list):
    for j in range(i*2, b + 1, i):
        if j > b:
            break
        num_list.add(j)

print(b - a + 1 - len(num_list))