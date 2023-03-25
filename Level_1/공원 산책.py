def solution(park, routes):
    n = len(park)
    m = len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x = i
                y = j
    for route in routes:
        flag = False
        dir, dis = route.split()
        if dir == "N":
            nx = x - int(dis)
            ny = y
        elif dir == "S":
            nx = x + int(dis)
            ny = y
        elif dir == "W":
            nx = x 
            ny = y - int(dis)
        else:
            nx = x
            ny = y + int(dis)
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        for i in range(1, int(dis) + 1):
            if dir == "N":
                if park[x - i][y] == "X":
                    flag = True
            elif dir == "S":
                if park[x + i][y] == "X":
                    flag = True
            elif dir == "W":
                if park[x][y - i] == "X":
                    flag = True
            else:
                if park[x][y + i] == "X":
                    flag = True
        if flag: continue
        x, y = nx, ny 
    return [x, y]

a = ["XXX","XSX","XXX"]
b = ["E 2","S 2","W 1"]
print(solution(a, b))