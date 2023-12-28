from collections import deque, defaultdict
from typing import List
# https://leetcode.com/problems/word-ladder/description/

"""
    candidate: word in each pattern
    view: word
"""
def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    word_map = defaultdict(list)
    for w in wordList:
        for i in range(len(w)):
            pattern = w[:i] + '*' + w[i+1:]
            word_map[pattern].append(w)
    que = deque([(beginWord, 1)])
    visited = set([beginWord])
    while que:
        current_word, level = que.popleft()
        if current_word == endWord:
            return level
        for i in range(len(current_word)):
            newPattern = current_word[:i] + '*' + current_word[i+1:]
            for nw in word_map[newPattern]:
                if nw not in visited:
                    visited.add(nw)
                    que.append((nw, level + 1))
    return 0



print(ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))

