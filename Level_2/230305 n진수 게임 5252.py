import string

tmp = string.digits+string.ascii_uppercase

def convert(n, k):
    q, r = divmod(k, n)
    if q == 0:
        return tmp[r]
    else:
        return convert(n, q) + tmp[r]

def game(n, t, m):
    result = ''
    i = 0
    while len(result) <= t * m:
        result += convert(n, i)
        i += 1
    return result

def solution(n, t, m, p):
    answer = ''
    x = game(n, t, m)
    for i in range(len(x)):
        if i % m == p-1:
            answer += x[i]
        if len(answer) == t:
            break
    return answer
