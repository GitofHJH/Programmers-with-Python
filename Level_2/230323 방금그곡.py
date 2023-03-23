def solution(m, musicinfos):
    answer = ''
    record = []
    for music in musicinfos:
        start, end, name, info = music.split(',')
        whole_length = (int(end.split(':')[0]) * 60 + int(end.split(':')[1])) - (int(start.split(':')[0]) * 60 + int(start.split(':')[1]))
        
        play_info = []
        for i in info:
            if i == '#':
                x = play_info.pop()
                play_info.append(x+i)
            else:
                play_info.append(i)
        
        list_m = []
        for i in m:
            if i == '#':
                x = list_m.pop()
                list_m.append(x+i)
            else:
                list_m.append(i)
        
        if whole_length >= len(play_info):
            play_info = play_info * (whole_length // len(play_info)) + play_info[:whole_length % len(play_info)]
        else:
            play_info = play_info[:whole_length]
        
        # 음악 정보 문자열 변환
        convert_m = ' '.join(list_m) + ' '
        convert_play = ' '.join(play_info) + ' '
        
        if convert_m in convert_play:
            record.append((name, whole_length))
    record = sorted(record, key=lambda x: x[1], reverse=True)
    if record:
        answer = record[0][0]
    else:
        answer = "(None)"
    return answer

a = "ABC"
b = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(a, b))