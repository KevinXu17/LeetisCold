# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # pathSumRoot => A to leaf
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.pathSumRoot(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def pathSumRoot(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        res = 0
        if root.val == targetSum:
            res += 1
        return res + self.pathSumRoot(root.left, targetSum - root.val) + self.pathSumRoot(root.right, targetSum - root.val)

"""
    O(n): DFS + dictionary
    
    since the path MUST be continuous:
    10     5           3               3
    10     15          18              21  # sum previous #
           15-10=5     18-15=3              # get itself
                        18-10=8 (5+3)        # get some path
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[0] = 1  # Initialize the lookup dictionary with 0 sum having 1 count
        def dfs(node, root_sum):
            if not node:
                return
            root_sum += node.val
            # Update total count with the number of paths ending at the current node that sum up to targetSum
            self.total += self.lookup[root_sum - targetSum]
            # Increment the count of current sum in the lookup dictionary
            self.lookup[root_sum] += 1
            # Recur for left and right subtrees
            dfs(node.left, root_sum)
            dfs(node.right, root_sum)
            # Decrement the count of current sum after traversing its subtrees
            self.lookup[root_sum] -= 1
        dfs(root, 0)
        return self.total

