def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    digit = 0
    origin_n = n
    while n >= k:
        n = n // k
        digit += 1
    n = origin_n

    jinsu = ''
    for i in range(digit, -1, -1):
        jinsu += str(n // (k ** i))
        n -= (n // (k ** i)) * (k ** i) 

    answer = 0
    for x in jinsu.split('0'):
        if x != '' and is_prime(int(x)):
            answer += 1
    return answer

n = 437674
k = 3
print(solution(n, k))