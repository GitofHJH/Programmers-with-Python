# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    left = k
    area = []
    while 1:
        if left % 2 == 0:
            right = left // 2
        else:
            right = left * 3 + 1
        area.append((left + right)/2)
        if right == 1:
            break
        left = right
    
    size = len(area)
    for a, b in ranges:
        if a > size + b:
            answer.append(-1)
            continue
        answer.append(sum(area[a:size + b]))
        
    return answer

a = 5
b = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(a, b))