def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수인 경우
        if number % 2 == 0:
            answer.append(number + 1)
        # 홀수인 경우
        else:
            temp = '0' + bin(number)[2:]
            for idx in range(-1, -len(temp) - 1, -1):
                if temp[idx] == '0':
                    break
            temp = list(temp)
            temp[idx] = '1'
            temp[idx + 1] = '0'
            temp = ''.join(temp)
            answer.append(int(temp, 2))
    return answer

a = [1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
print(solution(a))