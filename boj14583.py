import math
h, v = map(float, input().split())

a = v * h / (h + math.sqrt(h**2 + v**2))

l = (h*v - h*a) / 2

prop = h / v

b = math.sqrt(l * prop)

print("%.2f" % float(b), "%.2f" % float(b / prop))
