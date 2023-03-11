from collections import deque

def solution(number, k):
    q = deque()
    for num in number:
        while k > 0 and q and q[-1] < num:
            q.pop()
            k -= 1
        q.append(num)
    return ''.join(list(q)[:len(q) - k])

a = "4177252741"
# a = "77774444"
print(solution(a, 4))