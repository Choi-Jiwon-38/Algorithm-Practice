def solution(nums):
    n = len(nums)
    set_len = len(set(nums))
    return min(n // 2, set_len)