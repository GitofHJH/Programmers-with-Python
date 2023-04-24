# https://school.programmers.co.kr/learn/courses/30/lessons/181187
def solution(r1, r2):
    answer = 0
    minY, maxY = r1,r2 
    for x in range(0,r2):
        while r2**2 < maxY**2 + x**2:
            maxY -= 1
        while minY-1 and r1**2 <= (minY-1)**2 + x**2:
            minY -= 1
        answer += (maxY-minY) + 1
    return answer*4