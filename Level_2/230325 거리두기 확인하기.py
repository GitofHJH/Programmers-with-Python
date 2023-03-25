def get_person(place, x, y):
    result = []
    dir = [(2,0), (1,1), (0,2), (-1,1), (-2,0), (-1,-1), (0,-2), (1,-1)]
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if place[nx][ny] == "P":
            result.append((nx, ny))
    return result

# 거리두기를 지키면 True를 리턴
def check1(place, x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        if place[x1][y2] == "X" and place[x2][y1] == "X":
            return True
        return False
    else:
        if place[int((x1+x2)/2)][int((y1+y2)/2)] == "X":
            return True
        return False

# 1칸 내에 응시자가 없으면 True를 리턴
def check2(place, x1, x2):
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    for dx, dy in dir:
        nx = x1 + dx
        ny = x2 + dy
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if place[nx][ny] == "P":
            return False
    return True

def solution(places):
    answer = []
    for place in places:
        flag = False
        for x1 in range(5):
            for y1 in range(5):
                if place[x1][y1] == "P":
                    for x2, y2 in get_person(place, x1, y1):
                        if not check1(place, x1, y1, x2, y2):
                            flag = True
                    if not check2(place, x1, y1):
                        flag = True
        if flag: answer.append(0)
        else: answer.append(1)
    return answer

a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(a)

