def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)

    return sorted(answer)

#def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]