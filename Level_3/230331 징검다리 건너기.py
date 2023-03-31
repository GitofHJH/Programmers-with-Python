import heapq

def solution(stones, k):
    answer = 200000000
    q = []
    for i, stone in enumerate(stones):
        if i < k-1:
            heapq.heappush(q, (-stone, i))
            continue
        heapq.heappush(q, (-stone, i))
        while q[0][1] <= i - k:
            heapq.heappop(q)
        answer = min(answer, -q[0][0])
    # if answer == 200000000:
    #     answer = -q[0][0]
    return answer


a = [2, 4, 5, 4, 2, 1, 4, 2, 5, 1]
b = 3
print(solution(a, b))