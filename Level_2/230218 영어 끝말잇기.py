def solution(n, words):
    stack = []

    for i in range(len(words)):
        if words[i] not in stack:
            stack.append(words[i])
            if i > 0:
                if words[i][0] != stack[-2][-1]:
                    return [(i % n) + 1, (i // n) + 1]
        else:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))