from math import ceil

def solution(fees, records):
    answer = []
    in_dict = {}
    out_dict = {}
    # 입출차 기록 만들기
    for r in records:
        time, car_num, in_out = r.split()
        if in_out == "IN":
            if car_num not in in_dict.keys():
                in_dict[car_num] = [time]
                out_dict[car_num] = []
            else:
                in_dict[car_num].append(time)
        else:
            out_dict[car_num].append(time)

    # 출차 기록 없는 경우 추가
    for key in in_dict.keys():
        if len(in_dict[key]) != len(out_dict[key]):
            out_dict[key].append("23:59")

    # key 값으로 오름차순 정렬
    in_dict = dict(sorted(in_dict.items()))
    out_dict = dict(sorted(out_dict.items()))

    # 주차 요금 계산
    for key in in_dict.keys():
        total = 0
        for i, o in zip(in_dict[key], out_dict[key]):
            i = int(i[0:2]) * 60 + int(i[3:])
            o = int(o[0:2]) * 60 + int(o[3:])
            total += (o - i)
        if total > fees[0]:
            answer.append(fees[1] + ceil((total - fees[0])/fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer