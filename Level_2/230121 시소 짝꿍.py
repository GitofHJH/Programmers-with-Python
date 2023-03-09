from itertools import combinations as combi

def solution(weights):
    answer = 0
    weights.sort()

    # 몸무게가 똑같은 애들 처리
    count = 1
    for i in range(len(weights) - 1):
        present = weights[i]
        next = weights[i + 1]
        if present != next or i == len(weights) - 1:
            answer += len(list(combi([0]*count, 2)))
            count = 1
        else:
            count += 1
    # 몸무게가 다른 애들 처리
    set_weights = list(set(weights))

    for i in range(len(set_weights)):
        zzak_list = [set_weights[i], int(set_weights[i]*2/3), int(set_weights[i]/2), int(set_weights[i]*1.5), int(set_weights[i]*0.75), int(set_weights[i]*2), int(set_weights[i]*4/3)]
        for j in range(i+1, len(set_weights)):
            if set_weights[j] in zzak_list:
                answer += 1
    return answer

weights = [100,180,360,100,270]
print(solution(weights))