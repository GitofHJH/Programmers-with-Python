def solution(s):
    my_list = list(map(int, s.split()))
    my_list.sort()

    answer = str(my_list[0]) + " " + str(my_list[-1])
    return answer