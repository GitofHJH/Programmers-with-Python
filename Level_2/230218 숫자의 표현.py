def count(n):
    answer = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            answer += 1
            if i**2 != n:
                answer += 1
    return answer

def division(n):
    while n % 2 != 1:
        n /= 2
    return n

def solution(n):
    if n % 2 == 0:
        answer = count(division(n))
    else:
        answer = count(n)
    return answer

print(division(2))
print(solution(2))