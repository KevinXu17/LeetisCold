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

