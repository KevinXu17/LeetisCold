## https://leetcode.com/problems/maximum-subarray/submissions/
## TODO only when current + n < 0 we get rid of it
def maxSubArray(nums):
    max_res = -100000
    current = 0
    for n in nums:
        current += n
        max_res = max(max_res, current)
        if current <= 0:
            current = 0
    return max_res
