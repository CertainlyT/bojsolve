n1 = int(input())

for i in range(n1):
    n2 = int(input())
    num = 0
    gpa = 0.0
    for j in range(n2):
        a, b = map(float, input().split())
        num += int(a)
        gpa += a * b
    print(num, round(gpa / num, 1))
