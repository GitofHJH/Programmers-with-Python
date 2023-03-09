def solution(citations):
    citations = [0] + sorted(citations, reverse=True)
    answer = 0
    for i in range(1, len(citations)):
        if citations[i] >= i:
            answer = i
        else:
            break
    return answer

citations = [5,5,5,5]
print(solution(citations))