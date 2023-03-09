from math import ceil

def solution(progresses, speeds):
    answer = []
    time_taken = []
    for i in range(len(progresses)):
        time_taken.append(ceil((100 - progresses[i]) / speeds[i]))
        
    count = 1
    present = time_taken[0]
    for i in range(1, len(time_taken)):
        if time_taken[i] <= present:
            count += 1
        else:
            answer.append(count)
            count = 1
            present = time_taken[i]
    answer.append(count)

    return answer

a = [93, 30, 55]
b = [1, 30, 5]
solution(a, b)