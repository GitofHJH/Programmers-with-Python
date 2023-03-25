my_dict = {'1':[1,1], '2':[1,2], '3':[1,3], '4':[2,1], '5':[2,2], '6':[2,3], '7':[3,1], '8':[3,2], '9':[3,3], '*':[4,1], '0':[4,2], '#':[4,3]}

def solution(numbers, hand):
    answer = ''
    if hand == 'left':
        leftuser = True
    else:
        leftuser = False

    L = '*'
    R = '#'
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            L = str(i)
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            R = str(i)
        elif i == 2 or i == 5 or i == 8 or i == 0:
            if abs(my_dict[L][0] - my_dict[str(i)][0]) + abs(my_dict[L][1] - my_dict[str(i)][1]) > abs(my_dict[R][0] - my_dict[str(i)][0]) + abs(my_dict[R][1] - my_dict[str(i)][1]):
                answer += 'R'
                R = str(i)
            elif abs(my_dict[L][0] - my_dict[str(i)][0]) + abs(my_dict[L][1] - my_dict[str(i)][1]) < abs(my_dict[R][0] - my_dict[str(i)][0]) + abs(my_dict[R][1] - my_dict[str(i)][1]):
                answer += 'L'
                L = str(i)
            else:
                if leftuser:
                    answer += 'L'
                    L = str(i)
                else:
                    answer += 'R'
                    R = str(i)

    return answer