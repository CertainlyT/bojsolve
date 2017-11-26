import sys
for i in range(int(input())):
    ant_lst = []
    min_lst = []
    max_lst = []
    n, k = map(int, sys.stdin.readline().split())
    for j in range(k):
        num = int(sys.stdin.readline())
        temp = [num, n - num]
        min_lst.append(min(temp))
        max_lst.append(max(temp))
    print(max(min_lst), max(max_lst))