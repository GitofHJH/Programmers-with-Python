def solution(N, stages):
    answer = []
    f_rate = {}
    x = 0
    for i in range(1,N+1):
        f_rate[i] = 0
    for stage in sorted(stages):
        if stage in f_rate.keys():
            f_rate[stage] += 1
    for i in range(1,N+1):
        if f_rate[i] == 0:
            continue
        else:
            tmp = f_rate[i]
            f_rate[i] = tmp/(len(stages)-x)
            x += tmp
    sorted_f_rate = sorted(f_rate.items(), key= lambda x: x[1], reverse= True)
    for i in sorted_f_rate:
        answer.append(i[0])
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))