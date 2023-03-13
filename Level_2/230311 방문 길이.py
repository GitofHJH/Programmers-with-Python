def solution(dirs):
    answer = 0
    x, y = 0, 0
    dx = {"U":0, "D":0, "R":1, "L":-1}
    dy = {"U":1, "D":-1, "R":0, "L":0}

    visited = []
    
    for dir in dirs:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        temp = [(x, y), (nx, ny)]
        temp = sorted(temp)
        if temp not in visited:
            answer += 1
            visited.append(temp)

        x, y = nx, ny
    
    return answer

print(solution("ULURRDLLU"))