# https://leetcode.com/problems/non-decreasing-array/description/
from typing import List

"""
    the choices we have are whether change p1 or p2
    [p0] [p1] [p2] [p3]
    trigger condiction: p1 > p2
    since non-decreasing, we need to consider p0 and p3 too
    if p0 > p2 => p2 = p1
    else p1 = p2
"""
def checkPossibility(nums: List[int]) -> bool:
    new_nums = [-100000] + nums + [100000]
    change = 1
    for i in range(2, len(nums) + 1):
        if new_nums[i - 1] > new_nums[i]:
            change -= 1
            if change < 0:
                return False
            if new_nums[i - 2] > new_nums[i]:
                new_nums[i] = new_nums[i - 1]
            else:
                new_nums[i - 1] = new_nums[i - 2]
    return change >= 0


# class Solution {
# public:
#     bool checkPossibility(vector<int>& nums) {
#         int chance = 1;
#         if (nums.size() <= 2) return true;
#         for (int i = 1; i < nums.size(); i++) {
#             if (nums[i - 1] > nums[i]) {
#                 chance--;
#                 if (chance < 0) {
#                     return false;
#                 }
#
#                 if (i+1 == nums.size() || (i - 2 >=0 && nums[i-2] > nums[i])) {
#                     nums[i] = nums[i - 1];
#                 } else {
#                     nums[i - 1] = nums[i];
#                 }
#
#             }
#         }
#         return chance >= 0;
#     }
# };