def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    stack = []
    for sk in skill_trees:
        for s in sk:
            if s in skill:
                stack.append(s)
        if stack == skill[:len(stack)]:
            answer += 1
        stack = []
    return answer