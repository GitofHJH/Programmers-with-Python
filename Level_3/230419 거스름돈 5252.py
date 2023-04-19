def solution(n, money):
    dp = [1] + [0] * n
    for m in money:
        for price in range(m, n + 1):
            dp[price] += dp[price - m]
    return dp[n] % (int(1e9) + 7)

solution(5, [1,2,5])