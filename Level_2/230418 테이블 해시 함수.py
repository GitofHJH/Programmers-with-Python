# https://school.programmers.co.kr/learn/courses/30/lessons/147354
def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    s = sum([x % row_begin for x in data[row_begin - 1]])
    for i in range(row_begin + 1, row_end + 1):
        s = s ^ sum([x % i for x in data[i - 1]])
    return s

a = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
b = 2
c = 2
d = 3
solution(a,b,c,d)