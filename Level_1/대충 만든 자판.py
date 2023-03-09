def solution(keymap, targets):
    answer = []
    
    for target in targets:
        result = 0
        for char in target:
            idx = 101
            for key in keymap:
                if char in key:
                    idx = min(idx, key.index(char))
            if idx == 101:
                result = -1
            if result == -1:
                continue
            else:    
                result += (idx + 1)
        answer.append(result)
    return answer

a = ["ABACD", "BCEFD"]
b = ["ABCD","AABB"]
print(solution(a, b))