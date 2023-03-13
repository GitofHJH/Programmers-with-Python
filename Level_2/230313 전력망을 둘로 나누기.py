import copy

def make_graph(n, array):
    graph = [[] for _ in range(n + 1)]
    for x, y in array:
        graph[x].append(y)
        graph[y].append(x)
    return graph

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def solution(n, wires):
    answer = n
    wires_org = copy.deepcopy(wires)
    for w in wires:
        wires = copy.deepcopy(wires_org)
        wires.remove(w)
        graph = make_graph(n, wires)
        visited = [False] * (n + 1)
        dfs(graph, 1, visited)
        count = len([x for x in visited if x == True])
        answer = min(answer, abs(count - (n-count)))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))