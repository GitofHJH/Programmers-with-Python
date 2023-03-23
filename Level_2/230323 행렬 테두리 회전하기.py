def solution(rows, columns, queries):
    answer = []
    graph = [[y + 1 + columns * x for y in range(columns)] for x in range(rows)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for x, y, endx, endy in queries:
        record = rows * columns + 1
        x -= 1
        y -= 1
        endx -=1
        endy -=1
        startx = x
        starty = y
        # 우 하 좌 상
        dir = 0
        tmp = graph[x][y]
        while 1:
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < startx or nx > endx or ny < starty or ny > endy:
                dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
            tmp2 = graph[nx][ny]
            graph[nx][ny] = tmp
            record = min(record, tmp)
            if nx == startx and ny == starty:
                break
            x = nx
            y = ny
            tmp = tmp2
        answer.append(record)
    return answer

a = 3
b = 3
c = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(a,b,c))