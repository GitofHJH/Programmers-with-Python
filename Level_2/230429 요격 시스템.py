# https://school.programmers.co.kr/learn/courses/30/lessons/181188
from collections import deque

def solution(targets):
    answer = 1
    targets = deque(sorted(targets, key=lambda x: x[1]))
    
    s, e = targets.popleft()
    while targets:
        ns, ne = targets.popleft()
        if e <= ns:
            answer += 1
            s, e = ns, ne
            continue
        s = max(s, ns)
        e = min(e, ne)
    return answer

a = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(a))