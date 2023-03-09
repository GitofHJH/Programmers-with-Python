def solution(begin, end):
    greb = [0] * (end - begin + 1)

    for n in range(1, end//2 + 1):
        length = len(greb[n*2:end+1:n])
        greb[n*2:end+1:n] = [n] * length
        
    return greb[1:]

print(solution(10, 20))