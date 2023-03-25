def solution(n):
    answer = ''
    a = ['수','박']
    for i in range(n):
        if i % 2 == 0:
            answer += a[0]
        else:
            answer += a[1]
    return answer