# https://leetcode.com/problems/first-bad-version/description/
"""
    after bad version, all are bad
    0 1 2 3 4 5 6 ....
"""

def firstBadVersion(n: int) -> int:
    l, r = 0, n
    while l < r:
        m = l + (r - l) // 2
        if isBadVersion(m):
            r = m
        else:
            l = m + 1
    return l