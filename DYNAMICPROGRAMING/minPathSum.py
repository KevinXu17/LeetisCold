## TODO this 2D input maybe not need to think as 2D
## TODO loop as 1D sts will be much faster

## https://leetcode.com/problems/minimum-path-sum/description/
from typing import List

"""
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
"""
## dp x y
def minPathSum(grid: List[List[int]]) -> int:
    ## dp[(x, y)] = min(dp[(x-1, y)], dp[(x, y - 1)]) + itself
    dic_map = {}
    dic_map[(0, 0)] = grid[0][0]

    def helper(x, y):
        if (x, y) in dic_map:
            return dic_map[(x, y)]
        min_before = 0
        if x - 1 >= 0 and y - 1 >= 0:
            min_before = min(helper(x-1, y), helper(x, y -1))
        elif x - 1 >= 0:
            min_before = helper(x-1, y)
        elif y - 1 >= 0:
            min_before = helper(x, y-1)
        dic_map[(x, y)] = min_before + grid[x][y]
        return min_before + grid[x][y]
    return helper(len(grid)-1, len(grid[0]) - 1)

## dp only keep 0 to len(grid) - 1
##  1) first loop the first row get result
## 2) loop other row: and the min is (current_row - 1 (left) or current (up))
def minPathSum1(grid: List[List[int]]) -> int:
    rows = len(grid)
    idx = len(grid[0])
    res = [0] * idx
    res[0] = grid[0][0]
    rows = len(grid)
    idx = len(grid[0])
    for i in range(1, idx):
        res[i] = res[i - 1] + grid[0][i]

    for r in range(1, rows):
        for i in range(0, idx):
            if i == 0:
                res[0] = res[0] + grid[r][i]
            else:
                res[i] = min(res[i - 1], res[i]) + grid[r][i]
    return res[idx - 1]



print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))