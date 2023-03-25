day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(a, b):
    days = 0
    if a == 1:
        days = b
    else:
        for i in range(a-1):
            days += month[i]
        days += b
    answer = day[days % 7]
    
    return answer

