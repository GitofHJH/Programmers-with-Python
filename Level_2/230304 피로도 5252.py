answer = 0
def dfs(k, dungeons, visited, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if visited[i] == False and dungeons[i][0] <= k:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, visited, cnt + 1)
            visited[i] = False

def solution(k, dungeons):
    global answer
    dungeons = sorted(dungeons, key=lambda x : -(x[0] - x[1]))
    visited = [False] * len(dungeons)

    dfs(k, dungeons, visited, 0)
    return answer

a = 80
b = [[80,20],[50,40],[30,10]]
print(solution(a, b))