# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) == 0:
#             return [-1, -1]
#         smallest = self.getLargestIndex(nums, target)
#         if smallest == len(nums) or nums[smallest] != target:
#             return [-1,-1]
#         largest = self.getLargestIndex(nums, target + 1) - 1
#         return [smallest, largest]
#
#     def getLargestIndex(self, nums, target):
#         l = 0
#         r = len(nums)
#         while l < r:
#             m = (l + r)//2
#             m_num = nums[m]
#             if m_num < target:
#                 l = m+1
#             else:
#                 r = m
#         return l