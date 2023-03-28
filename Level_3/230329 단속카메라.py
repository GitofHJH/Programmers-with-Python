# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 1
    routes = sorted(routes, key= lambda x: x[0])
    print(routes)
    camera = routes[0][1]
    for idx, val in enumerate(routes[1:]):
        if val[0] <= camera:
            camera = min(camera, val[1])
        else:
            answer += 1
            camera = val[1]
    return answer

a = [[-20,-15], [-20,-5], [-18,-13], [-5,-3]]
print(solution(a))