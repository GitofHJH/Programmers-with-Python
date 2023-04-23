# https://school.programmers.co.kr/learn/courses/30/lessons/12952
def dfs(graph, n, x):
    count = 0

    if x == n:
        return 1
    
    for y in range(n):
        graph[x] = y
        for row in range(x):
            if graph[x] == graph[row]:
                break
            if abs(graph[row] - graph[x]) == x - row:
                break
        else:
            count += dfs(graph, n, x + 1)
    return count

def solution(n):
    graph = [0] * n
    return dfs(graph, n, 0)