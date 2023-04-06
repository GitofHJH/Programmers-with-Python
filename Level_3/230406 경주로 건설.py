# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque

def solution(board):
    INF = int(1e9)
    n = len(board)
    m = len(board[0])
    graph = [[[INF, INF, INF, INF] for _ in range(m)] for _ in range(n)]
    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    graph[0][0] = [0, 0, 0, 0]
    q = deque([(0, 0, 0), (0, 0, 2)])
    while q:
        x, y, dir = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 1:
                continue
            cost = graph[x][y][dir]
            n_cost = cost + 100
            if dir != i: n_cost += 500
            if n_cost < graph[nx][ny][i]:
                graph[nx][ny][i] = n_cost
                if nx == n-1 and ny == m-1:
                    continue
                q.append((nx, ny, i))         
    return min(graph[n-1][m-1])

a = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
b = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(b))