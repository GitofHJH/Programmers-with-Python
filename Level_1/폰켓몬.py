def solution(nums):
    n_nums = set(nums)
    N = len(nums)/2
    if N < len(n_nums):
        answer = N
    elif N >= len(n_nums):
        answer = len(n_nums)
    return answer