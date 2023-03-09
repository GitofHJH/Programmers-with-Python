def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i=commands[x][0]
        j=commands[x][1]
        k=commands[x][2]
        new_array = sorted(array[i-1:j])
        answer.append(new_array[k-1])
    
    return answer