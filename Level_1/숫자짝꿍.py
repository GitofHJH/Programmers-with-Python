from collections import Counter

def solution(X, Y):
    common_dict = {}
    count_X = Counter(X)
    count_Y = Counter(Y)
    for key in count_X.keys():
        if key in count_Y:
            common_dict[key] = min(count_X[key], count_Y[key])
    if common_dict == {}:
        return "-1"
    elif len(common_dict) == 1 and "0" in common_dict.keys():
        return "0"
    else:
        answer = ""
        for key in sorted(common_dict.keys(), reverse=True):
            answer += key * common_dict[key]
        return answer

x = "12321"
y = "42531"
print(solution(x, y))
