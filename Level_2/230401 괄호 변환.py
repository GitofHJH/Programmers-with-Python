# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def balance(p):
    check = 0
    for idx, char in enumerate(p):
        if char == "(":
            check += 1
        else:
            check -= 1
        if check == 0:
            i = idx
            break
    return p[:i + 1], p[i + 1:]

def correct(u):
    check = 0
    for idx, char in enumerate(u):
        if char == "(":
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    return True

def func(p):
    # 1
    if p == '':
        return ''
    # 2
    u, v = balance(p)
    # 3
    if correct(u):
        # 3-1
        return u + func(v)
    # 4
    # 4-1
    tmp = "("
    # 4-2
    tmp += func(v)
    # 4-3
    tmp += ")"
    # 4-4
    u = u[1:-1]
    tmp2 = ''
    for char in u:
        if char == ")":
            tmp2 += "("
        else:
            tmp2 += ")"
    u = tmp2
    # 4-5

    return tmp + u

def solution(p):
    if correct(p):
        return p
    answer = ''
    answer = func(p)
    return answer