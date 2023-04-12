# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    my_dict = {}
    for sample in relation:
        for idx, val in enumerate(sample):
            if idx not in my_dict.keys():
                my_dict[idx] = [val]
            else:
                my_dict[idx] += [val]
    
    not_subset = []
    for c in range(1, col + 1):
        for combi in combinations([i for i in range(col)], c):
            tmp = ['' for _ in range(row)]
            for key in combi:
                for idx in range(row):
                    tmp[idx] += my_dict[key][idx]
            if len(tmp) == len(set(tmp)):
                if not not_subset:
                    not_subset.append(list(combi))
                else:
                    flag = False
                    for subset in not_subset:
                        if set(subset).issubset(set(combi)):
                            flag = True
                    if not flag:
                        not_subset.append(list(combi))
    return len(not_subset)

a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(a)