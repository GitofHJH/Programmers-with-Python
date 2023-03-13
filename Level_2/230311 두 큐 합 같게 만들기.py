from collections import deque

def solution(queue1, queue2):
    answer = 0
    length = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    while 1:
        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            answer += 1
            sum1 -= x
            sum2 += x

        elif sum2 > sum1:
            x = q2.popleft()
            q1. append(x)
            answer += 1
            sum1 += x
            sum2 -= x
        else:
            break
        if answer >= length * 3:
            answer = -1
            break

    return answer

a = [3, 2, 7, 2]
b = [4, 6, 5, 1]
solution(a, b)