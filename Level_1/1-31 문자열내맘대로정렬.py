def solution(strings, n):
    answer = []
    strings = sorted(strings)
    a={}
    for i in range(len(strings)):
        a[i] = strings[i][n]
    a = sorted(a.items(), key = lambda item: item[1])
    for i in range(len(a)):
        answer.append(strings[a[i][0]])
    return answer