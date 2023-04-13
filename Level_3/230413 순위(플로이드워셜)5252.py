# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    graph = [[0] * n for _ in range(n)]

    for a, b in results:
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = -1

    for k in range(n):
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                if graph[a][k] == graph[k][b] == 1:
                    graph[a][b] = 1
                    graph[b][a] = -1
                    graph[b][k] = -1
                    graph[k][a] = -1
    for row in graph:
        if row.count(0) == 1:
            answer += 1
    return answer


a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(a, b)