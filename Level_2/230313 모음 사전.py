from collections import deque

def solution(word):
    answer = 0
    my_dic = {"A":1, "E":2, "I":3, "O":4, "U":5}
    compare = []
    for w in word:
        compare.append(my_dic[w])
    q = deque()
    while 1:
        answer += 1
        if len(q) < 5:
            q.append(1)
        else:
            x = q.pop()
            while x == 5:
                x = q.pop()
            q.append(x + 1)
        if list(q) == compare: break
    return answer

word = "UUUUU"
print(solution(word))