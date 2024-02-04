# https://leetcode.com/problems/2-keys-keyboard/
"""
    minimum factor will combine with maximum factor
    (minimum paste step)             (dp[m])
    otherwise cannot find any factor:
    n step: copy + n-1 paste
"""

def minSteps(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 2
    for i in range(2, n // 2):
        if n % i == 0:
            return i + minSteps(n // i)
    return n

    return helper(n)
print(minSteps(3))