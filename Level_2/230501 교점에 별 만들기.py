def solution(line):
    coordinate = set()
    max_x = -int(1e15)
    min_x = int(1e15)
    max_y = -int(1e15)
    min_y = int(1e15)
    for a, b, e in line:
        for c, d, f in line:
            deno = a*d - b*c
            # 기울기가 같은 경우
            if deno == 0:
                continue
            x = b*f - e*d
            y = e*c - a*f
            if x % deno == 0 and y % deno == 0:
                x = x/deno
                y = y/deno
                max_x = max(max_x, x)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                min_y = min(min_y, y)
                coordinate.add((x, y))
    len_x = int(max_x - min_x)
    len_y = int(max_y - min_y)
    answer = [list("." * (len_x + 1)) for _ in range(len_y + 1)]
    coordinate = [list(map(int, [x - min_x, y - min_y])) for x, y in coordinate]
    
    for x, y in coordinate:
        answer[len_y - y][x] = "*"

    answer = [''.join(i) for i in answer]
    return answer

a = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(a))