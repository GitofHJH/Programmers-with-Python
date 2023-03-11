def solution(record):
    answer = []
    nickname = {}
    result = []
    for r in record:
        temp = r.split()
        if temp[0] == "Enter":
            result.append((temp[1], "님이 들어왔습니다."))
            nickname[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            result.append((temp[1], "님이 나갔습니다."))
        else:
            nickname[temp[1]] = temp[2]
    for user, ment in result:
        answer.append(nickname[user] + ment) 
    return answer