def solution(triangle):
    # i는 현재 값을 바꿔야할 층
    for i in range(1, len(triangle)):
        # 현재 층의 인덱스
        for idx in range(len(triangle[i])):
            # 가장 왼쪽
            if idx == 0:
                triangle[i][idx] += triangle[i - 1][0]
            # 가장 오른쪽
            elif idx == len(triangle[i]) - 1:
                triangle[i][idx] += triangle[i-1][-1]
            # 중간
            else:
                left = triangle[i][idx] + triangle[i - 1][idx - 1]
                right = triangle[i][idx] + triangle[i - 1][idx]
                triangle[i][idx] = max(left, right)
                
    return max(triangle[-1])