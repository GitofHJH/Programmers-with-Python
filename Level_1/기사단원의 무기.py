# 약수의 개수를 구하는 방법의 시간복잡도를 줄여야함
def factor(n, limit, power):
    count = 0
    if n == 1:
        return 1
    else:
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                count += 1
                if i**2 != n:
                    count += 1
            if count > limit:
                count = power
                break
        return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        fact = factor(i, limit, power)
        answer += fact
    return answer