def solution(n):
    ans = []
    for i in range(2,n):
        if n % i == 1:
            ans.append(i)
    return min(ans)