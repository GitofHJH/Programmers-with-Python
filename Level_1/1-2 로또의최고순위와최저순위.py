def solution(lottos, win_nums):
    my_dict = {}
    zero_num = 0
    crt_num = 0

    for i in range(0,7):
        if i == 0:
            my_dict[str(i)] = 6
        elif i == 1:
            my_dict[str(i)] = 6
        else:
            my_dict[str(i)] = 7-i

    for x in lottos:
        for y in win_nums:
            if x == y:
                crt_num += 1

    if 0 in lottos:
        for x in lottos:
            if x == 0:
                zero_num += 1
    
    answer = [my_dict[str(zero_num+crt_num)], my_dict[str(crt_num)]]

    return answer

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))