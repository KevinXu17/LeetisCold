def longestPalindrome(s: str) -> str:
    mapDic = {}
    def helper(l, r):
        if (l, r) in mapDic:
            return mapDic[(l, r)]
        if l == r:
            mapDic[(l, r)] = True
        elif l == r - 1:
            mapDic[(l, r)] = s[l] == s[r]
        else:
            mapDic[(l,r)] = helper(l+1, r-1) and s[l] == s[r]
        return mapDic[(l ,r)]
    a  = 0
    b = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if helper(i, j):
                if j - i > b - a:
                    a = i
                    b = j
    return s[a: b+1]


print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))