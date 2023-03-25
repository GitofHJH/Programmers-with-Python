def solution(arr1, arr2):
    n=len(arr1)
    m=len(arr2)
    answer = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer