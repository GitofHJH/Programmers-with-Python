def solution(ingredient):
    answer = 0
    stacking = []
    for i in range(len(ingredient)):
        stacking.append(ingredient[i])
        while stacking[-4:] == [1,2,3,1]:
            for _ in range(4):
                stacking.pop()
            answer += 1
    return answer