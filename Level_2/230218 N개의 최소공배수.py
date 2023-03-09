import math
def lcm(a, b):
    return int(a * b / math.gcd(a, b))

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer

print(solution([1,2,3]))