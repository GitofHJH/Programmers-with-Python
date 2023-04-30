# https://school.programmers.co.kr/learn/courses/30/lessons/176962
import heapq as hq

def solution(plans):
    answer = []
    for idx, plan in enumerate(plans):
        sub, start_time, taken_time = plan
        h, m = map(int, start_time.split(":"))
        plans[idx] = [h*60 + m, int(taken_time), sub]
    # print(plans)
    hq.heapify(plans)
    work_in_progress = ""
    paused_task = []
    time = plans[0][0]
    while plans or work_in_progress:
        if plans:
            if plans[0][0] == time:
                if work_in_progress:
                    paused_task.append([work_in_progress, taken_time])
                start_time, taken_time, sub = hq.heappop(plans)
                work_in_progress = sub
        time += 1
        taken_time -= 1
        if taken_time == 0:
            answer.append(work_in_progress)
            work_in_progress = ""
            if paused_task:
                work_in_progress, taken_time = paused_task.pop()
    return answer

a = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(a))