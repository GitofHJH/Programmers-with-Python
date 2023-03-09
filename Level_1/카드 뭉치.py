from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for char in goal:
        if cards1:
            one = cards1.popleft()
        if cards2:
            two = cards2.popleft()
        if char == one:
            cards2.appendleft(two)
        elif char == two:
            cards1.appendleft(one)
        else:
            return "No"
    return "Yes"