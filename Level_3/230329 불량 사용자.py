# https://school.programmers.co.kr/learn/courses/30/lessons/64064
lst = []

def recur(record, i, tmp):
    global lst
    if i == len(record):
        tmp = sorted(tmp)
        if tmp not in lst:
            lst.append(tmp)
        return
    for j in record[i]:
        if j not in tmp:
            recur(record, i + 1, tmp + [j])
    

def solution(user_id, banned_id):
    record = []
    for ban in banned_id:
        tmp = []
        for idx1, user in enumerate(user_id):
            flag = False
            if len(ban) != len(user): continue
            for idx2, val in enumerate(ban):
                if val != user[idx2] and val != "*":
                    flag = True
            if not flag:
                tmp.append(idx1)
                flag = False
        record.append(tmp)
    
    global lst
    recur(record, 0, [])
    
    return len(lst)

a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
solution(a, b)