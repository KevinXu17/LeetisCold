# https://leetcode.com/problems/sum-of-square-numbers/description/
import math

def judgeSquareSum(c: int):
    l = 0
    r = int(math.sqrt(c))
    while l <= r:
        if l * l + r * r == c:
            return True
        elif l * l + r * r > c:
            r -= 1
        else:
            l += 1
    return False


# prime
# if c % 4 == 3, then c must cant be expressed as 2 square number sum
# a positive integer can be expressed as the sum of two squares if and
# only if every prime factor of the form 4n + 3 occurs an even number of times in its prime factorization.
def judgeSquareSum(c: int):
    sqrt_c = int(c ** 0.5)
    divisor_map = [0] * (sqrt_c + 1)
    for i in range(2, sqrt_c + 1):
        if divisor_map[i] == 0:
            # for j in range(i, sqrt_c, i):
            #     divisor_map[j] = 1
            ## update this improve performance to cross out not prime number
            divisor_map[i::i] = [1] * ((sqrt_c - i) // i + 1)
            count = 0
            while c % i == 0:
                count += 1
                c //= i
            if i % 4 == 3 and count % 2 != 0:
                return False
    return c % 4 != 3


