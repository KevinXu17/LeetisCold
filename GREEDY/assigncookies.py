
## https://leetcode.com/problems/assign-cookies/description/

"""
    greedy always come with sort
"""
def findContentChildren(g, s) -> int:
    g.sort()
    s.sort()
    res, gi, si = 0, 0 ,0
    while gi < len(g) and si < len(s):
        if g[gi] <= s[si]:
            res += 1
            gi += 1
            si += 1
        else:
            si += 1
    return res