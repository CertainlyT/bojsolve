import queue


def bfs(lst, check_lst, que, width, height):
    while que.qsize() != 0:
        temp = que.get()
        # left
        if temp[1] > 0:
            if lst[temp[0]][temp[1] - 1] == 1 and check_lst[temp[0]][temp[1] - 1] != 1:
                que.put((temp[0], temp[1] - 1))
                check_lst[temp[0]][temp[1] + 1] = 1
        # right
        if temp[1] + 1 < width:
            if lst[temp[0]][temp[1] + 1] == 1 and check_lst[temp[0]][temp[1] + 1] != 1:
                que.put((temp[0], temp[1] + 1))
                check_lst[temp[0]][temp[1] + 1] = 1
        # up
        if temp[0] > 0:
            if lst[temp[0] - 1][temp[1]] == 1 and check_lst[temp[0] - 1][temp[1]] != 1:
                que.put((temp[0] - 1, temp[1]))
                check_lst[temp[0]][temp[1]] = 1
        # down
        if temp[0] + 1 < height:
            if lst[temp[0] + 1][temp[1]] == 1 and check_lst[temp[0] + 1][temp[1]] != 1:
                que.put((temp[0] + 1, temp[1]))
                check_lst[temp[0] + 1][temp[1]] = 1


for i in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0 for j in range(m)] for c in range(n)]
    check = [[0 for j in range(m)] for c in range(n)]
    print(arr)
    q = queue.Queue()
    for j in range(k):
        a, b = map(int, input().split())
        q.put((a, b - 1))
    bfs(arr, check, q, m, n)
    print(check)
