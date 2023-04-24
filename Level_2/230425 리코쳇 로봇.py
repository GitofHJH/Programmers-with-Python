# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                x_s, y_s = i, j
            if board[i][j] == "G":
                x_g, y_g = i, j
    graph = [[int(1e9)]*m for _ in range(n)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # bfs
    graph[x_s][y_s] = 0
    q = deque([(x_s, y_s, 0)])
    while q:
        x_s, y_s, cost = q.popleft()
        x, y = x_s, y_s
        for i in range(4):
            while 1:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if board[nx][ny] == "D":
                    break
                x, y = nx, ny
            if x != x_s or y != y_s:
                if cost + 1 < graph[x][y]:
                    q.append((x, y, cost + 1))
                    graph[x][y] = min(graph[x][y], cost + 1)
            x, y = x_s, y_s
    ans = graph[x_g][y_g]
    if ans == int(1e9):
        return -1
    return ans

board = [".D.R", "....", ".G..", "...D"]
print(solution(board))