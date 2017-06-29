def rev(a):
    a = int(str(a)[::-1])
    return a

a, b = map(int, input().split())

a = rev(a)
b = rev(b)

print(rev(a+b))