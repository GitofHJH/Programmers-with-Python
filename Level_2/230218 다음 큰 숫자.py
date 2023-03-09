from collections import Counter

def solution(n):
    answer = n + 1
    count_one = Counter(bin(n))['1']

    while Counter(bin(answer))['1'] != count_one:
        answer += 1
    
    return answer