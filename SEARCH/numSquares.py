import collections


def numSquares(n: int) -> int:
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

