# https://school.programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    for i in range(4, n + 1):
        if i % 2 == 0:
            tmp = dp[i - 2] * 3 + 2
            for x in range(2, i-4+1):
                tmp += dp[x] * 2
            dp[i] = tmp % 100000007
    return dp[n]