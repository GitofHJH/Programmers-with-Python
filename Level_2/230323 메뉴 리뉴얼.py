from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        record = {}
        for order in orders:
            tmp = sorted(list(order))
            for combi in combinations(tmp, c):
                if ''.join(combi) in record.keys():
                    record[''.join(combi)] += 1
                else:
                    record[''.join(combi)] = 1
        answer += [k for k, v in record.items() if max(record.values()) == v and v >= 2]
    answer = sorted(answer)
    
    return answer

a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b = [2,3,4]

solution(a, b)