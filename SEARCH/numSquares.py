import collections

# https://leetcode.com/problems/perfect-squares/description/

"""
    1)
    assume diff is the destination of result if it reaches 0
    if some diff is marked, which means some less # combination have been reached there
    and wont put into the queue
    candidate: diff
    view: diff
    2)
    dynamic programing version
"""

def numSquares(n: int) -> int:
    """
        only use add to fine all square #
        1 4 9 16 25 ...
         3 5 7  9 ...
    """
    def getSquares(num):
        res = []
        diff = 3
        i = 1
        while i <= num:
            res.append(i)
            i = i + diff
            diff = diff + 2
        return res

    squares = getSquares(n)
    mem_map = [0] * (n + 1)
    # Queue for all unseen diff
    que = collections.deque()
    que.append((0, n))
    while 1 == 1:
        level, num = que.popleft()
        nextLevel = level + 1
        for s in squares:
            diff = num - s
            if diff < 0:
                break
            if diff == 0:
                return nextLevel
            if mem_map[diff] == 1:
                continue
            mem_map[diff] = 1
            que.append((nextLevel, diff))

print(numSquares(4))

