# https://leetcode.com/problems/sort-characters-by-frequency/description/
"""
    Counter vs normal self make dictionary
    https://stackoverflow.com/questions/43956930/why-does-a-dictionary-count-in-some-cases-faster-than-collections-counter
    Counter is slow with short iterables
    Faster in long iterables
"""
# bucket sort
from collections import Counter

def frequencySort(s: str) -> str:
    bucket = Counter(s)
    char_frequency = sorted(bucket.items(), key=lambda x: x[1], reverse= True)
    res = ''
    for c in char_frequency:
        k, i = c
        res += k * i
    return res

    # return ''.join([i * j for i, j in sorted({i: s.count(i) for i in set(s)}.items,
    # key = lambda item: item[1], reverse = True)])
