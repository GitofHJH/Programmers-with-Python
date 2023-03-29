# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# def solution(gems):
#     short = len(gems)
#     all_gem = list(set(gems))
#     print(all_gem)
#     index_dict = {}
#     for idx, gem in enumerate(all_gem):
#         index_dict[gem] = idx

#     num_gem = len(all_gem)
#     index_list = [0] * num_gem

#     for i, gem in enumerate(gems):
#         index_list[index_dict[gem]] = i + 1
#         if 0 not in index_list:
#             print(index_list)
#             max_idx = max(index_list)
#             min_idx = min(index_list)
#             tmp = max_idx - min_idx
#             if tmp < short:
#                 answer = [min_idx, max_idx]
#                 short = tmp
#     return answer

def solution(gems):
    answer = [0, len(gems) - 1]
    start = 0
    end = 0
    size = len(set(gems))
    gem_dict = {gems[start] : 1}
    while start < len(gems) and end < len(gems):
        # 보석 종류가 모두 들어온 경우
        if len(gem_dict) == size:
            # 최소값 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]] == 0:
                    del gem_dict[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems): break
            if gems[end] in gem_dict:
                gem_dict[gems[end]] += 1
            else:
                gem_dict[gems[end]] = 1
    return [answer[0] + 1, answer[1] + 1]

a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(a))
