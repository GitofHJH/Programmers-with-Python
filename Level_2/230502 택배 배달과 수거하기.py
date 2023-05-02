# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()
            
        target = max(len(deliveries), len(pickups))
        answer += target * 2
        num_d = cap
        num_p = cap
        for i in range(len(deliveries) - 1, -1, -1):
            if deliveries[i] <= num_d:
                num_d -= deliveries[i]
                deliveries.pop()
            else:
                deliveries[i] -= num_d
                break
        for i in range(len(pickups) - 1, -1, -1):
            if pickups[i] <= num_p:
                num_p -= pickups[i]
                pickups.pop()
            else:
                pickups[i] -= num_p
                break
    return answer

a=2
b=7
c=[1, 0, 2, 0, 1, 0, 2]
d=[0, 2, 0, 1, 0, 2, 0]
solution(a,b,c,d)