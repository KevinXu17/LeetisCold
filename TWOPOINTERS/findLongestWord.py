# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

from typing import List
def findLongestWord(s: str, dictionary: List[str]) -> str:
    order_dict = sorted(dictionary, key=len)
    res = ""
    for w in order_dict:
        if len(w) > len(s):
            break
        l_s = 0
        for c in s:
            if l_s < len(w) and c == w[l_s]:
                l_s += 1
        if l_s == len(w):
            res = w if l_s > len(res) else min(res, w)
    return res

## use str.find(c, start, end)
def findLongestWord2(s: str, dictionary: List[str]) -> str:
    dict_ordered = sorted(dictionary, key=len)
    res = ""
    for w in dict_ordered:
        if len(w) <= len(s):
            idx = 0
            is_match = True
            for c in w:
                idx = s.find(c, idx)
                if idx == -1:
                    is_match = False
                    break
                idx += 1
            if is_match:
                res = w if len(w) > len(res) else min(res, w)
    return res


print(findLongestWord2("abpcplea", ["a","b","c"]))