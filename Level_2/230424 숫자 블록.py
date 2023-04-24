# https://school.programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    def func(n):
        result = []
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                if i <= int(1e7):
                    result.append(i)
                if i**2 != n and i != 1:
                    if n//i <= int(1e7):
                        result.append(n//i)
        return max(result)
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        if i % 2 == 0:
            if i//2 <= int(1e7):
                answer.append(i//2)
            else:
                answer.append(func(i))
            continue
        answer.append(func(i))
    return answer

print(solution(1,2))