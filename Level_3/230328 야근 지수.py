# https://school.programmers.co.kr/learn/courses/30/lessons/12927
import heapq

def solution(n, works):
    if sum(works) - n <= 0:
        return 0
    works = [-x for x in works]
    heapq.heapify(works)
    for _ in range(n):
        max_num = -heapq.heappop(works)
        max_num -= 1
        heapq.heappush(works, -max_num)
    return sum([x ** 2 for x in works])

n = 4
works = [4,3,3]
solution(n, works)