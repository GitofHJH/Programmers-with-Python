# https://school.programmers.co.kr/learn/courses/30/lessons/17678
from collections import deque

def solution(n, t, m, timetable):
    corn = 0
    answer = ''
    timetable = sorted(timetable)
    new_tt = deque()
    for time in timetable:
        hour, min = time.split(":")
        new_tt.append(60 * int(hour) + int(min))
    
    time = 0
    bus = deque()
    bus_time = 9*60
    while time < 24*60:
        time += 1
        while new_tt:
            if new_tt[0] == time:
                x = new_tt.popleft()
                bus.append(x)
            else:
                break
        # 콘이 탈 자리가 없을 때
        if n * m <= len(bus):
            corn = bus[-1]
            while 1:
                tmp = [i for i in bus if i <= corn]
                if len(tmp) + 1 > m:
                    corn -= 1
                else:
                    break
        else:
            corn = bus_time
        if n > 0 and time == bus_time:
            n -= 1
            for _ in range(m):
                if bus:
                    bus.popleft()
            bus_time += t
        if n == 0:
            break
    return answer + str(corn // 60).zfill(2) + ":" + str(corn % 60).zfill(2)

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n,t,m,timetable))