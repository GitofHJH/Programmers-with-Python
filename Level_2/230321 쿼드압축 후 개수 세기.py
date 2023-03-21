from collections import Counter
count_0 = 0
count_1 = 0

def dfs(arr):
    global count_0
    global count_1
    
    temp = []
    for ar in arr:
        temp += ar
    # 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
    if len(set(temp)) == 1:
        if set(temp) == {0}:
            count_0 -= (len(temp) - 1)
            return
        else:
            count_1 -= (len(temp) - 1)
            return
    # 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤, 
    # 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
    else:
        # 리스트 쪼개기
        l = len(arr)
        arr1, arr2, arr3, arr4 = [], [], [], []
        for i in range(0, l//2):
            arr1.append(arr[i][:l//2])
        for i in range(0, l//2):
            arr2.append(arr[i][l//2:])
        for i in range(l//2, l):
            arr3.append(arr[i][:l//2])
        for i in range(l//2, l):
            arr4.append(arr[i][l//2:])
        dfs(arr1)
        dfs(arr2)
        dfs(arr3)
        dfs(arr4)


def solution(arr):
    global count_0
    global count_1
    temp = []
    for ar in arr:
        temp += ar
    counter = Counter(temp)
    count_0 = counter[0]
    count_1 = counter[1]
    dfs(arr)

    return [count_0, count_1]

a = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(a))