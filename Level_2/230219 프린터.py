from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while 1:
        flag = False
        j = q.popleft()
        for waiting in list(q):
            if waiting[0] > j[0] and flag == False:
                q.append(j)
                flag = True
        if flag == False:
            answer += 1
            if j[1] == location:
                break
    return answer

a = [2, 1, 3, 2]
b = 2
solution(a, b)