# https://school.programmers.co.kr/learn/courses/30/lessons/92342
from itertools import product

def solution(n, info):
    info.reverse()
    lion_result = list(product([True, False], repeat=11))
    max_diff = 0
    for result in lion_result:
        arrow = sum(info[i] + 1 for i in range(11) if result[i])
        if arrow <= n:
            lion_score = sum(i for i in range(11) if result[i])
            apeach_score = sum(i for i in range(11) if not result[i] and info[i])
            diff = lion_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                answer = [info[i] + 1 if result[i] else 0 for i in range(11) ]
                answer[0] = n - arrow
    answer.reverse()
    return answer

a = 9
b = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(a, b))