def solution(n):
    answer = 0
    i=0
    ans = []
    while True:
        if 3**i > n:
            break
        i += 1
    while True:
        i = i-1
        mok_nmz = divmod(n, 3**i)
        ans.append(mok_nmz[0])
        n = mok_nmz[1]
        if i == 0:
            break
    for i in range(len(ans)):
        answer += ans[i]*(3**i)
    return answer