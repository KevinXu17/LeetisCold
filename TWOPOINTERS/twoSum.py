# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List


# two pointers
def twoSum(numbers: List[int], target: int):
    l = 0
    r = len(numbers)
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r =- 1
        else:
            l =+1
    return []

# dict
def twoSum1(numbers: List[int], target: int):
    num_idx = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in num_idx:
            return [num_idx[diff]+1, i+1]
        num_idx[numbers[i]] = i
    return []



