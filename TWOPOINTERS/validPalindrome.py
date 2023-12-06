# https://leetcode.com/problems/valid-palindrome-ii/description/

def validPalindrome(s: str) -> bool:
    #     begin = 0
    #     end = len(s) - 1
    #     while begin < end:
    #         if (s[begin] != s[end]):
    #             return self.helper(s, begin + 1, end) or self.helper( s, begin, end - 1)
    #         begin = begin + 1
    #         end = end - 1
    #     return True

    # def helper(self, s: str, begin: int, end: int) -> bool:
    #     if begin == end:
    #         return True
    #     while begin < end:
    #         if (s[begin] != s[end]):
    #             return False
    #         begin = begin + 1
    #         end = end - 1
    #     return True
    mid = len(s) // 2 + 1
    after_mid_rev = s[-mid:][::-1]
    if s[:mid] == after_mid_rev:
        return True
    for i in range(mid):
        if s[i] != after_mid_rev[i]:
            return s[i + 1: mid] == after_mid_rev[i:mid - 1] or s[i:mid - 1] == after_mid_rev[i + 1:]
    return True