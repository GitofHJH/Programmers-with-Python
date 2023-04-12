# https://school.programmers.co.kr/learn/courses/30/lessons/148653
answer = int(1e9)

def recur(storey, cnt):
    global answer
    if len(storey) == 1:
        answer = min(answer, cnt + int(storey), cnt + 1 + (10 - int(storey)))
        return
    tmp = int(storey[-1])
    if tmp < 5:
        recur(storey[:-1], cnt + tmp)
    elif tmp == 5:
        recur(storey[:-1], cnt + tmp)
        recur(str(int(storey) + (10 - tmp))[:-1], cnt + (10 - tmp))
    else:
        recur(str(int(storey) + (10 - tmp))[:-1], cnt + (10 - tmp))


def solution(storey):
    global answer
    recur(str(storey), 0)
    return answer

print(solution(6))