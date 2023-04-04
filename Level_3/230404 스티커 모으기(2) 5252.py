# https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]
    dp1 = sticker[1:]
    dp2 = sticker[:-1]
    for i in range(1, size-1):
        if i == 1:
            dp1[i] = max(dp1[i-1], dp1[i])
            continue
        dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
    for i in range(1, size-1):
        if i == 1:
            dp2[i] = max(dp2[i-1], dp2[i])
            continue
        dp2[i] = max(dp2[i] + dp2[i-2], dp2[i-1])
    return max(dp1[-1], dp2[-1])

a = [1, 1, 100, 1, 1, 100]
print(solution(a))