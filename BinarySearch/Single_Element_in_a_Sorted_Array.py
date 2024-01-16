# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
"""
    Normal index: even and odd are the same
    0 1 2 3 4 5 6 7
    1 1 2 2 3 3 4 4
    when some odd appear, even and odd are not the same
    0 1 2 3 4 5 6
    1 1 2 3 3 4 4
    the dupilicate word's position predict the odd word's position

"""

def singleNonDuplicate(nums) -> int:
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r - l) // 2
        mIsEven = m % 2 == 0
        # if even, and it is normal, we jump ahead + 2
        if mIsEven and m + 1 < len(nums) and nums[m] == nums[m + 1]:
            l = m + 2
        # if odd, and it is normal, we only jump + 1
        elif not mIsEven and nums[m] == nums[m - 1]:
            l = m + 1
        else:
            r = m
    return nums[l]


print(singleNonDuplicate([1]))