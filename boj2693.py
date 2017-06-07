t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    print(n[2])
