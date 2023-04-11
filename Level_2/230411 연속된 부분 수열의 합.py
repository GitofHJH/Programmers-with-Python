#  https://school.programmers.co.kr/learn/courses/30/lessons/178870
from collections import deque

def solution(sequence, k):
    sum = 0
    answer = []
    start = 0
    q = deque()
    for idx, num in enumerate(sequence):
        q.append(num)
        sum += num
        if sum < k:
            continue
        else:
            while q and sum > k:
                x = q.popleft()
                start += 1
                sum -= x
        if sum == k:
            answer.append((start, len(q)))
            x = q.popleft()
            start += 1
            sum -= x
    
    answer = sorted(answer, key=lambda x: (x[1], x[0]))
    return [answer[0][0], answer[0][0] + answer[0][1] - 1] 

a = [1, 1, 1, 2, 3, 4, 5]
b = 5
print(solution(a, b))