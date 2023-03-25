def solution(s):
    word_dict = {}
    word_list = []
    answer = []
    for i in range(len(s)):
        if s[i] not in word_list:
            word_list.append(s[i])
            word_dict[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - word_dict[s[i]])
            # 최근 위치 정보 갱신
            word_dict[s[i]] = i

    return answer