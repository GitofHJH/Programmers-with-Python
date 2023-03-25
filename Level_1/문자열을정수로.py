def solution(s):
    if s.isdigit():
        answer = int(s)
    else:
        if s[0] == '+':
            answer = +int(s[1:])
        else:
            answer = -int(s[1:])
    return answer