def solution(order):
    idx = 0 
    stack = []
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1

    return len(order) - len(stack)

a = [5,4,3,2,1]
solution(a)