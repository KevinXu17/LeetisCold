## https://leetcode.com/problems/integer-break/description/

# 2  1*1 = 1
# 3  1*2 = 2  # edge since has 1
# 4  2*2 = 4
# 5  2*3 = 6
# 6  3*3 = 9
# 7   max(f(5)* 2 or f(4) * 3)
# ...

def integerBreak(n):
    mem = [0, 0, 1, 2, 4, 6, 9]
    if n <= 6:
        return mem[n]
    mem = mem + [0] * (n - 6)
    i = 7
    while i <= n:
        mem[i] = max(mem[i - 2] * 2, mem[i - 3] * 3)
        i = i + 1
    return mem[n]

## math formula
##  n % 3 == 0 => 3 ** (n//3)
##  n % 3 == 1 => 3 ** (n//3 - 1) * 4
##  n $ 3 == 2 => 3 ** (n//3) * 2