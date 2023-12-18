from typing import List
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# 1 built-in sort
def findKthLargest(nums: List[int], k: int) -> int:
    nums_ordered = sorted(nums)
    return nums_ordered[-k]

# 2 counting sort (Fast, bad mem)
"""
    arrayVal COUNT         # count nums
    arrayIdx 0 1 2 3 4 ... # nums
"""
def findKthLargest2(nums: List[int], k: int) -> int:
    min_num = min(nums)
    max_num = max(nums)

    counts = [0] * (max_num - min_num + 1)
    for num in nums:
        counts[num - min_num] += 1

    remain = k
    for i in range(max_num - min_num + 1, -1, -1):
        if counts[i] == 0 or remain - counts[i] > 0:
            remain -= counts[i]
        else:
            return min_num + i
    return -1

# 3 heapq
import heapq
def findKthLargest3(nums: List[int], k: int) -> int:
    hq = [-10000] * k
    heapq.heapify(hq)

    for n in nums:
        heapq.heappush(hq, n)
        heapq.heappop(hq)
    return heapq.heappop(hq)

# 4 quick sort until find k
def findKthLargest4(nums: List[int], k: int) -> int:
    k = len(nums) - k
    l = 0
    r = len(nums) - 1
    while l < r:
        k_can = partition(nums, l, r)
        if k == k_can:
            return nums[k]
        elif k > k_can:
            l = k_can + 1
        else:
            r = k_can - 1
    return nums[k]

def partition(nums: List[int], l: int, r: int) -> int:
    i = l
    j = r + 1
    while True:
        i += 1
        while i < r and nums[i] < nums[l]:
            i += 1
        j -= 1
        while j > l and nums[j] > nums[l]:
            j -= 1
        if i >= j:
            break
        swap(nums, i, j)
    swap(nums, l, j)
    return j

def swap(nums: List[int], i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


findKthLargest4([3,3,3,3], 1)