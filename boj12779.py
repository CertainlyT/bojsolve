import math, fractions

a, b = map(int, input().split())

root_a = int(math.sqrt(a))
root_b = int(math.sqrt(b))

odd = root_b - root_a

print(fractions.Fraction(odd, b - a))
