# https://leetcode.com/problems/count-primes/description/

## Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime,
# starting with the first prime number, 2. The multiples of a given prime are generated as a sequence
# of numbers starting from that prime, with constant difference between them that is equal to that prime.
# This is the sieve's key distinction from using trial division to sequentially test each candidate number
# for divisibility by each prime.
# Once all the multiples of each discovered prime have been marked as composites,
# the remaining unmarked numbers are primes.

## logic:
## 1） mark all not primes with their factors from 2 to sqrt(n)

def countPrimes(n):
    if n < 3:
        return 0
    marks = [1] * n
    marks[0] = marks[1] = 0
    m = 2
    ## begin with 2; using m * m rather than sqrt
    while m * m < n:
        # no prime num has been marked by other factors before
        if marks[m] == 1:
        # 1) why begin with m*m, since k*m k<m has been marked
        # 2) why n-1 => since n is not include in this problem
        # 3) mark all nums with factor m as not prime
            marks[m*m: n: m] = [0] * ((n - 1 - m*m) // m + 1)
        # sequence 2, 3, 5, 7, 9....
        m += 1 if m == 2 else 2
    for i in range(2, n-1):
        if marks[i] == 1:
            print(i)
    return sum(marks)

import math
# second version to get rid of num with factor 2
# marks
# 0 1 2 3 4 5 ...
# 3 5 7 9 11 13...
def countPrimes2(n):
    if n < 3:
        return 0
    marks = [1] * (n//2)
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if marks[i//2 - 1] == 1:
            for mul in range(i*i, n, 2*i):
                marks[mul//2 - 1] = 0
    for i in range(len(marks)):
        if marks[i] == 1:
            print(3 + i * 2)
    return sum(marks)


def countPrimes3(n: int) -> int:
    if n < 3:
        return 0
    marks = [1] * (n // 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if marks[i // 2 - 1] == 1:
            marks[i * i // 2 - 1: n // 2 - 1: i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    for i in range(len(marks)):
        if marks[i] == 1:
            print(3 + i * 2)
    return sum(marks)



countPrimes3(49)