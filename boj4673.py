num = {i for i in range(1, 10001)}
self = set()

for i in num:
    for j in str(i):
        i += int(j)
    self.add(i)

none_self = sorted(num - self)

for k in none_self:
    print(k)
