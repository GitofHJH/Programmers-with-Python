import string
tmp = string.ascii_uppercase

def solution(name):
    global result
    answer = 0
    # 각 알파벳을 바꾸는데 사용한 조작 횟수
    for n in name:
        move = tmp.index(n)
        if move > 13:
            move = 26 - move
        answer += move

    # 커서 이동 최소 횟수
    min_move = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    return answer + min_move

a = "BBAAAABBB"
print(solution(a))