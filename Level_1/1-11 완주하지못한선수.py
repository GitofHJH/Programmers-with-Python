def solution(participant, completion):
    parHash = {}
    comHash = {}
    for x in participant:
        if x not in parHash.keys():
            parHash[x] = 1
        else:
            parHash[x] += 1
    for x in completion:
        if x not in comHash.keys():
            comHash[x] = 1
        else:
            comHash[x] += 1
    for i in parHash.keys():
        if i not in comHash.keys():
            answer = i
        elif parHash[i] != comHash[i]:
            answer = i
    return answer