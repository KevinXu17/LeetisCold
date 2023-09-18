## https://leetcode.com/problems/unique-binary-search-trees-ii/description/
## Time Complexity
## the nth: : G(n)=O(4^n / n^1.5)   ## https://en.wikipedia.org/wiki/Catalan_number
## Catalan number: Cn = (2n!)/( (n+1)! * n! )
## n * nth => O(4^n / n^0.5)
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


## add memoization to catch up range (x, y) result
def generateTrees(n):
    if n <= 0:
        return [None]
    mapDic = {}
    def helper(l, r):
        if l > r:
            return [None]
        if (l, r) in mapDic:
            return mapDic[(l, r)]
        res = []
        for i in range(l, r+1):
            ls = helper(l, i - 1)
            rs = helper(i+1, r)
            for a in ls:
                for b in rs:
                    res.append(TreeNode(i, a, b))
        mapDic[(l, r)] = res
        return res

    return helper(1, n)



def printNode(root):
    if root is not None:
        print('\n')
        print(root.val)
        printNode(root.left)
        printNode(root.right)

a = generateTrees(3)
for i in a:
    print('aaaaaaa')
    printNode(i)








# def generateTrees(n):
#     if n <= 0:
#         return [None]
#     return generateTreesHelper(1, n)
#
# def generateTreesHelper(s, e):
#     res = []
#     if s > e:
#         res.append(None)
#     i = s
#     while i <= e:
#         ls = generateTreesHelper(s, i - 1)
#         rs = generateTreesHelper(i+1, e)
#         for l in ls:
#             for r in rs:
#                 c = TreeNode(i)
#                 c.left = l
#                 c.right = r
#                 res.append(c)
#         i = i + 1
#     return res
