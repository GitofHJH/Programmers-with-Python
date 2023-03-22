from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    if len(left) == len(right):
        answer += 1
    for t in topping:
        if t not in left:
            left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        if len(left) == len(right):
            answer += 1
        
    return answer

a = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(a))