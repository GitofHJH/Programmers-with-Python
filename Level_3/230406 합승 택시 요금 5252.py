# https://school.programmers.co.kr/learn/courses/30/lessons/72413
import heapq    

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[] for _ in range(n + 1)]
    for c, d, f in  fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    def dijkstra(start):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    dist = [[]]
    for i in range(1, n + 1):
        dist.append(dijkstra(i))

    for i in range(1, n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer

n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))