def solution(s):
    s = s[2:-2]
    s_list = s.split("},{")
    s_list = sorted([list(map(int, x.split(','))) for x in s_list], key=lambda x: len(x))

    answer = s_list[0]
    for i in range(1, len(s_list)):
        present = s_list[i]
        for j in answer:
            present.remove(j)
        answer += present
    
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)