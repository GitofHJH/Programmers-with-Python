# https://school.programmers.co.kr/learn/courses/30/lessons/169198
def solution(m, n, startX, startY, balls):
    answer = []
    def func(x1, y1, x2, y2, m, n):
        ans1, ans2, ans3, ans4 = int(1e9), int(1e9), int(1e9), int(1e9)
        # 좌
        if not (y1==y2 and x1 > x2):
            ans1 = (x1 + x2)**2 + (y1 -y2)**2
        # 우
        if not (y1==y2 and x1 < x2):
            ans2 = (2*m-x1-x2)**2 + (y1-y2)**2
        # 상
        if not (x1==x2 and y1 < y2):
            ans3 = (x1-x2)**2 + (2*n-y1-y2)**2
        # 하
        if not (x1==x2 and y1 > y2):
            ans4 = (x1-x2)**2 + (y1+y2)**2
        return min(ans1, ans2, ans3, ans4)
    for x2, y2 in balls:
        answer.append(func(startX, startY, x2, y2, m, n))
    return answer

m=10
n=10
x=3
y=7
b=[[7, 7], [2, 7], [7, 3]]
print(solution(m,n,x,y,b))