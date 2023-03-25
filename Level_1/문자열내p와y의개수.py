def solution(s):
    answer = True
    s = s.lower()
    check_p = 0
    check_y = 0
    for i in s:
        if i == 'p':
            check_p += 1
        elif i == 'y':
            check_y += 1
    if check_p != check_y:
        answer = False
    return answer