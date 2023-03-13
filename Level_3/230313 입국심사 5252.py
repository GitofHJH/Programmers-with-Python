def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while start <= end:
        total = 0
        mid = (start + end) // 2
        print(mid)
        for t in times:
            total += (mid // t)
        # 시간이 충분하면 시간 줄이기
        if total >= n:
            end = mid - 1
            answer = mid
        # 시간이 부족하면 시간 늘리기
        else:
            start = mid + 1
    return answer

a = 6
b = [7,10]
print(solution(a, b))