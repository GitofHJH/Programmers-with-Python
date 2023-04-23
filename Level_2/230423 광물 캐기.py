# https://school.programmers.co.kr/learn/courses/30/lessons/172927
answer = int(1e9)

def dfs(minerals, mine_dict, cost):
    global answer
    graph = [[1,1,1], [5,1,1], [25,5,1]]
    mineral = {"diamond":0, "iron":1, "stone":2}
    if not minerals or sum([v for k, v in mine_dict.items()]) == 0:
        answer = min(answer, cost)
        return
    
    for key in mine_dict.keys():
        if mine_dict[key] > 0:
            tmp = 0
            for idx, val in enumerate(minerals):
                if idx < 5:
                    tmp += graph[key][mineral[val]]
            mine_dict[key] -= 1
            if len(minerals) >= 5:
                dfs(minerals[5:], mine_dict, cost + tmp)
            else:
                dfs([], mine_dict, cost + tmp)
            mine_dict[key] += 1
            
def solution(picks, minerals):
    global answer
    
    mine_dict = {}
    for mine, pick in zip([0, 1, 2], picks):
        if pick != 0:
            mine_dict[mine] = pick
    dfs(minerals, mine_dict, 0)
    return answer

a = [0,1,1]
b = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(a, b))