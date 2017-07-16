import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

a = int(sys.stdin.readline())
chk_lst = list(map(int, sys.stdin.readline().split()))

for i in chk_lst:
    if i in lst:
        print(1)
    else:
        print(0)