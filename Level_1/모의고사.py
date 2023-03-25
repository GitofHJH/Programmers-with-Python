def solution(answers):
    answer = []
    one = [1,2,3,4,5,1,2,3,4,5]*1000
    two = [2,1,2,3,2,4,2,5]*1250
    three = [3,3,1,1,2,2,4,4,5,5]*1000
    cor_one = 0
    cor_two = 0
    cor_three = 0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            cor_one += 1
    for i in range(len(answers)):
        if answers[i] == two[i]:
            cor_two += 1
    for i in range(len(answers)):
        if answers[i] == three[i]:
            cor_three += 1
    temp = [cor_one, cor_two, cor_three]
    maxval = max(temp)
    for i in range(3):
        if maxval == temp[i]:
            answer.append(i+1)

    return answer