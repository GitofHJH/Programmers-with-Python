# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    mydict = {}
    for n, y in zip(name, yearning):
        mydict[n] = y
    for p in photo:
        tmp = [mydict[i] if i in mydict.keys() else 0 for i in p ]
        answer.append(sum(tmp))
    return answer