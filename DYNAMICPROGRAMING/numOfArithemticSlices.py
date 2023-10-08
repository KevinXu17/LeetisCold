## https://leetcode.com/problems/arithmetic-slices/description/
from typing import List


# 1 2 3 4 5
#
# 1 2 3     a[0] = 1
# 1 2 3 4   a[1] = a[0] + 1   ## 1234 is 123 + 4
#   2 3 4
# 1 2 3 4 5 a[2] = a[1] + 1
#   2 3 4 5
#     3 4 5


def numberOfArithmeticSlices(nums: List[int]) -> int:
    l = len(nums)
    if l < 3:
        return 0
    mem = [0] * len(nums)
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            mem[i] = mem[i-1] + 1
    return sum(mem)