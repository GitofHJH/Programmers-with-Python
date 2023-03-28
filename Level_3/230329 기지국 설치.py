# https://school.programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil

def solution(n, stations, w):
    answer = 0
    start = 1
    for station in stations:
        end = station - w
        if start < end:
            answer += ceil((end - start) / (2 * w + 1))
        start = station + w + 1
    if start <= n:
        answer += ceil((n - start + 1) / (2 * w + 1))
    return answer