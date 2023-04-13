# https://school.programmers.co.kr/learn/courses/30/lessons/135807
from math import gcd

def yaksu(n):
    result = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if i != n//i:
                result.append(i)
                result.append(n//i)
            else:
                result.append(i)
    return result

def gcd_N(arr):
    g = arr[0]
    for i in arr:
        g = gcd(g, i)
    return g

def solution(arrayA, arrayB):
    answer = 0
    gcd_A = gcd_N(arrayA)
    gcd_B = gcd_N(arrayB)
    for i in yaksu(gcd_A):
        flag = False
        for B in arrayB:
            if B % i == 0:
                flag = True
        if not flag:
            answer = max(answer, i)

    for i in yaksu(gcd_B):
        flag = False
        for A in arrayA:
            if A % i == 0:
                flag = True
        if not flag:
            answer = max(answer, i)
    return answer