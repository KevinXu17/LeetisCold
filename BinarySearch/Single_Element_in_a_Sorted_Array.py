# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# 0   1  #2  3 4
# the dupilicate word's position predict the odd word's position

def singleNonDuplicate(nums) -> int:
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r - l) // 2
        mIsEven = m % 2 == 0

        if (nums[m - 1] == nums[m] and mIsEven) or (not mIsEven and nums[m] == nums[m + 1]):
            r = m
        else:
            l = m + 1
    return nums[l - 1]