import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        x = heapq.heappop(scoville)
        if x >= K:
            break
        y = heapq.heappop(scoville)
        new = x + 2 * y
        if new < K and not scoville:
            answer = -1
            break
        heapq.heappush(scoville, new)
        answer += 1

    return answer

a = [1, 2, 3, 9, 10, 12]
b = 7
print(solution(a, b))