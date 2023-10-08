## Fibonacci Sequence
## https://leetcode.com/problems/climbing-stairs/description/

## current = [current -1] + 1
## or
## current = [current - 2] + 2
## current = [current-1] + [current-2]  TODO Fibonacci Sequence
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