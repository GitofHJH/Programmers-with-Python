def change(alpha, skip, index):
    count = 0
    temp = ord(alpha)
    skip = list(map(ord, skip))
    while count < index:
        temp += 1
        if temp > ord('z'):
            temp = ord('a')

        if temp not in skip:
            count += 1
    return chr(temp)

def solution(s, skip, index):
    answer = ''
    for alpha in s:
        answer += change(alpha, skip, index)
    return answer

s="aukks"
skip="wbqd"
for index in range(1,26):
    print(solution(s, skip, index))