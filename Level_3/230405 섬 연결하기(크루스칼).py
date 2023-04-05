# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def find_parent(parent, x):
    # 루트 노드가 아니라면
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, costs):
    answer = 0
    # 부모 테이블 초기화
    parent = [i for i in range(n)]
    # 비용순으로 costs 리스트 정렬
    costs = sorted(costs, key=lambda x:x[2])

    for x, y, cost in costs:
        # 사이클이 발생하지 않은 경우에만
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += cost
    return answer