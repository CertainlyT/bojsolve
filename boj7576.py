import queue


def bfs(lst, row, col, que, visit):
    matrix = [[0 for i in range(m)] for j in range(n)]
    while que.qsize() != 0:
        c = que.get()
        visit[c[0]][c[1]] = 1
        if c[0] < row - 1 and visit[c[0] + 1][c[1]] == 0 and lst[c[0]][c[1]] == 1 and lst[c[0] + 1][c[1]] == 0:  # down
            visit[c[0] + 1][c[1]] = 1
            matrix[c[0] + 1][c[1]] = matrix[c[0]][c[1]] + 1
            lst[c[0] + 1][c[1]] = 1
            que.put((c[0] + 1, c[1]))
        if c[0] > 0 and visit[c[0] - 1][c[1]] == 0 and lst[c[0]][c[1]] == 1 and lst[c[0] - 1][c[1]] == 0:  # up
            visit[c[0] - 1][c[1]] = 1
            matrix[c[0] - 1][c[1]] = matrix[c[0]][c[1]] + 1
            lst[c[0] - 1][c[1]] = 1
            que.put((c[0] - 1, c[1]))
        if c[1] > 0 and visit[c[0]][c[1] - 1] == 0 and lst[c[0]][c[1]] == 1 and lst[c[0]][c[1] - 1] == 0:  # left
            visit[c[0]][c[1] - 1] = 1
            matrix[c[0]][c[1] - 1] = matrix[c[0]][c[1]] + 1
            lst[c[0]][c[1] - 1] = 1
            que.put((c[0], c[1] - 1))
        if c[1] < col - 1 and visit[c[0]][c[1] + 1] == 0 and lst[c[0]][c[1]] == 1 and lst[c[0]][c[1] + 1] == 0:  # right
            visit[c[0]][c[1] + 1] = 1
            matrix[c[0]][c[1] + 1] = matrix[c[0]][c[1]] + 1
            lst[c[0]][c[1] + 1] = 1
            que.put((c[0], c[1] + 1))
    return matrix


m, n = map(int, input().split())

tomato_matrix = []

for i in range(n):
    tomato_matrix.append(list(map(int, input().split())))

check = 1
for i in range(n):
    flag = False
    for j in range(m):
        if tomato_matrix[i][j] != 1:
            check = 0
            flag = True
            break
    if flag:
        break

if check == 1:
    print(0)
else:
    q = queue.Queue()

    for i in range(n):
        for j in range(m):
            if tomato_matrix[i][j] == 1:
                q.put((i, j))

    visited_list = [[0 for i in range(m)] for j in range(n)]

    answer_matrix = bfs(tomato_matrix, n, m, q, visited_list)

    max_num = -2

    for i in range(n):
        flag = False
        for j in range(m):
            if tomato_matrix[i][j] == 0:
                max_num = -1
                flag = True
                break
            if max_num < answer_matrix[i][j]:
                max_num = answer_matrix[i][j]
        if flag:
            break

    if max_num == -1:
        print(-1)
    else:
        print(max_num)
