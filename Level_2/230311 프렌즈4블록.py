def solution(m, n, board):
    answer = 0
    graph = [list(x) for x in board]
    record = []

    while 1:
        # 지울 부분 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                tmp = graph[i][j]
                if tmp != "#" and graph[i + 1][j] == tmp and graph[i][j + 1] == tmp and graph[i + 1][j + 1] == tmp:
                    record.append((i, j))
                    record.append((i + 1, j))
                    record.append((i, j + 1))
                    record.append((i + 1, j + 1))
        # 기록이 비어있다면 종료
        if record == []:
            break
        # 지우기
        for x, y in record:
            graph[x][y] = "#"
        # 밑으로 내리기
        for i in range(m-2, -1, -1):
            for j in range(n):
                for k in range(m-1, i, -1):
                    if graph[k][j] == "#":
                        graph[i][j], graph[k][j] = graph[k][j], graph[i][j]
                        break
        # 기록 초기화
        record = []

    # # 개수 세기
    for i in range(m):
        for j in range(n):
            if graph[i][j] == "#":
                answer += 1
    
    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))