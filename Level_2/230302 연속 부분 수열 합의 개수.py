def solution(elements):
    result = []
    length = len(elements)
    circle_q = elements + elements
    for i in range(1, length + 1):
        start = 0
        end = start + i
        for j in range(length):
            new_start = start + j
            new_end = end + j
            summation = sum(circle_q[new_start:new_end])
            result.append(summation)
    
    return len(set(result))

a = [7,9,1,1,4]
print(solution(a))