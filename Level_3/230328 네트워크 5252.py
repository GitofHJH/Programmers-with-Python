# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def search_parent(parent, x):
    if parent[x] != x:
        parent[x] = search_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = search_parent(parent, x)
    b = search_parent(parent, y)
    if a < b:
        for idx, val in enumerate(parent):
            if val == b:
                parent[idx] = a
    else:
        for idx, val in enumerate(parent):
            if val == a:
                parent[idx] = b

def solution(n, computers):
    parent = [x for x in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                union_parent(parent, i, j)
                # print(i, j)
                # print(parent)
                # print('-'*20)
    # print(parent)
    return len(set(parent))

a = 7
b = [[1,0,0,0,0,0,1],
     [0,1,1,0,1,0,0],
     [0,1,1,1,0,0,0],
     [0,0,1,1,0,0,0],
     [0,1,0,0,1,1,0],
     [0,0,0,0,1,1,1],
     [1,0,0,0,0,1,1]]
print(solution(a, b))