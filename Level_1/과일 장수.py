from collections import deque

def solution(k, m, score):
    answer = 0
    score = sorted(score)
    q = deque(score)
    while len(q) >= m:
        box = []
        for _ in range(m):
            box.append(q.pop())
        answer += min(box) * m
    return answer