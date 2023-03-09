from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([0])
    for num in numbers:
        for _ in range(len(q)):
            x = q.popleft()
            q.append(x + num)
            q.append(x - num)
    print(q)
    for _ in range(len(q)):
        val = q.pop()
        if val == target:
            answer += 1
    return answer

a = [4, 1, 2, 1]
b = 4
solution(a, b)