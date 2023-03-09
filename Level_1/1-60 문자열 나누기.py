def solution(s):
    answer = 0
    while s:
        x = s[0]
        x_count = 1
        count = 0
        for i in range(1, len(s)):
            if s[i] == x:
                x_count += 1
            else:
                count += 1
            if x_count == count:
                s = s[i+1:]
                answer += 1
                break
        if len(s)-1 == i:
            answer += 1
            break
    return answer

s = "banana"
print(solution(s))