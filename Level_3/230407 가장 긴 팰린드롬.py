# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    answer = 0
    size = len(s)
    for i in range(size):
        for j in range(i + 1, size + 1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                answer = max(answer, j-i)

    return answer