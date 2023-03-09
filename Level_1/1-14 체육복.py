def solution(n, lost, reserve):
    s_lost = set(lost)-set(reserve)
    s_reserve = set(reserve)-set(lost)
    
    for reserve in s_reserve:
        front = reserve-1
        back = reserve+1
        if front in s_lost:
            s_lost.remove(front)
        elif back in s_lost:
            s_lost.remove(back)
    return n-len(s_lost)
