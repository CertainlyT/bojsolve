import queue


def bfs(lst, row, col, que, visit):
    while que.qsize() != 0:
        c = q.get()
        visit[c[0]][c[1]] = 1
        if c[0] < row - 1 and visit[c[0] + 1][c[1]] == 0 and lst[c[0]][c[1]] != 0 and lst[c[0] + 1][c[1]] != 0:  # down
            visit[c[0] + 1][c[1]] = 1
            lst[c[0] + 1][c[1]] = lst[c[0]][c[1]] + 1
            que.put((c[0] + 1, c[1]))
        if c[0] > 0 and visit[c[0] - 1][c[1]] == 0 and lst[c[0]][c[1]] != 0 and lst[c[0] - 1][c[1]] != 0:  # up
            visit[c[0] - 1][c[1]] = 1
            lst[c[0] - 1][c[1]] = lst[c[0]][c[1]] + 1
            que.put((c[0] - 1, c[1]))
        if c[1] > 0 and visit[c[0]][c[1] - 1] == 0 and lst[c[0]][c[1]] != 0 and lst[c[0]][c[1] - 1] != 0:  # left
            visit[c[0]][c[1] - 1] = 1
            lst[c[0]][c[1] - 1] = lst[c[0]][c[1]] + 1
            que.put((c[0], c[1] - 1))
        if c[1] < col - 1 and visit[c[0]][c[1] + 1] == 0 and lst[c[0]][c[1]] != 0 and lst[c[0]][c[1] + 1] != 0:  # right
            visit[c[0]][c[1] + 1] = 1
            lst[c[0]][c[1] + 1] = lst[c[0]][c[1]] + 1
            que.put((c[0], c[1] + 1))
    return lst[row - 1][col - 1]


n, m = map(int, input().split())
adj_matrix = [[0 for i in range(m)] for j in range(n)]
visit_matrix = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    s = input()
    for j in range(m):
        adj_matrix[i][j] = int(s[j])

q = queue.Queue()
q.put((0, 0))

print(bfs(adj_matrix, n, m, q, visit_matrix))
