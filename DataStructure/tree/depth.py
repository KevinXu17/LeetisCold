# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

from collections import deque
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    # bfs
    q = deque([root])
    level = 0
    while q:
        for i in range(len(q)):
            item = q.popleft()
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        level += 1
    return level

# isbalance => compare the height of left and right


# diameter => sum left and right when computing the height
# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_height_helper(root)
        return self.diameter

    def max_height_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left:
            l = self.max_height_helper(root.left)
        else:
            l = 0
        if root.right:
            r = self.max_height_helper(root.right)
        else:
            r = 0
        self.diameter = max(self.diameter, l + r)
        return 1 + max(l, r)


    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     def dfs(root):
    #         if not root:
    #             return (0,True)
    #         left,right= dfs(root.left), dfs(root.right)
    #         return (1+max(left[0],right[0]), left[1] and right[1] and (abs(left[0]-right[0]) <=1 ) )
    #     return dfs(root)[1]==True


# https://leetcode.com/problems/path-sum/description/
# path sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)





