from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        present = people.pop()
        if present > limit - 40:
            answer += 1
        else:
            people.append(present)
            break
    while people:
        heavy = people.pop()
        if people:
            light = people.popleft()
            if heavy + light <= limit:
                answer += 1
            else:
                people.appendleft(light)
                answer += 1
        else:
            answer += 1
        
    return answer

people = [70, 60, 80, 60, 60]
limit = 100
print(solution(people, limit))