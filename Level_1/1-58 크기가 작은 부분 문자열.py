def solution(t, p):
    l = len(p)
    answer = 0
    for i in range(len(t) - len(p) + 1):
        compare = t[0 + i : l + i]
        if compare <= p:
            answer += 1
    return answer