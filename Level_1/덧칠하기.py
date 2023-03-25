def solution(n, m, section):
    answer = 0
    visited = [False] * (n + 1)
    for s in section:
        if visited[s] == False:
            for i in range(m):
                visited[s + i] = True
            answer += 1
        else:
            continue
    return answer