def solution(arr):
    minVal = min(arr)
    del arr[arr.index(minVal)]
    if arr:
        answer = arr
    else:
        answer = [-1]
    return answer

print(solution([1,2,3,4]))