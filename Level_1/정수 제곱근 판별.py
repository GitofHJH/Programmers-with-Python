def solution(n):
    if n**(1/2) - int(n**(1/2)) == 0:
        answer = ((n**(1/2))+1)**2
    else:
        answer = -1
    return answer