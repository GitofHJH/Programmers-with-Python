from collections import deque

def correct(s):
    q = deque()
    for char in s:
        if not q and char in [")", "]", "}"]:
            return False
        elif char in ["(", "[", "{"]:
            q.append(char)
        else:
            previous = q.pop()
            if previous + char == "()" or previous + char == "[]" or previous + char == "{}":
                continue
            else:
                return False
    if not q:
        return True

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        rotate = s.popleft()
        s.append(rotate)
        if correct(list(s)):
            answer += 1
    return answer

s = "[](){}"
print(solution(s))