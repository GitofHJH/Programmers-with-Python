def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                if j == i and count % 2 == 0:
                    answer += j
                elif j == i and count % 2 == 1:
                    answer -= j
    return answer

print(solution(13,17))