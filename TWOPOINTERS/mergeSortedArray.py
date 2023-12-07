# https://leetcode.com/problems/merge-sorted-array/description/
from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    left, right = m - 1, n - 1
    put_in = m + n - 1
    while right >= 0:
        if left < 0 or nums1[left] <= nums2[right]:
            nums1[put_in] = nums2[right]
            right = right - 1
        else:
            nums1[put_in] = nums1[left]
            left = left - 1
        put_in = put_in - 1

    # start = m
    # for val in nums2:
    #     nums1[start] = val
    #     start += 1
    # nums1.sort()