def solution(nums):
    answer = 0
    a=[]
    N = len(nums)
    for x in range(N-2):       
        a.clear()
        a.append(nums[x])
        for y in range(x+1,N-1):
            if len(a) > 1:
                a.pop()
            a.append(nums[y])
            for z in range(y+1,N):
                a.append(nums[z])
                for i in range(2,sum(a)):
                    if sum(a) % i != 0:
                        if i == sum(a)-1: 
                            answer +=1
                            a.pop()
                        continue                  
                    else:
                        a.pop()
                        break              
    return answer