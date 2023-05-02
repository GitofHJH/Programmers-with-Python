# https://school.programmers.co.kr/learn/courses/30/lessons/148652
def solution(n, l, r):
    num, left, right = n, l, r
    lst = [(num, left, right)]
    while right - left >= 5:
        left //= 5
        right //= 5
        num -= 1
        lst.append((num, left, right))

    cantor = [""] * (num + 1)
    cantor[0] = "1"
    for i in range(1, num + 1):
        cantor[i] = ''.join(["11011" if int(i) else "00000" for i in cantor[i-1]])
    result = cantor[num]

    p_left = 0
    while lst:
        num, left, right = lst.pop()
        tmp = left
        left -= p_left*5
        right -= p_left*5
        result = result[left:right+1]
        p_left = tmp
        if not lst:
            break
        result = ''.join(["11011" if int(i) else "00000" for i in result])
    return result.count("1")

solution(2, 4, 17)