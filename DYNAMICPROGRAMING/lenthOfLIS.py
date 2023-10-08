## https://leetcode.com/problems/longest-increasing-subsequence/submissions/1070476258/
import bisect
## mem[j] = find the max(mem[i]) + 1 if nums[j] > nums[i]    i: 0 => j
## n^2
from typing import List
def lengthOfLIS(nums: List[int]) -> int:
    mem = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                mem[i] = max(mem[j] + 1, mem[i])
    return max(mem)

## n * logn  with binary search then insert to the end of list if max in list; otherwise substitute
def lengthOfLIS2(nums: List[int]) -> int:
    mem = []
    for i in range(len(nums)):
        idx = bisect.bisect_left(mem, nums[i])
        if idx == len(mem):
            mem.append(nums[i])
        else:
            mem[idx] = nums[i]
    return len(mem)
