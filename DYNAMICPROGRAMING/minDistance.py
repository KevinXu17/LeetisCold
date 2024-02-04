def minDistance(word1: str, word2: str) -> int:
    w1_len = len(word1)
    w2_len = len(word2)
    mem = [[0] * (w2_len + 1) for i in range(w1_len + 1)] # IMPORTANT not the same as [[0] * 3] * 3

    for i in range(1, w1_len + 1):
        for j in range(1, w2_len + 1):
            if word1[i - 1] == word2[j - 1]:
                mem[i][j] = mem[i - 1][j - 1] + 1
            else:
                mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])
    return w1_len + w2_len - 2 * mem[w1_len][w2_len]

print(minDistance("intention", "execution"))

import bisect

"""
    use bisect to do quick search for idx of same char
"""
def minDistance2(word1: str, word2: str) -> int:
    pattern = {}
    for i, x in enumerate(word1):
        if x in pattern:
            pattern[x].append(i)
        else:
            pattern[x] = [i]

    dp = [len(word1)] * len(word1)
    for x in word2:
        if x in pattern:
            for i in reversed(pattern[x]):
                dp[bisect.bisect_left(dp, i)] = i

    return len(word1) + len(word2) - 2 * bisect.bisect_left(dp, len(word1))




# https://leetcode.com/problems/edit-distance/submissions/1165608616/
    def minDistance3(word1: str, word2: str) -> int:
        w1_len = len(word1)
        w2_len = len(word2)

        mem = [[0] * (w2_len + 1) for i in range(w1_len + 1)] # IMPORTANT not the same as [[0] * 3] * 3
        for m in range(w1_len + 1):
            mem[m][0] = m
        for n in range(w2_len + 1):
            mem[0][n] = n


        for i in range(1, w1_len + 1):
            for j in range(1, w2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    mem[i][j] = mem[i - 1][j - 1]
                else:
                    mem[i][j] = min(mem[i - 1][j-1], mem[i-1][j], mem[i][j-1]) + 1
        return mem[w1_len][w2_len]