def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[s//2]
    else:
        answer = s[s//2-1:s//2]
    return answer