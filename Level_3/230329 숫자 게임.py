# https://school.programmers.co.kr/learn/courses/30/lessons/12987
from collections import deque

def solution(A, B):
    answer = 0
    A = deque(sorted(A))
    B = deque(sorted(B))

    for _ in range(len(A)):
        a = A.pop()
        b = B.pop()
        if a >= b:
            B.append(b)
            b = B.popleft()
            if a < b:
                answer += 1
        else:
            answer += 1

    return answer