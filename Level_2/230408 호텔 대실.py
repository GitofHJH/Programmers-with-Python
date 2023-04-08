import heapq

def solution(book_time):
    answer = 0 
    size = len(book_time)
    room = [[] for _ in range(size)]
    
    temp = []
    for start, end in book_time:
        a, b = start.split(":")
        c, d = end.split(":")
        temp.append([int(a)*60 + int(b), int(c)*60 + int(d)])
    heapq.heapify(temp)
    time = temp[0][0]
    while temp:
        for idx, r in enumerate(room):
            if r:
                if r[0] == time:
                    room[idx].pop()

        if temp[0][0] == time:
            start, end = heapq.heappop(temp)
            for i in range(size):
                if not room[i]:
                    room[i].append(end + 10)
                    answer = max(answer, i + 1)
                    break
        else:
            time += 1

    return answer

book_time1 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time2 = [["09:10", "10:10"], ["10:20", "12:20"]]
book_time3 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time1))
