# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def recur(cards, open, start, group):
    if open[start] == True:
        return group, open
    open[start] = True
    group.append(start)
    return recur(cards, open, cards[start], group)

def solution(cards):
    answer = 0
    size = len(cards)
    cards = [0] + cards
    for i in range(1, size + 1):
        open = [False] * (size + 1)
        group_1, open = recur(cards, open, i, [])
        for j in range(1, size + 1):
            if j not in group_1:
                group_2, _ = recur(cards, open, j, [])
                answer = max(answer, len(group_1) * len(group_2))
    return answer

a = [8,6,3,7,2,5,1,4]
solution(a)