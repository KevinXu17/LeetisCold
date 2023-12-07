# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/

def reverseVowels(s: str) -> str:
    l = 0
    r = len(s) - 1
    vowels = set('aeiouAEIOU')
    res = list(s)
    while l < r:
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1
        if l < r:
            res[l] = s[r]
            res[r] = s[l]
            l += 1
            r -= 1

    return ''.join(res)