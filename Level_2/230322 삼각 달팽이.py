def solution(n):
    answer = [[1] * x for x in range(1, n + 1)]
    visited = [[False] * x for x in range(1, n + 1)]
    
    x, y = 0, 0
    # 아래 오른쪽 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    dir = 0

    present = 0
    end = 0
    for i in range(1, n + 1): end += i
    
    while present != end:
        present += 1
        visited[x][y] = True
        answer[x][y] = present

        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True:
            dir = (dir + 1) % 3
        nx = x + dx[dir]
        ny = y + dy[dir]
        x, y = nx, ny
    result = []
    for ans in answer:
        for i in ans:
            result.append(i)
    return result