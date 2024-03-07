# https://leetcode.com/problems/daily-temperatures/
from typing import List

"""
    use stack to store all pre-idx, when current idx value > pre-idx, we get the result of pre-idx
"""
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    idxs = []
    for i in range(len(temperatures)):
        while (len(idxs) > 0 and temperatures[i] > temperatures[idxs[-1]]):
            pre_idx = idxs.pop()
            res[pre_idx] = i - pre_idx
        idxs.append(i)
    return res


# https://leetcode.com/problems/next-greater-element-ii/
"""
    version 2: assume nums is circle
"""
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    stack = [] # idxs
    for i in range(len(nums)):
        while(stack and nums[i] > nums[stack[-1]]):
            pre_idx = stack.pop()
            res[pre_idx] = nums[i]
        stack.append(i)
    for i in range(len(nums)):
        while(stack and nums[i] > nums[stack[-1]]):
            pre_idx = stack.pop()
            res[pre_idx] = nums[i]
    return res
