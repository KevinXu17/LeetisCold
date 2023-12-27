# https://leetcode.com/problems/sort-colors/description/
from typing import List

"""
    bucket
"""
def sortColors(nums: List[int]) -> None:
    # z, o, t = 0,0,0
    # for n in nums:
    #     if n == 0:
    #         z = z + 1
    #     elif n == 1:
    #         o = o + 1
    #     else:
    #         t = t + 1
    # for r in range(z):
    #     nums[r] = 0
    # for r in range(z, z + o):
    #     nums[r] = 1
    # for r in range(z + o, z+o+t):
    #     nums[r] = 2

    # l, p, r = -1, 0, len(nums)
    # while p < r:
    #     if nums[p] == 0:
    #         l = l + 1
    #         nums[p] = nums[l]
    #         nums[l] = 0
    #         p = p + 1
    #     elif nums[p] == 1:
    #         p = p + 1
    #     else:
    #         r = r - 1
    #         nums[p] = nums[r]
    #         nums[r] = 2
    from collections import Counter
    counts = Counter(nums)
    total_0 = counts[0]
    for i in range(total_0):
        nums[i] = 0
    total_1 = counts[1]
    for i in range(total_0, total_0 + total_1):
        nums[i] = 1
    total_2 = counts[2]
    for i in range(total_0 + total_1, total_0 + total_1 + total_2):
        nums[i] = 2

"""
          pointers
    low      mid      high
    1) mid == 0 => swap low mid => low mid + 1
    2) mid == 1 => mid + 1
    3) mid == 2 => high - 1
"""
def sortColors2(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

sortColors2([2,0,2,1,1,0])