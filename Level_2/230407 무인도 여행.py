# https://school.programmers.co.kr/learn/courses/30/lessons/154540
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    maps = [list(map) for map in maps]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def dfs(x, y):
        day = 0
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            day += int(maps[x][y])
            maps[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] != "X" and maps[nx][ny] != 0:
                    stack.append((nx, ny))
        return day
    
    for x in range(n):
        for y in range(m):
            if maps[x][y] != "X" and maps[x][y] != 0:
                answer.append(dfs(x, y))
    if not answer:
        return [-1]     
    return sorted(answer)

a = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(a))