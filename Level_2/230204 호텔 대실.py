def plus10m(time):
    start = time[0]
    end = time[1]
    hour, minute = end.split(':')
    minute = int(minute) + 10
    if minute > 59:
        minute -= 60
        hour = int(hour) + 1
    minute = str(minute).zfill(2)
    end = str(hour).zfill(2) + ":" + minute
    return [start, end]

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

def solution(book_time):
    new_book_time = []
    for time in book_time:
        new_book_time.append(plus10m(time))
    book_time = sorted(new_book_time)

    parent = [0] * len(book_time)
    for i in range(len(book_time)):
        parent[i] = i

    for i in range(len(book_time)):
        for j in range(i+1, len(book_time)):
            i = find_parent(parent, i)
            # j = find_parent(parent, j)
            if book_time[i][1] <= book_time[j][0]:
                union_parent(parent, i, j)

    return parent
book_time1 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time2 = [["09:10", "10:10"], ["10:20", "12:20"]]
book_time3 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time3))
print(sorted(book_time3))