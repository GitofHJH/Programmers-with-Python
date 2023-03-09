import numpy as np

def solution(arr1, arr2):
    answer = []
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    result = arr1.dot(arr2)
    for i in result:
        answer.append(list([int(x) for x in i]))
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

print(solution(arr1, arr2))