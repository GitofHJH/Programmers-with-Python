# https://school.programmers.co.kr/learn/courses/30/lessons/43164
answer = []
def dfs(plan, visited, takeoff, route, size):
    global answer
    if len(route) == size:
        answer.append(route)
        return
    
    if takeoff not in plan.keys():
        return
    
    stack = plan[takeoff]
    for i in stack:
        if stack.count(i) != (visited[takeoff]).count(i):
            visited[takeoff].append(i)
            dfs(plan, visited, i, route + [i], size)
            visited[takeoff].remove(i)

def solution(tickets):
    global answer
    size = len(tickets) + 1
    plan = {}
    for takeoff, landing in tickets:
        if takeoff in plan.keys():
            plan[takeoff].append(landing)
            continue
        plan[takeoff] = [landing]
    
    visited = {}
    for key in plan.keys():
        visited[key] = []

    dfs(plan, visited, "ICN", ["ICN"], size)
    answer = sorted(answer)
    return answer[0]

a = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(a))