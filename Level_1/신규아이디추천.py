def isValid(c):
    if c.isalnum():
        return True
    if c == '-' or c == '_' or c == '.':
        return True
    else: return False

def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    lastDot = False

    for x in new_id:
        if isValid(x) == False:
            continue

        if x == '.':
            if len(answer) == 0 or lastDot:
                continue
            lastDot = True
        else:
            lastDot = False

        x = x.lower()
        answer += x

    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]
        if len(answer) >= 3: break
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))