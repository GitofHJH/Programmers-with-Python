# import Counter 가 더 빠름

def solution(k, tangerine):
    my_list = [0] * (max(tangerine) + 1)
    for t in tangerine:
        my_list[t] += 1
    my_list.sort(reverse=True)

    answer = 0
    for count in my_list:
        k -= count
        answer += 1
        if k <= 0: break
    
    return answer

# from collections import Counter

# def solution(k, tangerine):
#     answer = 0
#     counter = dict(Counter(tangerine))
#     counter = dict(sorted(counter.items(), key=lambda x: -x[1]))
#     print(counter)
#     for key, val in counter.items():
#         k -= val
#         answer += 1
#         if k <= 0:
#             break
#     return answer