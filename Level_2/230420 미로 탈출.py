from collections import deque

def bfs(start, end, maps):
    n = len(maps)
    m = len(maps[0])
    x_s, y_s = start
    x_e, y_e = end
    visited = [[False] * m for _ in range(n)]
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x_s, y_s, 0)])
    visited[x_s][y_s] = True
    while q:
        x, y, cost = q.popleft()
        if x == x_e and y == y_e:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == "X":
                continue
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            q.append((nx, ny, cost + 1))
            
    return -1
            
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 좌표값 얻기
    for x in range(n):
        for y in range(m):
            if maps[x][y] == "S":
                x_s, y_s = x, y
            if maps[x][y] == "L":
                x_l, y_l = x, y
            if maps[x][y] == "E":
                x_e, y_e = x, y
    s_to_l = bfs((x_s, y_s), (x_l, y_l), maps)
    l_to_e = bfs((x_l, y_l), (x_e, y_e), maps)
    if s_to_l != -1 and l_to_e != -1:
        return s_to_l + l_to_e
    return -1

a = ["SEOOL", "XOOXX", "XXXXX", "XXXOO", "XXXXX", "XXXXX"]
b = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
print(solution(a))