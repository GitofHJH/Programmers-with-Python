def solution(s, n):
    answer = ''
    lowerAlpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upperAlpah = lowerAlpha.upper()
    for alpha in s:
        if alpha in lowerAlpha:
            answer += lowerAlpha[lowerAlpha.index(alpha)+n]
        elif alpha in upperAlpah:
            answer += upperAlpah[upperAlpah.index(alpha)+n]
        else:
            answer += ' '
    return answer