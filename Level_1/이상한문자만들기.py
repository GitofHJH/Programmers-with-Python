def solution(s):
    answer = ''
    my_list = s.split(' ')
    for str in my_list:
        for i in range(len(str)):
            if i % 2 == 0:
                answer += str[i].upper()
            else:
                answer += str[i].lower()
        answer += ' '
    return answer

print(solution("try hello world"))