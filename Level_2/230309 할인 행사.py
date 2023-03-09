def solution(want, number, discount):
    answer = 0
    wants = []
    for n, p in zip(number, want):
        for _ in range(n):
            wants.append(p)
    for i in range(len(discount) - 10 + 1):
        if sorted(wants) == sorted(discount[i:i+10]):
            answer += 1
    return answer