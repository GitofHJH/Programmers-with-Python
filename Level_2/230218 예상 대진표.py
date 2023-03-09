def solution(n,a,b):
    answer = 1
    if abs(a - b) == 1 and (a + b) % 4 == 3:
        return answer
    while 1:
        answer += 1
        a = (a + 1)//2
        b = (b + 1)//2

        if abs(a - b) == 1 and (a + b) % 4 == 3:
            break
    return answer