# https://school.programmers.co.kr/learn/courses/30/lessons/140107
def pita(length, i):
    return int((length**2 - i**2)**(1/2))

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        answer += (pita(d, i)//k + 1)
    return answer

print(solution(2, 5))