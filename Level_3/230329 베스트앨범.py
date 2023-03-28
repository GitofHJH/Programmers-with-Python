# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    record = {}
    for i in range(len(genres)):
        if genres[i] not in record.keys():
            record[genres[i]] = [plays[i], [(i, plays[i])]]
        else:
            record[genres[i]][0] += plays[i]
            record[genres[i]][1].append((i, plays[i]))
    record = dict(sorted(record.items(), key= lambda x: x[1][0], reverse=True))
    
    for key in record.keys():
        tmp = record[key][1]
        tmp = sorted(tmp, key=lambda x: (-x[1], x[0]))
        if len(tmp) < 2:
            answer.append(tmp[0][0])
        else:
            for i in range(2):
                answer.append(tmp[i][0])
    return answer

a = ["classic", "pop", "classic", "classic", "pop"]
b = [500, 600, 150, 150, 2500]
print(solution(a, b))