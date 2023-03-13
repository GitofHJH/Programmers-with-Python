import math
from itertools import permutations

def check(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    pm = []
    for i in range(1, len(numbers) + 1):
        for x in permutations(numbers, i):
            # print(''.join(x))
            tmp = int(''.join(x))
            print(tmp, check(tmp))
            if check(tmp) and tmp not in pm:
                pm.append(tmp)
                answer += 1
    return answer

a = "17"
solution(a)