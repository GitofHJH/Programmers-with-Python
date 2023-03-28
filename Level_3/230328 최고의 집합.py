# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    if s < n:
        return [-1]
    ans = []
    tmp = round(s/n)
    print(tmp)
    diff = s - n * tmp
    print(diff)
    if diff < 0:
        for _ in range(abs(diff)):
            ans.append(tmp - 1)
        for _ in range(n - abs(diff)):
            ans.append(tmp)
    else:
        for _ in range(abs(diff)):
            ans.append(tmp  + 1)
        for _ in range(n - abs(diff)):
            ans.append(tmp)
    return sorted(ans)
print(solution(2, 9))