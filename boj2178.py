import queue


def bfs(que, visit, bfs_lst, row, col):
    lst = []
    map_lst = [[0 for i in range(col)] for j in range(row)]
    map_lst[0][0] = 1
    while que.qsize() != 0:
        c = q.get()
        visit[c[0]][c[1]] = 1
        if bfs_lst[c[0] + 1][c[1]] == 1:
            if visit[c[0] + 1][c[1]] != 1:
                if (c[0] + 1, c[1]) not in lst:
                    lst.append((c[0] + 1, c[1]))
                    map_lst[c[0] + 1][c[1]] = map_lst[c[0]][c[1]] + 1
                    que.put((c[0] + 1, c[1]))
        if bfs_lst[c[0] - 1][c[1]] == 1:
            if visit[c[0] - 1][c[1]] != 1:
                if (c[0] - 1, c[1]) not in lst:
                    lst.append((c[0] - 1, c[1]))
                    map_lst[c[0] - 1][c[1]] = map_lst[c[0]][c[1]] + 1
                    que.put((c[0] - 1, c[1]))
        if bfs_lst[c[0]][c[1] + 1] == 1:
            if visit[c[0]][c[1] + 1] != 1:
                if (c[0], c[1] + 1) not in lst:
                    lst.append((c[0], c[1] + 1))
                    map_lst[c[0]][c[1] + 1] = map_lst[c[0]][c[1]] + 1
                    que.put((c[0], c[1] + 1))
        if bfs_lst[c[0]][c[1] - 1] == 1:
            if visit[c[0]][c[1] - 1] != 1:
                if (c[0], c[1] - 1) not in lst:
                    lst.append((c[0], c[1] - 1))
                    map_lst[c[0]][c[1] - 1] = map_lst[c[0]][c[1]] + 1
                    que.put((c[0], c[1] - 1))

    return map_lst[row - 1][col - 1]


n, m = map(int, input().split())
lst = [[0 for i in range(m + 1)] for j in range(n + 1)]
visited_list = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        lst[i][j] = int(s[j])

q = queue.Queue()
q.put((0, 0))

print(bfs(q, visited_list, lst, n, m))