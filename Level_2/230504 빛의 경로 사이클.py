# https://school.programmers.co.kr/learn/courses/30/lessons/86052
def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    # 하우상좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    route_all = set()
    for x in range(n):
        for y in range(m):
            init_x = x
            init_y = y
            for d in range(4):
                if (x, y, d) in route_all:
                    continue
                cost = 0
                init_d = d
                while 1:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0:
                        nx = n - 1
                    if nx >= n:
                        nx = 0
                    if ny < 0:
                        ny = m - 1
                    if ny >= m:
                        ny = 0
                    if grid[nx][ny] == "S":
                        x, y = nx, ny
                    elif grid[nx][ny] == "L":
                        x, y = nx, ny
                        d = (d + 1) % 4
                    else:
                        x, y = nx, ny
                        d -= 1
                        if d == -1: d = 3
                    route_all.add((x, y, d))
                    cost += 1
                    if x == init_x and y == init_y and d == init_d:
                        answer.append(cost)
                        break
    answer.sort()
    return answer

a = ["SL","LR"]
solution(a)