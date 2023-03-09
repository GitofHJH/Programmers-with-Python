from collections import deque

def solution(s):
    s = deque(s)
    q = deque()
    while s:
        present = s.popleft()
        if not q:
            q.append(present)
            continue
        else:
            previous = q.pop()
            if present != previous:
                q.append(previous)
                q.append(present)
    if q:
        return 0
    else:
        return 1

s = 'cdcd'
print(solution(s))