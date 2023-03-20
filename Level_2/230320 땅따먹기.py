def solution(land):
    n = len(land)
    for i in range(1, n):
        for j in range(4):
            temp = []
            for k in range(4):
                if k != j:
                    temp.append(land[i][j] + land[i-1][k])
            land[i][j] = max(temp)

    return max(land[-1])