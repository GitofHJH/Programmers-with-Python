def solution(numbers):
    valid_nums = []
    nums=[0,1,2,3,4,5,6,7,8,9]
    for i in nums:
        if i in numbers:
            continue
        else:
            valid_nums.append(i)
    
    answer = sum(valid_nums)
    return answer