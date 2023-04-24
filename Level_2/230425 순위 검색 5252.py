# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    csv = defaultdict(list)
    for i in info:
        condition = i.split()[:-1]
        score = int(i.split()[-1])
        for i in range(5):
            for combi in combinations([0,1,2,3], i):
                tmp = condition.copy()
                for idx in combi:
                    tmp[idx] = "-"
                csv[''.join(tmp)].append(score)

    for k in csv.keys():
        csv[k].sort()

    for q in query:
        q = q.replace("and", "")
        condition = ''.join(q.split()[:-1])
        score = int(q.split()[-1])
        target = csv[condition]
        start_idx = bisect_left(target, score)
        count = len(target) - start_idx
        answer.append(count)
    return answer

a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a, b))