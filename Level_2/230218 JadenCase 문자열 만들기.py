def solution(s):
    answer = ""
    s = s.lower()
    flag = True
    for char in s:
        if flag and char.isdigit():
            answer += char
            flag = False
        elif flag and char.isalpha():
            answer += char.upper()
            flag = False
        elif char == " ":
            answer += char
            flag = True
        else:
            answer += char

    return answer

s = "3people unFollowed  me"
print(solution(s))