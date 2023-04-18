# https://school.programmers.co.kr/learn/courses/30/lessons/68646
def solution(a):
    size = len(a)
    if size == 1:
        return 1
    answer = 2
    
    left = [a[0]]
    right = [a[-1]]
    for i in range(1, size):
        if left[-1] < a[i]:
            left.append(left[-1])
        else:
            left.append(a[i])
        if right[-1] < a[size - 1 - i]:
            right.append(right[-1])
        else:
            right.append(a[size - 1 - i])
    right.reverse()

    for i in range(1, size - 1):
        if a[i] < left[i - 1] or a[i] < right[i + 1]:
            answer += 1
            
    return answer

a = [9,-1,-5]
print(solution(a))