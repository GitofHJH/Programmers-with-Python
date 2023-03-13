def solution(N, number):
    if N == number:
        return 1
    possible = []
    for cnt in range(1, 9):
        partial_set = set()
        partial_set.add(int(str(N) * cnt))
        for i in range(cnt - 1):
            for op1 in possible[i]:
                for op2 in possible[-i-1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 - op2)
                    partial_set.add(op1 * op2)
                    if op2 != 0:
                        partial_set.add(op1 // op2)
            if number in partial_set:
                return cnt
        possible.append(partial_set)
    return -1