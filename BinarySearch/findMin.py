# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""
    binary search with RANGE
    we check l m r to find out min
    l     m       r
    0 1 2 3 4 5 6 7
    4 5 6 7 0 1 2 3

"""
def findMin(nums) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[l] <= nums[m] and nums[m] <= nums[r]:
            return nums[l]
        elif nums[l] > nums[m]:
            r = m
        else:
            l = m + 1
    return nums[l]