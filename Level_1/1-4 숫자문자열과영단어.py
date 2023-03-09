def solution(s):
    word =["zero", "one", "two","three", "four", "five", "six", "seven", "eight", "nine"]
    result=''

    i=0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            result += s[i]
            i += 1
        else:
            for x in range(10):
                if s.find(word[x],i,i+5) != -1:
                    result += str(x)
                    i += len(word[x])
                    break  

    answer = int(result)
    return answer

print(solution("123"))