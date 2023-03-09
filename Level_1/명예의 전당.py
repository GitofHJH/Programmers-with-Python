def solution(k, score):
    answer = []
    record = []
    for i in range(len(score)):
        record.append(score[i])
        record =sorted(record, reverse=True)
        if i < k:
            answer.append(record[-1])
        else:
            answer.append(record[k-1])
    return answer