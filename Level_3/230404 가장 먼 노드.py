# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def bfs(graph, visited, node, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                node[i] = node[v] + 1
                queue.append(i)
                visited[i] = True

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n + 1)
    node = [0] * (n + 1)

    bfs(graph, visited, node, 1)
    answer = node.count(max(node))
    return answer

a = 6
b = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(a, b))