from itertools import permutations
from collections import deque
import copy

def solution(expression):
    answer = 0
    tmp = ''
    for e in expression:
        if not e.isdigit():
            tmp += e
    operand = list(set(list(tmp)))

    list_exp = []
    for e in expression:
        if e.isdigit():
            if list_exp and list_exp[-1].isdigit():
                x = list_exp.pop()
                list_exp.append(x + e)
            else:
                list_exp.append(e)
        else:
            list_exp.append(e)
    list_exp = deque(list_exp)          
    exp_org = copy.deepcopy(list_exp)
    # 연산 우선순위 조합
    for perm in permutations(operand, len(operand)):
        # 우선순위 연산 하나씩 꺼내서 먼저 계산
        list_exp = copy.deepcopy(exp_org)
        for i in perm:
            stack = []
            while list_exp:
                tmp = list_exp.popleft()
                if tmp != i:
                    stack.append(tmp)
                else:
                    if tmp == '+':
                        x = stack.pop()
                        y = list_exp.popleft()
                        stack.append(int(x) + int(y))
                    elif tmp == '*':
                        x = stack.pop()
                        y = list_exp.popleft()
                        stack.append(int(x) * int(y))
                    else:
                        x = stack.pop()
                        y = list_exp.popleft()
                        stack.append(int(x) - int(y))
            list_exp = deque(stack)
        answer = max(answer, abs(stack[0]))
                
    return answer

a = "100-200*300-500+20"
solution(a)