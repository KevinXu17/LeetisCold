## Fibonacci Sequence
## https://leetcode.com/problems/climbing-stairs/description/
## dp[i] = dp[i-1] + dp[i-2]

## current = [current -1] + 1
## or
## current = [current - 2] + 2
## current = [current-1] + [current-2]  TODO Fibonacci Sequence -> only keep two vars
def climbStairs(n: int) -> int:
    mem = {}
    mem[0] = 0
    mem[1] = 1
    mem[2] = 2
    def helper(i):
        if i in mem:
            return mem[i]
        res = helper(i-1) + helper(i-2)
        mem[i] = res
        return res

    return helper(n)

def climbStairs2(n: int) -> int:
    before_before = 1
    before = 1
    for i in range(2, n + 1):
        before, before_before = before + before_before, before
    return before