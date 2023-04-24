# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq

def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    answer = k
    cover_k = enemy[:k]
    heapq.heapify(cover_k)
    
    while 1:
        n -= heapq.heappushpop(cover_k, enemy[k])
        if n < 0:
            break
        k += 1
        answer += 1
        if k >= len(enemy): break
        
    return answer

a = 7
b = 3
c = [4, 2, 4, 5, 3, 3, 1]
print(solution(a,b,c))