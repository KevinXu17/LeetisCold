# Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# You must solve it in O(n) time complexity.

from typing import List

## TODO SORT
# def findKthLargest(nums: List[int], k: int) -> int:
#     nums.sort()
#     return nums[-k]

import heapq
## TODO HEAP
def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    for i in range(k - 1):
        heapq.heappop(nums)
    return heapq.heappop(nums)


nums = [2, 4, 1, 5, 8]
print(findKthLargest(nums, 2))