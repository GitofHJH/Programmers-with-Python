from collections import deque

def solution(s):
    q = deque()
    count = 0
    for char in s:
        if not q and char == ")":
            return False
        if char == "(":
            q.append(char)
            count += 1
            continue
        if char == ")" and count > 0:
            q.pop()
            count -= 1
    if count == 0:
        return True
    else:
        return False